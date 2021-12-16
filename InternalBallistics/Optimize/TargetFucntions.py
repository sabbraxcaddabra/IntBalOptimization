from .SolveIntBal import solve_ib
from .SolveIntBal import solve_ib_ab5

def max_speed_t_func(x_vec, params):
    y, p_mean_max, p_sn_max, p_kn_max, psi_sum, eta_k = solve_ib(*params.create_params_tuple())
    return -y[0], (p_mean_max, p_sn_max, p_kn_max, psi_sum, eta_k)

