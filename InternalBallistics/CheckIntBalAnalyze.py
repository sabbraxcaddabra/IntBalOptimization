from matplotlib import pyplot as plt
from IntBalClasses import ArtSystem, Powder, IntBalParams
from InternalBallistics.Analyze.SolveIntBal import solve_ib


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

    ts, ys, p_mean, p_sn, p_kn, l_k = solve_ib(*int_bal_cond.create_params_tuple(), method="RK4")
    print(ys[1][l_k])
    plt.plot(ys[1], p_mean*1e-6)
    plt.scatter(ys[1][l_k], p_mean[l_k]*1e-6, label='Окончание горения')
    plt.show()