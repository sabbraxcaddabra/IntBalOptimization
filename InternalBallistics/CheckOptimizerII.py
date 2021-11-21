from InternalBallistics.IntBalClasses import ArtSystem, Powder, IntBalParams
from InternalBallistics.Optimize.TargetFucntions import max_speed_t_func
from Optimization.RandomOptimization.Optimizers import RandomSearchOptimizer
from InternalBallistics.Optimize.IntBalOptimizer import IntBalOptimizer
import numpy as np

def out_bal_func(x_vec, f, sol, params):
    print(f"Масса снаряда: {params.syst.q = } кг")
    for powd in params.charge:
        print(f"Масса пороха {powd.name}: {round(powd.omega, 4)} кг")
        print(f"Конечный импульс пороха {powd.name}: {round(powd.Jk, 2)} Па*с")
    print(f"Дульная скорость: {-round(f, 1)} м/с")
    print(f"Максимальное среднебаллистическое давление: {round(sol[0] * 1e-6, 2)} МПа")
    print(f"Максимальное давление на дно снаряда: {round(sol[1] * 1e-6, 2)} МПа")
    print(f"Максимальное давление на дно канала ствола: {round(sol[2] * 1e-6, 2)} МПа")
    print(f"Координата полного сгорания порохового заряда {round(sol[3], 4)} м")
    print("*" * 30 + '\n')

if __name__ == "__main__":
    artsys = ArtSystem(name='2А42', S=0.000735299, d=.03, q=0.389, W0=0.125E-3, l_d=2.263, l_k=0.12, l0=0.125E-3 / 0.000735299, Kf=1.136)

    int_bal_cond = IntBalParams(syst=artsys, P0=50e6, PV=4e6)

    int_bal_cond.add_powder(
        Powder(name='6/7', omega=0.07, rho=1.6e3, f_powd=988e3, Ti=2800., Jk=343.8e3, alpha=1.038e-3, teta=0.236,
               Zk=1.53, kappa1=0.239, lambd1=2.26, mu1=0., kappa2=0.835, lambd2=-0.943, mu2=0.))

    # int_bal_cond.add_powder(
    #     Powder(name='6/7', omega=0.05, rho=1.6e3, f_powd=988e3, Ti=2800., Jk=343.8e3, alpha=1.038e-3, teta=0.236,
    #            Zk=1.53, kappa1=0.239, lambd1=2.26, mu1=0., kappa2=0.835, lambd2=-0.943, mu2=0.))

    x_vec = np.array([0.07, 343.8e3, 0.05, 343.8e3])
    weights = [0.1, 0.7, 0.1, 0.7]
    xlims = [[-np.inf, np.inf] for nom, weight in zip(x_vec, weights)]
    opt = IntBalOptimizer(x_vec,
                                params=int_bal_cond,
                                x_lims=xlims, Pmax=500e6)

    opt.set_target_func(max_speed_t_func)
    opt.optimize_with_Jk(N=100, M=50, t0=0.1, R=1e-4)
    opt.get_optimized_powders_mass(N=100, M=50, t0=0.1, R=1e-4)