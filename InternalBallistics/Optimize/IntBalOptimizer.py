from Optimization.RandomOptimization.Optimizers import *
from Optimization.OptimizationErrors import *
from InternalBallistics.IntBalClasses import *
from InternalBallistics.ErrorClasses import NoOneCombo
from InternalBallistics.Optimize.TargetFucntions import max_speed_t_func
from itertools import combinations
from multiprocessing import Pool
import numpy as np
from copy import deepcopy

def check_eta_k(y, sol, params, eta_k_max):
    if sol[-1] != 0:
        res = sol[-1]/params.syst.l_d <= eta_k_max
        return res
    else:
        return False

def check_pmax(y, sol, params, pmax):
    return sol[1] <= pmax

def check_max_delta(x_cur, params, max_delta):
    return sum(powd.omega for powd in params.charge) <= max_delta*params.syst.W0

def adapt_proj_mass(x, params):
    params.syst.q = x[0]

def adapt_powders_mass(x, params):
    for xi, powd in zip(x[::2], params.charge):
        powd.omega = xi


def adapt_Jk(x, params):
    for xi, powd in zip(x[1::2], params.charge):
        powd.Jk = xi



class IntBalOptimizer(RandomScanOptimizer, RandomSearchOptimizer):
    methods = {
        'random_search': RandomSearchOptimizer.optimize,
        'random_scan': RandomScanOptimizer.optimize
    }
    KWARGS = {
        'random_search': {'N': 100, 'M': 50, 't0': 0.1, 'R': 1e-4},
        'random_scan': {'N': 400, 'max_modifier': 20}
    }

    combo_out_func = lambda combo: print(combo)

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
        self.set_second_ground_boundary()
        self.set_first_ground_boundary()
        self.set_target_func(max_speed_t_func)
        self.add_new_adapter('mass', adapt_powders_mass)
        self.add_new_adapter('Jk', adapt_Jk)

        if self.max_eta_k:
            self.second_ground_boundary['Eta_k'] = {'func': check_eta_k, 'lim': self.max_eta_k,
                                                    'fine': lambda x, y, solution, params: y*solution[4]}

    def set_second_ground_boundary(self):

        self.second_ground_boundary = {
            'Pmax': {'func': check_pmax, 'lim': self.Pmax}
        }

    def set_first_ground_boundary(self):

        self.first_ground_boundary = {
            'Delta_max': {'func': check_max_delta, 'lim': self.delta_max}
        }
    def set_combo_out_func(self, func):
        self.combo_out_func = func

    def _check_p_max(self):

        p_max_dict_func = {'func': check_pmax, 'lim': self.Pmax}
        return p_max_dict_func

    def optimize_with_Jk(self, method='random_search'):

        optimized_xvec, optimized_f, optimized_sol, summary = self.methods[method](self, **self.KWARGS[method])

        return optimized_xvec, optimized_f, optimized_sol, summary

    def get_powder_combination(self, Jk_dop_list, max_tol=15.):
        """
        Функция читающая базу порохов и по допустимым конечным импульсам(полученным в результате решения обобщенной задачи)
        возвращающая кортеж всех возможных комбинаций порохов
        :param Jk_dop_list: Итерируемый объект с допустимыми конечными импульсами(список/кортеж и тд.)
        :param max_tol: Максимальная ошибка по конечному импульсу
        :return: Кортеж всех возможных комбинаций порохов
        """

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

        unknowed = ('Сф_033', 'В_Уфл', 'ДРП', 'ВТ', 'ВТ_Д-25', 'МАП_23/1', 'СГ',
                    'Свинц._провол.', 'Инерт._добав.', 'Фл-тор')

        pirox = ('П125', 'П200', 'П200', 'ВТМ', 'ВТХ-10', 'ВТХ-20', '5/1', '4/1', '4/1_фл', '4/7', '4/7_Ц_гр', '5/7_св',
                 '5/7_н/а', '5/7_Ц_фл', '6/7_гр', '6/7_Бп_гр', '6/7_фл', '6/7_фл_ВБП', '6/7_П-5_БП_фл', '7/7', '7/14',
                 '5/1_Х-10', '7/1', '8/7', '8/1_уг', '9/7', '9/7_мн', '9/7_бп', '8/1_тр', '11/7', '12/7', '14/1_тр_в/а',
                 '14/7', '12/1_тр', '15/1_тр_в/а', '16/1_тр', '16/1_тр_в/а', '17/7', '18/1_тр', '22/7', 'УГ-1',
                 'УГФ_8/1', 'УГФ', '37/1_тр')

        ballistit = ('ДГ-314/1', 'НДТ-3_16/1', 'НДТ-3_18/1', 'ДГ-217/1', 'НДТ-3_19/1', 'ДГ-3_19/1', 'ДГ-3_20/1',
                     'НДТ-2_19/1', 'ДГ-3_23/1', 'НДТ-2_25/1', 'НДТ-3_32/1', 'НБ', 'АПЦ-235П_16Л')

        chemical_dict = {pirox: 'п', ballistit: 'б', unknowed: 'н'}

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
                else:
                    for key, val in chemical_dict.items():
                        if powder.name in key:
                            powder.chemical_group = val
                    powders_list.append(powder)

        # for powd in powders_list:
        #     try:
        #         print(powd.name, powd.chemical_group, sep='\t')
        #     except:
        #         print(powd.name)

        if not powders_list:
            raise NoOneCombo()

        elif len(powders_list) < len(Jk_dop_list):
            return tuple(map(list, combinations(powders_list, 1)))

        else:
            combo_charges = list(map(list, combinations(powders_list, len(Jk_dop_list))))
            if len(Jk_dop_list) == 1:
                return tuple(combo_charges)
            else:
                for combo in combo_charges[::-1]:
                    tmp = combinations(combo, 2)
                    check_list = [tmp_combo[0].chemical_group == tmp_combo[1].chemical_group for tmp_combo in tmp]
                    if not all(check_list):
                        combo_charges.remove(combo)

                one_powder_charge = list(map(list, combinations(powders_list, 1)))

                return tuple(combo_charges + one_powder_charge)

    def optimize_one_charge(self, omega_sum, charge, method):

        one_mass = 0.5 * omega_sum/len(charge)
        for powd in charge:
            powd.omega = one_mass #(self.delta_max * self.params.syst.W0)/(0.5*len(charge))

        self.params.charge = charge
        self.x_vec = np.array([powd.omega for powd in charge])
        self.x_lims = np.array([[0, np.inf] for powd in charge])
        xx, ff, ss, summary = self.methods[method](self, **self.KWARGS[method])

        self._adapt(xx)

        info_dict = {
            'combo': deepcopy(self.params.charge),
            'x_vec': xx,
            'sol': ss,
            'target_func': -ff,
            'summary': summary
        }


        return info_dict

    def get_optimized_powders_mass(self, optimized_xvec, method='random_search'):
        #self.out_func = None

        self._adapt(optimized_xvec)

        if "Jk" in self.adapters.keys():
            self.remove_adapter('Jk')

        self.x_lims = self.x_lims[::2]
        self.x_vec = self.x_vec[::2]
        omega_sum = sum(self.x_vec)

        Jk_dop_list = [powd.Jk for powd in self.params.charge]

        combos = self.get_powder_combination(Jk_dop_list)

        optimized_combos = []

        for combo in combos:
            try:
                info_dict = self.optimize_one_charge(omega_sum, combo, method)
                optimized_combos.append(info_dict)
            except FirstStepOptimizationFail as first_step_error:
                print(first_step_error)
            except MinStepOptimizerError as no_optimum:
                print(no_optimum)
            except:
                print('Хз че это было', combo, sep='\t')



        optimized_combos.sort(key=lambda info_dict: info_dict['target_func'], reverse=True)

        for combo in optimized_combos:
            print(combo)


        print('*'*40)
        print("Лучший вариант\n", max(optimized_combos, key=lambda info_dict: info_dict['target_func']))

        return optimized_combos

