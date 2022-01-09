import numpy as np
from numba import njit
from InternalBallistics.ErrorClasses import *

@njit
def P(y, igniter, lambda_khi, S, W0, qfi, omega_sum, psis, powders):
    thet = theta(psis, igniter, powders)
    fs = igniter.fs
    for i, powder in enumerate(powders):
        fs += powder.f_powd * powder.omega * psis[i]
        W0 -= powder.omega * ((1. - psis[i]) / powder.rho + psis[i] * powder.alpha)
    fs -= thet * y[0] ** 2 * (qfi / 2 + lambda_khi * omega_sum / 6.)
    W0 += y[1] * S
    if W0 < 0.:
        raise TooMuchPowderError()
    p_mean = 1e5 + fs / W0
    p_sn = (p_mean/(1 + (1/3) * (lambda_khi*omega_sum)/qfi))*(y[0] > 0.) + (y[0] == 0.)*p_mean
    p_kn = (p_sn*(1 + 0.5*lambda_khi*omega_sum/qfi))*(y[0] > 0.) + (y[0] == 0.)*p_mean

    return p_mean, p_sn, p_kn

@njit
def theta(psis, igniter, powders):
    sum1 = igniter.sum1
    sum2 = igniter.sum2
    for i, powder in enumerate(powders):
        sum1 += powder.f_powd * powder.omega * psis[i] / powder.Ti
        sum2 += powder.f_powd * powder.omega * psis[i] / (powder.Ti * powder.teta)
    if sum2 != 0:
        return sum1 / sum2
    else:
        return 0.4

@njit
def psi(z, zk, kappa1, lambd1, mu1, kappa2, lambd2, mu2):
    if z < 1:
        return kappa1*z*(1 + lambd1*z + mu1*z**2)
    elif 1 <= z <= zk:
        z1 = z - 1
        psiS = kappa1 + kappa1*lambd1 + kappa1*mu1
        return psiS + kappa2*z1*(1 + lambd2*z1 + mu2*z1**2)
    else:
        return 1

@njit
def int_bal_rs(dy, y, psis, P0, igniter, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders):
    """
    Функция правых частей системы уравнений внутреней баллистики при аргументе t
    """
    for i, powder in enumerate(powders):
        psis[i] = psi(y[2 + i], *powder[7:])
    lambda_khi = (y[1] + l_k)/(y[1] + l_ps)

    p_mean, p_sn, p_kn = P(y, igniter, lambda_khi, S, W0, qfi, omega_sum, psis, powders)
    if y[0] == 0. and p_mean < P0:
        dy[0] = 0.
        dy[1] = 0.
    else:
        dy[0] = p_sn*S/qfi
        dy[1] = y[0]
    for i, powder in enumerate(powders):
        if p_mean <= 50e6:
            dy[2+i] = ((k50*p_mean**0.75)/powder.Jk) * (y[2+i] < powder.Zk)
        else:
            dy[2+i] = (p_mean/powder.Jk) * (y[2+i] < powder.Zk)
    return p_mean, p_sn, p_kn

@njit
def solve_ib(P0, igniter, k50, S, W0, l_k, l_ps, omega_sum, qfi, l_d, powders, tmax = 1., tstep = 1e-5):
    """

    :param P0:
    :param igniter:
    :param k50:
    :param S:
    :param W0:
    :param l_k:
    :param l_ps:
    :param omega_sum:
    :param qfi:
    :param l_d:
    :param powders:
    :param tmax:
    :param tstep:
    :return:
    """
    y = np.zeros(2+len(powders))
    lk = 0. # Координата по стволу, соответсвующая полному сгоранию порохового заряда
    t0 = 0. # Начальное время
    p_mean_max = 1e5
    p_sn_max = 1e5
    p_kn_max = 1e5

    K = np.zeros((4, len(y)))

    psis = np.zeros(len(powders))

    while y[1] <= l_d:

        # Проверка условия сгорания всего заряда
        if np.all(1.<= psis) and lk == 0.:
            lk = y[1]

        p_mean1, p_sn1, p_kn1 = int_bal_rs(K[0], y, psis, P0, igniter, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)
        p_mean2, p_sn2, p_kn2 = int_bal_rs(K[1], y + tstep * K[0] / 2, psis, P0, igniter, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)
        p_mean3, p_sn3, p_kn3 = int_bal_rs(K[2], y + tstep * K[1] / 2, psis, P0, igniter, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)
        p_mean4, p_sn4, p_kn4 = int_bal_rs(K[3], y + tstep * K[2], psis, P0, igniter, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)
        y += tstep*(K[0] + 2*K[1] + 2*K[2] + K[3])/6
        t0 += tstep
        p_mean_max = max(p_mean1, p_mean2, p_mean3, p_mean4, p_mean_max)
        p_sn_max = max(p_sn1, p_sn2, p_sn3, p_sn4, p_sn_max)
        p_kn_max = max(p_kn1, p_kn2, p_kn3, p_kn4, p_kn_max)

        if t0 > tmax:
            raise TooMuchTime()

    psi_sum = 0
    for i, powder in enumerate(powders):
        y[2+i] = psi(y[2 + i], *powder[7:])
        psi_sum += y[2+i]*powder.omega
    psi_sum /= omega_sum
    return y, p_mean_max, p_sn_max, p_kn_max, psi_sum, lk/l_d

@njit
def solve_ib_ab5(P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, l_d, powders, tmax = 1. , tstep = 1e-5):
    """

    :param P0:
    :param PV:
    :param k50:
    :param S:
    :param W0:
    :param l_k:
    :param l_ps:
    :param omega_sum:
    :param qfi:
    :param l_d:
    :param powders:
    :param tmax:
    :param tstep:
    :return:
    """
    y = np.zeros(2+len(powders))
    zk_list = np.array([powders[i][7] for i in range(len(powders))])
    lk = 0. # Координата по стволу, соответсвующая полному сгоранию порохового заряда
    t0 = 0.
    p_mean_max = PV
    p_sn_max = PV
    p_kn_max = PV

    dy_array = []

    for i in range(4):
        k1, _, _, _ = int_bal_rs(y, P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)
        k2, _, _, _ = int_bal_rs(y + tstep * k1 / 2, P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)
        k3, _, _, _ = int_bal_rs(y + tstep * k2 / 2, P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)
        k4, _, _, _ = int_bal_rs(y + tstep * k3, P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)

        y += tstep * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t0 += tstep

        if np.all(zk_list <= y[2:]) and lk == 0.:
            lk = y[1]
        if t0 > tmax:
            raise TooMuchTime()

        dy_new, p_mean, p_sn, p_kn = int_bal_rs(y, P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)
        p_mean_max = max(p_mean, p_mean_max)
        p_sn_max = max(p_sn, p_sn_max)
        p_kn_max = max(p_kn, p_kn_max)
        dy_array.append(dy_new)

    while y[1] <= l_d:
        last_dy, p_mean, p_sn, p_kn = int_bal_rs(y, P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)
        y += tstep*((1901 / 720) * last_dy - (1387 / 360) * dy_array[3] + (109 / 30) * dy_array[2] - (637 / 360) * dy_array[1] + (251 / 720) * dy_array[0])
        t0 += tstep
        p_mean_max = max(p_mean, p_mean_max)
        p_sn_max = max(p_sn, p_sn_max)
        p_kn_max = max(p_kn, p_kn_max)
        if np.all(zk_list <= y[2:]) and lk == 0.:
            lk = y[1]
        if t0 > tmax:
            raise TooMuchTime()
        dy_array = dy_array[1:] + [last_dy]
    return y, p_mean_max, p_sn_max, p_kn_max, lk
