import numpy as np
from numba import njit

@njit
def P(y, Pv, lambda_khi, S, W0, qfi, omega_sum, psis, powders):
    thet = theta(psis, powders)
    chisl = 0
    znam = 0
    for i in range(len(powders)):
        f = powders[i][2]
        om = powders[i][0]
        delta = powders[i][1]
        alpha = powders[i][5]
        chisl += f*psis[i]*om
        znam += om*(((1-psis[i])/delta) + alpha*psis[i])
    p_mean = Pv + (chisl - thet*y[0]**2 * (qfi/2 + lambda_khi * omega_sum/6))/(W0 - znam + S*y[1])
    p_sn = (p_mean/(1 + (1/3) * (lambda_khi*omega_sum)/qfi))*(y[0] > 0.) + (y[0] == 0.)*p_mean
    p_kn = (p_sn*(1 + 0.5*lambda_khi*omega_sum/qfi))*(y[0] > 0.) + (y[0] == 0.)*p_mean

    return p_mean, p_sn, p_kn

@njit
def theta(psis, powders):
    sum1 = 0
    sum2 = 0
    for i in range(len(powders)):
        sum1 += powders[i][2] * powders[i][0] * psis[i] / powders[i][3]
        sum2 += powders[i][2] * powders[i][0] * psis[i] / (powders[i][3] * powders[i][6])
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
        return psiS + kappa2*z1*(1 + lambd2*z1 +mu2*z1**2)
    else:
        return 1

@njit
def int_bal_rs(y, P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders):
    """
    Функция правых частей системы уравнений внутреней баллистики при аргументе t
    """
    f = np.zeros(2 + len(powders))
    psis = np.zeros(len(powders))
    for i in range(len(powders)):
        psis[i] = psi(y[2 + i], *powders[i][7:])
    lambda_khi = (y[1] + l_k)/(y[1] + l_ps)

    p_mean, p_sn, p_kn = P(y, PV, lambda_khi, S, W0, qfi, omega_sum, psis, powders)
    if y[0] == 0. and p_mean < P0:
        f[0] = 0
        f[1] = 0
    else:
        f[0] = (p_sn*S)/(qfi)
        f[1] = y[0]
    for k in range(len(powders)):
        if p_mean <= 50e6:
            f[2+k] = ((k50*p_mean**0.75)/powders[k][4]) * (y[2+k] < powders[k][7])
        else:
            f[2+k] = (p_mean/powders[k][4]) * (y[2+k] < powders[k][7])
    return f, p_mean, p_sn, p_kn

@njit
def solve_ib(P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, l_d, powders, tmax = 1. , tstep = 1e-5):
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
    while y[1] <= l_d:
        k1, p_mean1, p_sn1, p_kn1 = int_bal_rs(y, P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)
        k2, p_mean2, p_sn2, p_kn2 = int_bal_rs(y+tstep*k1/2, P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)
        k3, p_mean3, p_sn3, p_kn3 = int_bal_rs(y+tstep*k2/2, P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)
        k4, p_mean4, p_sn4, p_kn4 = int_bal_rs(y+tstep*k3, P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)
        y += tstep*(k1 + 2*k2 + 2*k3 + k4)/6
        t0 += tstep
        p_mean_max = max(p_mean1, p_mean2, p_mean3, p_mean4, p_mean_max)
        p_sn_max = max(p_sn1, p_sn2, p_sn3, p_sn4, p_sn_max)
        p_kn_max = max(p_kn1, p_kn2, p_kn3, p_kn4, p_kn_max)
        if np.all(zk_list <= y[2:]) and lk == 0.:
            lk = y[1]
        if t0 > tmax:
            raise Exception("Превышено максимальное время выстрела\nОшибка расчета!")
    return y, p_mean_max, p_sn_max, p_kn_max, lk

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
            raise Exception("Превышено максимальное время выстрела\nОшибка расчета!")

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
            raise Exception("Превышено максимальное время выстрела\nОшибка расчета!")
        dy_array = dy_array[1:] + [last_dy]
    return y, p_mean_max, p_sn_max, p_kn_max, lk
