from Optimization.RandomOptimization.Optimizers import *
from InternalBallistics.IntBalClasses import *
from InternalBallistics.ErrorClasses import NoOneCombo
from itertools import combinations
from multiprocessing import Pool
import numpy as np
from benchmark import benchmark
from copy import deepcopy

def check_eta_k(sol, params, eta_k_max):
    return sol[-1]/params.syst.l_d <= eta_k_max

def check_pmax(sol, params, pmax):
    return sol[0] <= pmax

def check_max_delta(x_cur, params, max_delta):
    return sum(powd.omega for powd in params.charge) <= max_delta*params.syst.W0

def adapt_proj_mass(x, params):
    params.syst.q = x[0]

def adapt_powders_mass(x, params):
    if len(x) != 1:
        check1 = len(x)%2
        check2 = (len(x)-check1)//len(params.charge)
        for xi, powd in zip(x[check1::check2], params.charge):
            powd.omega = xi
    else:
        params.charge[0].omega = x[0]

def adapt_Jk(x, params):
    if len(x) != 1:
        check1 = len(x)%2
        check2 = (len(x) - check1) // len(params.charge)
        for xi, powd in zip(x[check1:][check2-1::check2], params.charge):
            powd.Jk = xi
    else:
        params.charge[0].Jk = x[0]



class IntBalOptimizer(RandomScanOptimizer, RandomSearchOptimizer):
    methods = {
        'random_search': RandomSearchOptimizer.optimize,
        'random_scan': RandomScanOptimizer.optimize
    }

    def __init__(self,
                 x_vec,
                 params=None,
                 adapters=dict(),
                 first_ground_boundary=dict(),
                 second_ground_boundary=dict(),
                 x_lims=None,
                 t_func=None,
                 out_func=None, Pmax=None, delta_max=None, max_eta_k=None):

        super().__init__(x_vec, params, adapters, first_ground_boundary,
                 second_ground_boundary, x_lims, t_func, out_func)

        self.Pmax = Pmax
        self.delta_max = delta_max
        self.max_eta_k = max_eta_k
        self.add_second_ground_boundary('Pmax', self._check_p_max())
        self.add_new_adapter('mass', adapt_powders_mass)
        self.add_new_adapter('Jk', adapt_Jk)

    def _check_p_max(self):

        p_max_dict_func = {'func': check_pmax, 'lim': self.Pmax}
        return p_max_dict_func

    def optimize_with_Jk(self, method='random_search', **kwargs):

        self.optimized_xvec = self.methods[method](self, **kwargs)[0]

    def get_powder_combination(self, Jk_dop_list, max_tol=15.):
        """
        Функция читающая базу порохов и по допустимым конечным импульсам(полученным в результате решения обобщенной задачи)
        возвращающая кортеж всех возможных комбинаций порохов
        :param Jk_dop_list: Итерируемый объект с допустимыми конечными импульсами(список/кортеж и тд.)
        :param max_tol: Максимальная ошибка по конечному импульсу
        :return: Кортеж всех возможных комбинаций порохов
        """

        def check_Jk(powder, Jk_dop, max_tol):
            tol = abs((powder.Jk / Jk_dop) * 100 - 100)
            if tol <= max_tol:
                return True

        with open('PowdersBase.txt', encoding='utf8') as base_file:
            non_powder = (
                'Фл-тор',
                'Инерт._добав.',
                'Свинц._провол.'
            )
            powders_list = []
            for line in base_file:
                powder = Powder.from_data_string(line)
                powder_check_list = [check_Jk(powder, Jk_dop, max_tol) for Jk_dop in Jk_dop_list]
                if powder.name in non_powder or not any(powder_check_list):
                    continue
                powders_list.append(powder)

        if len(powders_list) < len(Jk_dop_list):
            raise NoOneCombo()
        else:
            comb_powders = tuple(map(list, combinations(powders_list, len(Jk_dop_list))))
            return comb_powders

    def optimize_one_charge(self, charge, method, **kwargs):

        for powd in charge:
            powd.omega = (self.delta_max * self.params.syst.W0)/len(charge)

        self.params.charge = charge
        self.x_vec = np.array([powd.omega for powd in charge])
        xx, ff = self.methods[method](self, **kwargs)

        self._adapt(xx)

        info_dict = {
            'combo': deepcopy(self.params.charge),
            'x_vec': xx,
            'target_func': ff
        }


        return info_dict

    def get_optimized_powders_mass(self, method='random_search', **kwargs):

        self._adapt(self.optimized_xvec)

        if "Jk" in self.adapters.keys():
            self.remove_adapter('Jk')

        self.x_lims = self.x_lims[::2]

        Jk_dop_list = [powd.Jk for powd in self.params.charge]

        combos = self.get_powder_combination(Jk_dop_list)
        optimized_combos = []

        # with Pool(3) as p:
        #     res = p.map(self.optimize_one_charge, combos)

        for combo in combos:
            info_dict = self.optimize_one_charge(combo, method, **kwargs)
            optimized_combos.append(info_dict)

        optimized_combos.sort(key=lambda info_dict: info_dict['target_func'], reverse=True)

        for combo in optimized_combos:
            print(combo)

        print('*'*40)
        print("Лучший вариант\n", min(optimized_combos, key=lambda info_dict: info_dict['target_func']))