from .SolveIntBal import solve_ib
from .SolveIntBal import solve_ib_ab5

def max_speed_t_func(x_vec, params):
    y, p_mean_max, p_sn_max, p_kn_max, psi_sum, eta_k = solve_ib(*params.create_params_tuple())
    return -y[0], (p_mean_max, p_sn_max, p_kn_max, psi_sum, eta_k)



def max_speed_t_func_with_fine(x_vec, params):
    y, p_mean_max, p_sn_max, p_kn_max, lk = solve_ib(*params.create_params_tuple())
    fine = sum(y[2+i] * params.charge[i].omega for i in range(len(params.charge)))/sum(params.charge[i].omega for i in range(len(params.charge)))
    return -y[0]*fine, (p_mean_max, p_sn_max, p_kn_max, lk/params.syst.l_d)

