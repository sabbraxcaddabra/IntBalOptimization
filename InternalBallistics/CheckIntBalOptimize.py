from IntBalClasses import ArtSystem, Powder, IntBalParams
from Optimize.SolveIntBal import solve_ib, TooMuchPowderError
from benchmark import benchmark
from collections import namedtuple


if __name__ == '__main__':
    artsys = ArtSystem(name='2А42', d=.03, S=0.000735299, q=0.389, W0=0.125E-3, l_d=2.263, l_k=0.12,
                       l0=0.125E-3 / 0.000735299, Kf=1.136)

    int_bal_cond = IntBalParams(syst=artsys, P0=50e6, PV=4e6)
    int_bal_cond.add_powder(
        Powder(name='6/7', omega=0.07, rho=1.6e3, f_powd=988e3, Ti=2800., Jk=343.8e3, alpha=1.038e-3, teta=0.236,
               Zk=1.53, kappa1=0.239, lambd1=2.26, mu1=0., kappa2=0.835, lambd2=-0.943, mu2=0.))
    int_bal_cond.add_powder(
        Powder(name='6/7', omega=0.03, rho=1.6e3, f_powd=988e3, Ti=2800., Jk=343.8e3, alpha=1.038e-3, teta=0.236,
               Zk=1.53, kappa1=0.239, lambd1=2.26, mu1=0., kappa2=0.835, lambd2=-0.943, mu2=0.))
    int_bal_cond.add_powder(
        Powder(name='6/7', omega=0.02, rho=1.6e3, f_powd=988e3, Ti=2800., Jk=343.8e3, alpha=1.038e-3, teta=0.236,
               Zk=1.53, kappa1=0.239, lambd1=2.26, mu1=0., kappa2=0.835, lambd2=-0.943, mu2=0.))


    y, p_mean_max, p_sn_max, p_kn_max, lk = solve_ib(*int_bal_cond.create_params_tuple())

    print("Печать результатов рачета\n")
    print(f"Дульная скорость: {round(y[0], 1)} м/с")
    print(f"Максимальное среднебаллистическое давление: {round(p_mean_max * 1e-6, 2)} МПа")
    print(f"Максимальное давление на дно снаряда: {round(p_sn_max * 1e-6, 2)} МПа")
    print(f"Максимальное давление на дно канала ствола: {round(p_kn_max * 1e-6, 2)} МПа")
    print(f"Координата полного сгорания порохового заряда {round(lk, 4)} м")

    # try:
    #     solve_ib = benchmark()(solve_ib)
    #     y, p_mean_max, p_sn_max, p_kn_max, lk = solve_ib(*int_bal_cond.create_params_tuple())

    #     print("Печать результатов рачета\n")
    #     print(f"Дульная скорость: {round(y[0], 1)} м/с")
    #     print(f"Максимальное среднебаллистическое давление: {round(p_mean_max * 1e-6, 2)} МПа")
    #     print(f"Максимальное давление на дно снаряда: {round(p_sn_max * 1e-6, 2)} МПа")
    #     print(f"Максимальное давление на дно канала ствола: {round(p_kn_max * 1e-6, 2)} МПа")
    #     print(f"Координата полного сгорания порохового заряда {round(lk, 4)} м")

    # except TooMuchPowderError:
    #     print("слишком много пороха")
    
    