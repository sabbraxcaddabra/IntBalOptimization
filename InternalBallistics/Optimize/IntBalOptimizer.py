from Optimization.RandomOptimization.Optimizers import *


def adapt_proj_mass(x, params):
    params.syst.q = x[0]

def adapt_powders_mass(x, params):
    check1 = len(x)%2
    check2 = (len(x)-check1)//len(params.charge)
    for xi, powd in zip(x[check1::check2], params.charge):
        powd.omega = xi

def adapt_Jk(x, params):
    check1 = len(x)%2
    check2 = (len(x) - check1) // len(params.charge)
    for xi, powd in zip(x[check1:][check2-1::check2], params.charge):
        powd.Jk = xi

class IntBalOptimizer(RandomScanOptimizer, RandomSearchOptimizer):
    methods = {
        'random_search': RandomSearchOptimizer.optimize,
        'random_scan': RandomScanOptimizer.optimize
    }

    def __init__(self,
                 x_vec,
                 params=None,
                 adapters=[],
                 first_ground_boundary=dict(),
                 second_ground_boundary=dict(),
                 x_lims=None,
                 t_func=None,
                 out_func=None, Pmax=None, delta_max=None):

        super().__init__(x_vec, params, adapters, first_ground_boundary,
                 second_ground_boundary, x_lims, t_func, out_func)

        self.Pmax = Pmax
        self.delta_max = delta_max
        self.add_second_ground_boundary('Pmax', self._check_p_max())
        self.add_new_adapter(adapt_powders_mass)
        self.add_new_adapter(adapt_Jk)

    def _check_p_max(self):

        p_max_dict_func = {'func': lambda sol, params, lim: sol[0] < lim, 'lim': self.Pmax}
        return p_max_dict_func

    def optimize(self, method='random_search', **kwargs):

        self.optimized_xvec = self.methods[method](self, **kwargs)