from abc import ABC, abstractmethod
import numpy as np
from numpy.random import uniform
from numpy.linalg import norm

from Optimization.OptimizationErrors import *

__all__ = ['RandomScanOptimizer', 'RandomSearchOptimizer']

# TODO: Добавить методы для удаления ограничений 1-го и 2-го рода по ключу
# TODO: Проверить качество и правильность реализации метода случайного сканирования
# TODO: Добавить еще несколько реализацций алгоритмов оптимизации
# TODO: Написать нормальную документацию для каждого класса



class Optimizer(ABC):
    """
    Абстрактный класс-оптимайзер.
    Конкретные реализации алгоритмов оптимизации должны наследоваться от данного класса
    """
    possible_errors = [LimitExeedErroor, FirstGroundBoundaryError, SecondGroundBoundaryError]
    def __init__(self,
                 x_vec,
                 params=None,
                 adapters=dict(),
                 first_ground_boundary=dict(),
                 second_ground_boundary=dict(),
                 x_lims=None,
                 t_func=None,
                 out_func=None):
        self.x_vec = x_vec
        self.params = params
        self.adapters = adapters
        self.first_ground_boundary = first_ground_boundary
        self.second_ground_boundary = second_ground_boundary
        self.x_lims = x_lims
        self.t_func = t_func
        self.out_func = out_func

    def add_new_adapter(self, key, adapt_func) -> None:
        """
        Метод для добавления в задачу нового адаптера
        :param adapt_func: Функция, лямбда-функция, классовый метод и т.д(callable объект)
        :return: None
        """
        self.adapters[key] = adapt_func

    def _adapt(self, x_vec_new: list) -> None:
        """
        Метод адаптирует параметры задачи(подставляет значения x_vec_new в необходимые поля params для решения
        целевой функции
        :param x_vec_new: Новый вектор варьируемых параметров X
        :return: None
        """
        if self.adapters:
            for func in self.adapters.values():
                func(x_vec_new, self.params)

    def remove_adapter(self, key):

        del self.adapters[key]

    def add_first_ground_boundary(self, name: str, func_dict: dict) -> None:
        """
        Метод для добавления функций - ограничений первого рода
        :param name: Название ограничения первого рода(оптимизатором не используется, необходимо для удобства
        пользователя и возможности проще удалить при необходимости)
        :param func_dict: Словарь с ключами func и lims, где func соответсвтует функция, лямбда и тд,
        которая принимат в себе параметры задачи и сравнивает необходимые поля параметров или их преобразования с lims
        :return: None
        """
        self.first_ground_boundary[name] = func_dict

    def _check_first_ground_boundary(self, x_vec_cur):
        """
        Проверка ограничений 1-го рода. Если словарь ограничений пуст, проверяется только вхождение каждой компоненты
        x_vec_cur в ограничения заданные x_lims
        :param x_vec_cur: Текущая реализация вектора варьируемых параметров
        :return: bool
        """
        if self.first_ground_boundary:
            for func_dict_name, func_dict in self.first_ground_boundary.items():
                res = func_dict['func'](x_vec_cur, self.params, func_dict['lim'])
                if not res:
                    func_dict['errors'] += 1
                    raise FirstGroundBoundaryError(func_dict_name)

        if len(self.x_lims) != len(x_vec_cur):
            raise Exception("Длина вектора варьируемых параметров не совпадает с длиной вектора ограничений")
        else:
            check_list = [lim[0] <= x <= lim[1] for lim, x in zip(self.x_lims, x_vec_cur)]
            if not all(check_list):
                raise LimitExeedErroor(x_vec_cur, self.x_lims)


    def add_second_ground_boundary(self, name: str, func_dict: dict) -> None:
        """
        Добавление функций-ограничений второго рода
        :param name: Название ограничения первого рода(оптимизатором не используется, необходимо
        для удобства пользователяи возможности проще удалить при необходимости)
        :param func_dict: Словарь с ключами func и lims, где func соответсвтует функция,
        лямбда и тд, которая принимат в себея параметры
        задачи и решение целевой функции и сравнивает необходимые поля решения с lims
        :return: None
        """
        self.second_ground_boundary[name] = func_dict

    def _check_second_ground_boundary(self, x, y, solution, params):
        """
        Проверка ограничений 2-го рода
        :param solution: Текущий результат решения целевой функции
        :return: bool
        """

        if self.second_ground_boundary:
            for func_dict_name, func_dict in self.second_ground_boundary.items():
                res = func_dict['func'](y, solution, self.params, func_dict['lim'])
                if not res:
                    fine_func = func_dict.get('fine')
                    if fine_func:
                        y = fine_func(x, y, solution, params)
                        func_dict['fines'] += 1
                    else:
                        func_dict['errors'] += 1
                        raise SecondGroundBoundaryError(func_dict_name)
        return y

    def set_target_func(self, t_func) -> None:
        """
        Установка целевой функции
        :param t_func: Целевая функция(callable)
        :return:
        """
        self.t_func = t_func

    def set_out_func(self, o_func):
        self.out_func = o_func

    def clearify_errors(self):
        '''
        Зануление счетчиков ошибок для ограничений 1 и 2 рода
        :return:
        '''
        if self.second_ground_boundary:
            for func_dict in self.second_ground_boundary.values():
                func_dict['errors'] = 0
                func_dict['fines'] = 0

        if self.first_ground_boundary:
            for func_dict in self.first_ground_boundary.values():
                func_dict['errors'] = 0

    def get_optimization_summary(self, above_limits, target_func_calculated):
        summary = {'t_func_calcs': target_func_calculated, 'first_ground': dict(), 'above_limits': above_limits, 'second_ground': dict()}

        if self.second_ground_boundary:
            for func_key, func_value in self.second_ground_boundary.items():
                summary['second_ground'][func_key] = {'errors': func_value['errors']}
                summary['second_ground'][func_key]['fines'] = func_value['fines']

        if self.first_ground_boundary:
            for func_key, func_value in self.first_ground_boundary.items():
                summary['first_ground'][func_key] = {'errors': func_value['errors']}

        return summary


    @abstractmethod
    def optimize(self):
        pass

class RandomScanOptimizer(Optimizer):
    """
    Класс-наследник оптимизатора
    Реализация алгоритма случайного сканирования
    """

    def _jump(self, x, i):
        """
        Расчет следующего приближения x
        :param x: Вектор варьируемых параметров
        :param i: Модификатор шага
        :return: Новое приближение x
        """
        ai = np.array([(lim[0] + lim[1]) / 2 for lim in self.x_lims])
        bi = np.array([abs(lim[0] - lim[1]) / 2 for lim in self.x_lims])
        x = ai + bi * uniform(-1. / i, 1. / i, len(x))
        return x

    def optimize(self, N=50, max_modifier=8, min_delta_f=0.):
        """
        Реализация алгоритма оптимизации
        :param N: Максимальное число неудачных шагов
        :param max_modifier: Максимальный модификатор щага
        :param min_delta_f: Минимальное уменьшение целевой функции
        :return: last_x Оптимальное значение вектора x_vec
        """
        try:
            last_x = self.x_vec[:]
            self._adapt(last_x)
            last_f, last_sol = self.t_func(last_x, self.params)
            last_f = self._check_second_ground_boundary(last_x, last_f, last_sol, self.params)
        except SecondGroundBoundaryError:
            pass

        except:
            raise FirstStepOptimizationFail()

        bad_steps_cur = 0  # Счетчик неудачных шагов
        cur_step_modifier = 1

        while bad_steps_cur < N and cur_step_modifier <= max_modifier:
            xx = self._jump(last_x, cur_step_modifier)
            self._adapt(xx)
            if self._check_first_ground_boundary(xx):
                try:
                    cur_f, cur_solution = self.t_func(xx, self.params)
                    if self._check_second_ground_boundary(cur_solution):
                        if cur_f <= last_f and abs(cur_f - last_f) > min_delta_f:
                            last_f, last_x, last_sol = cur_f, xx[:], cur_solution
                            if self.out_func:
                                self.out_func(xx, cur_f, cur_solution, self.params)
                            bad_steps_cur = 0
                        else:
                            bad_steps_cur += 1
                    else:
                        bad_steps_cur += 1
                except:
                    bad_steps_cur += 1
            else:
                bad_steps_cur += 1

            if bad_steps_cur == N and cur_step_modifier < max_modifier:
                bad_steps_cur = 0
                cur_step_modifier += 1

        if not np.array_equal(last_x, self.x_vec):
            return last_x, last_f, last_sol
        else:
            raise MinStepOptimizerError()

class RandomSearchOptimizer(Optimizer):

    @staticmethod
    def _get_yj(x_cur, tk):
        """

        :param x_cur:
        :param tk:
        :return:
        """
        ksi = uniform(-1, 1, len(x_cur))
        yj = x_cur + tk * ksi / norm(ksi)
        return yj

    @staticmethod
    def _get_zj(x_cur, alpha, yj):
        """

        :param x_cur:
        :param alpha:
        :param yj:
        :return:
        """
        zj = x_cur + alpha * (yj - x_cur)
        return zj

    # @benchmark(iters=10)#, file_to_write="opt_benc_200_jited.txt", make_graphics=True)
    def optimize(self, N=100, M=10, t0=1., R=0.1, alpha=1.618, beta=0.618, min_delta_f=0.):
        """

        :param N:
        :param M:
        :param t0:
        :param R:
        :param alpha:
        :param beta:
        :return:
        """
        self.clearify_errors()

        above_limits = 0
        target_func_calculated = 0


        steps_total = 0
        bad_steps_cur = 1

        try:
            last_x = np.ones(len(self.x_vec))
            self._adapt(last_x*self.x_vec)
            self._check_first_ground_boundary(last_x*self.x_vec)
            last_f, last_sol = self.t_func(last_x*self.x_vec, self.params)
            last_f = self._check_second_ground_boundary(last_x*self.x_vec, last_f, last_sol, self.params)

        except LimitExeedErroor as raised_error:

            new_rised_error = FirstStepOptimizationFail(error=raised_error)
            raise new_rised_error

        except FirstGroundBoundaryError as raised_error:

            new_rised_error = FirstStepOptimizationFail(error=raised_error)
            raise new_rised_error

        except SecondGroundBoundaryError as raised_error:
            info_dict = {
                'x_vec': last_x*self.x_vec,
                'sol': last_sol,
                'target_func': last_f,
            }
            if self.out_func:
                out_func_message = self.out_func(last_x*self.x_vec, last_f, last_sol, self.params)
                new_raised_error = FirstStepOptimizationFail(error=raised_error, t_func_info=info_dict,
                                                             out_message=out_func_message)
            else:
                new_raised_error = FirstStepOptimizationFail(error=raised_error, t_func_info=info_dict)

            raise new_raised_error

        except BaseException as raised_error:
            raise FirstStepOptimizationFail(error=raised_error)



        while steps_total < N:
            while bad_steps_cur < M:
                yj = self.x_vec * self._get_yj(last_x, t0)
                self._adapt(yj)
                try:
                    self._check_first_ground_boundary(yj) # Проверка ограничений первого рода
                    cur_f, cur_solution = self.t_func(yj, self.params) # Вычисление ЦФ
                    target_func_calculated += 1
                    cur_f = self._check_second_ground_boundary(yj, cur_f, cur_solution, self.params) # Проверка ограничений второго рода
                    if cur_f <= last_f and abs(cur_f - last_f) > min_delta_f:
                        zj = self.x_vec * self._get_zj(last_x, alpha, yj/self.x_vec)
                        self._adapt(zj)
                        self._check_first_ground_boundary(zj) # Проверка ограничений первого рода
                        cur_f, cur_solution = self.t_func(zj, self.params) # Вычисление ЦФ
                        target_func_calculated += 1
                        cur_f = self._check_second_ground_boundary(zj, cur_f, cur_solution, self.params) # Проверка ограничений второго рода
                        if cur_f <= last_f and abs(cur_f - last_f) > min_delta_f:
                            last_x, last_f, last_sol = zj/self.x_vec, cur_f, cur_solution
                            t0 *= alpha
                            steps_total += 1
                            if self.out_func:
                                self.out_func(zj, cur_f, cur_solution, self.params)
                            break
                        else:
                            bad_steps_cur += 1
                    else:
                        bad_steps_cur += 1
                except LimitExeedErroor:
                    above_limits += 1
                except:
                    bad_steps_cur += 1

            if t0 <= R:
                if not np.array_equal(last_x, np.ones(len(self.x_vec))):
                    #print(f"Оптимизация завершилась успешно, шаг минимальный {t0=}")
                    summary = self.get_optimization_summary(above_limits, target_func_calculated)
                    return last_x * self.x_vec, last_f, last_sol, summary
                else:
                    summary = self.get_optimization_summary(above_limits, target_func_calculated)
                    raise MinStepOptimizerError(summary)
            else:
                t0 *= beta
                bad_steps_cur = 1

        if not np.array_equal(last_x, np.ones(len(self.x_vec))):
            #print("Оптимизация завершилась успешно, израсходованно максимальное число итераций")
            summary = self.get_optimization_summary(above_limits, target_func_calculated)
            return last_x * self.x_vec, last_f, last_sol, summary
        else:
            summary = self.get_optimization_summary(above_limits, target_func_calculated)
            raise TooMuchItersOptimizerError(summary)