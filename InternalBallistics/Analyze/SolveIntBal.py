import numpy as np
from collections import deque
import matplotlib.pyplot as plt


def adams_bashford5(f, y0, t0, t_end, tau, args, stopfunc=None):
    def runge_step(f, t, y, tau, args):
        k1 = tau * f(t, y, *args)
        k2 = tau * f(t, y + k1 / 2, *args)
        k3 = tau * f(t, y + k2 / 2, *args)
        k4 = tau * f(t, y + k3, *args)
        increment = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        return y + increment, f(t + tau, y + increment, *args)

    if not stopfunc:
        stopfunc = lambda t, y: t <= t_end

    dy_que = deque(maxlen = 4)
    ys = [y0]
    ts = [t0]
    for _ in range(4):
        y0, dy = runge_step(f, t0, y0, tau, args)
        t0 += tau
        if stopfunc(t0, y0):
            ys.append(y0)
            dy_que.append(dy)
            ts.append(t0)
        else:
            return np.array(ys).T, np.array(ts)

    while stopfunc(t0, y0):
        last_dy = f(t0, y0, *args)
        y0 = y0 + tau * ((1901 / 720) * last_dy - (1387 / 360) * dy_que[3] + (109 / 30) * dy_que[2] - (637 / 360) * dy_que[1] + (251 / 720) * dy_que[0])
        t0 += tau
        ys.append(y0)
        dy_que.append(last_dy)
        ts.append(t0)
    return np.array(ys).T, np.array(ts)

def runge_kutta4(f, y0, t0, t_end, tau, args, stopfunc=None):
    def rungeStep(f, t, y, tau, args):
        k1 = tau * f(t, y, *args)
        k2 = tau * f(t, y + k1 / 2, *args)
        k3 = tau * f(t, y + k2 / 2, *args)
        k4 = tau * f(t, y + k3, *args)
        increment = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        return y + increment

    if not stopfunc:
        stopfunc = lambda t, y: t <= t_end

    ys = [y0]
    ts = [t0]
    while stopfunc(t0, y0):
        y0 = rungeStep(f, t0, y0, tau, args)
        t0 += tau
        ys.append(y0)
        ts.append(t0)
    return np.array(ys).T, np.array(ts)


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

def psi(z, zk, kappa1, lambd1, mu1, kappa2, lambd2, mu2):
    if z < 1:
        return kappa1*z*(1 + lambd1*z + mu1*z**2)
    elif 1 <= z <= zk:
        z1 = z - 1
        psiS = kappa1 + kappa1*lambd1 + kappa1*mu1
        return psiS + kappa2*z1*(1 + lambd2*z1 +mu2*z1**2)
    else:
        return 1

def int_bal_rs(t, y, P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders):
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
    return f

def solve_ib(P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, l_d, powders, method = 'RK4', tmax = 1. , tstep = 1e-5):
    methods = {'AB5':adams_bashford5, 'RK4':runge_kutta4}
    y = np.zeros(2+len(powders))
    args = (P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)
    ys, ts = methods[method](int_bal_rs, y, 0., tmax, tstep, args, stopfunc=lambda t, y: y[1] < l_d)
    psis = np.zeros((len(powders), ys.shape[1]))
    for i, powd in enumerate(powders):
        psis[i, :] = np.array([psi(ys[2+i][k], *powd[7:]) for k in range(ys.shape[1])])

    lambda_khi = (ys[1] + l_k)/(ys[1] + l_ps)

    p_mean, p_sn, p_kn = np.zeros(ys.shape[1]), np.zeros(ys.shape[1]), np.zeros(ys.shape[1])

    for i in range(ys.T.shape[0]):
        p_mean[i], p_sn[i], p_kn[i] = P(ys.T[i], PV, lambda_khi[i], S, W0, qfi, omega_sum, psis.T[i], powders)

    ys[2:] = psis

    return ys, p_mean, p_sn, p_kn



