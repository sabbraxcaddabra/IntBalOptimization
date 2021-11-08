import numpy as np
from numba import njit
from collections import deque
import matplotlib.pyplot as plt
from InternalBallistics.ErrorClasses import *


def adams_bashford5(f, y0, t0, t_end, tau, args, stopfunc=None, eventfunc=None):
    def runge_step(f, t, y, tau, args):
        k1 = tau * f(t, y, *args)
        k2 = tau * f(t + (1 / 4) * tau, y + (1 / 4) * k1, *args)
        k3 = tau * f(t + (3 / 8) * tau, y + (3 / 32) * k1 + (9 / 32) * k2, *args)
        k4 = tau * f(t + (12 / 13) * tau, y + (1932 / 2197) * k1 - (7200 / 2197) * k2 + (7296 / 2197) * k3, *args)
        k5 = tau * f(t + tau, y + (439 / 216) * k1 - 8 * k2 + (3680 / 513) * k3 - (845 / 4104) * k4, *args)
        k6 = tau * f(t + (1 / 2) * tau,
                     y - (8 / 27) * k1 + 2 * k2 - (3544 / 2565) * k3 + (1859 / 4104) * k4 - (11 / 40) * k5, *args)
        increment = (16 / 135) * k1 + (6656 / 12825) * k3 + (28561 / 56430) * k4 - (9 / 50) * k5 + (2 / 55) * k6
        return y+increment, k1

    if not stopfunc:
        stopfunc = lambda t, y: t <= t_end
    if not eventfunc:
        eventfunc = lambda t, y: False

    dy_que = deque(maxlen = 4)
    event_indices = []
    ys = [y0]
    ts = [t0]
    for _ in range(4):
        y0, dy = runge_step(f, t0, y0, tau, args)
        t0 += tau
        if stopfunc(t0, y0) and t0 < t_end:
            ys.append(y0)
            dy_que.append(dy)
            ts.append(t0)
            if eventfunc(t0, y0):
                event_indices.append(len(ts)-1)
        else:
            return np.array(ys).T, np.array(ts)

    while stopfunc(t0, y0) and t0 < t_end:
        last_dy = f(t0, y0, *args)
        y0 = y0 + tau * ((1901 / 720) * last_dy - (1387 / 360) * dy_que[3] + (109 / 30) * dy_que[2] - (637 / 360) * dy_que[1] + (251 / 720) * dy_que[0])
        t0 += tau
        ys.append(y0)
        dy_que.append(last_dy)
        ts.append(t0)
        if eventfunc(t0, y0):
            event_indices.append(len(ts) - 1)

    return np.array(ys).T, np.array(ts), event_indices



def runge_kutta4(f, y0, t0, t_end, tau, args, stopfunc=None, eventfunc=None):
    def rungeStep(f, t, y, tau, args):
        k1 = tau * f(t, y, *args)
        k2 = tau * f(t, y + k1 / 2, *args)
        k3 = tau * f(t, y + k2 / 2, *args)
        k4 = tau * f(t, y + k3, *args)
        increment = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        return y + increment

    if not stopfunc:
        stopfunc = lambda t, y: t <= t_end

    if not eventfunc:
        eventfunc = lambda t, y: False

    event_indices = []

    ys = [y0]
    ts = [t0]
    while stopfunc(t0, y0) and t0 < t_end:
        y0 = rungeStep(f, t0, y0, tau, args)
        t0 += tau
        ys.append(y0)
        ts.append(t0)
        if eventfunc(t0, y0):
            event_indices.append(len(ts) - 1)

    return np.array(ys).T, np.array(ts), event_indices

def P(y, Pv, lambda_khi, S, W0, qfi, omega_sum, psis, powders):
    thet = theta(psis, powders)
    fs = 0.
    for i, powder in enumerate(powders):
        f = powder[2]
        om = powder[0]
        delta = powder[1]
        alpha = powder[5]
        fs += f*om*psis[i]
        W0 -= om*((1.-psis[i])/delta + psis[i]*alpha)
    fs -= thet * y[0]**2 * (qfi/2 + lambda_khi * omega_sum / 6.)
    W0 += y[1] * S
    if W0 < 0.:
        raise TooMuchPowderError()
    p_mean = Pv + fs/W0
    p_sn = (p_mean/(1 + (1/3) * (lambda_khi*omega_sum)/qfi))*(y[0] > 0.) + (y[0] == 0.)*p_mean
    p_kn = (p_sn*(1 + 0.5*lambda_khi*omega_sum/qfi))*(y[0] > 0.) + (y[0] == 0.)*p_mean

    return p_mean, p_sn, p_kn

def theta(psis, powders):
    sum1 = 0
    sum2 = 0
    for i, powder in enumerate(powders):
        sum1 += powder[2] * powder[0] * psis[i] / powder[3]
        sum2 += powder[2] * powder[0] * psis[i] / (powder[3] * powder[6])
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
    for i, powder in enumerate(powders):
        psis[i] = psi(y[2 + i], *powder[7:])
    lambda_khi = (y[1] + l_k)/(y[1] + l_ps)

    p_mean, p_sn, p_kn = P(y, PV, lambda_khi, S, W0, qfi, omega_sum, psis, powders)
    if y[0] == 0. and p_mean < P0:
        f[0] = 0
        f[1] = 0
    else:
        f[0] = (p_sn*S)/(qfi)
        f[1] = y[0]
    for i, powder in enumerate(powders):
        if p_mean <= 50e6:
            f[2+i] = ((k50*p_mean**0.75)/powder[4]) * (y[2+i] < powder[7])
        else:
            f[2+i] = (p_mean/powder[4]) * (y[2+i] < powder[7])
    return f

def solve_ib(P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, l_d, powders, method = 'RK4', tmax = 1. , tstep = 1e-5):
    methods = {'AB5':adams_bashford5, 'RK4':runge_kutta4}

    y = np.zeros(2+len(powders))
    zk_list = np.array([powders[i][7] for i in range(len(powders))])
    args = (P0, PV, k50, S, W0, l_k, l_ps, omega_sum, qfi, powders)
    ys, ts, events = methods[method](int_bal_rs, y, 0., tmax, tstep, args, stopfunc=lambda t, y: y[1] < l_d,
                             eventfunc=lambda t, y:np.all(zk_list <= y[2:]))
    if events:
        lk_index = events[0]
    else:
        lk_index = 0

    if ts[-1] > tmax:
        raise TooMuchTime()

    psis = np.zeros((len(powders), ys.shape[1]))

    for i, powd in enumerate(powders):
        psis[i, :] = np.array([psi(ys[2+i][k], *powd[7:]) for k in range(ys.shape[1])])

    lambda_khi = (ys[1] + l_k)/(ys[1] + l_ps)

    p_mean, p_sn, p_kn = np.zeros(ys.shape[1]), np.zeros(ys.shape[1]), np.zeros(ys.shape[1])

    for i in range(ys.T.shape[0]):
        p_mean[i], p_sn[i], p_kn[i] = P(ys.T[i], PV, lambda_khi[i], S, W0, qfi, omega_sum, psis.T[i], powders)

    ys[2:] = psis

    return ts, ys, p_mean, p_sn, p_kn, lk_index



