from abc import ABC, abstractmethod
import numpy as np
from numpy.random import uniform
from numpy.linalg import norm

# TODO: Добавить методы для удаления ограничений 1-го и 2-го рода по ключу
# TODO: Проверить качество и правильность реализации метода случайного сканирования
# TODO: Добавить еще несколько реализацций алгоритмов оптимизации
# TODO: Написать нормальную документацию для каждого класса

class TooMuchItersOptimizerError(Exception):
    def __str__(self):
        return "Не найдено ни одного оптимума. Израсходовано максимальное число итераций\n" \
               "Попробуйте меньший шаг или большее максимальное число итераций"

class MinStepOptimizerError(Exception):
    def __str__(self):
        return "Не найдено ни одного оптимума. Достигнут минимальный шаг\n" \
               "Попробуйте меньший шаг или большее максимальное число итераций"

class Optimizer(ABC):
    """
    Абстрактный класс-оптимайзер.
    Конкретные реализации алгоритмов оптимизации должны наследоваться от данного класса
    """

    def __init__(self,
                 x_vec,
                 params=None,
                 adapters=[],
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

    def add_new_adapter(self, adapt_func) -> None:
        """
        Метод для добавления в задачу нового адаптера
        :param adapt_func: Функция, лямбда-функция, классовый метод и т.д(callable объект)
        :return: None
        """
        self.adapters.append(adapt_func)

    def _adapt(self, x_vec_new: list) -> None:
        """
        Метод адаптирует параметры задачи(подставляет значения x_vec_new в необходимые поля params для решения
        целевой функции
        :param x_vec_new: Новый вектор варьируемых параметров X
        :return: None
        """
        if self.adapters:
            for func in self.adapters:
                func(x_vec_new, self.params)

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
            check_list = [func_dict['func'](x_vec_cur, self.params, func_dict['lims']) for func_dict in
                          self.first_ground_boundary]
        else:
            if len(self.x_lims) != len(x_vec_cur):
                raise Exception("Длина вектора варьируемых параметров не совпадает с длиной вектора ограничений")
            else:
                check_list = [lim[0] <= x <= lim[1] for lim, x in zip(self.x_lims, x_vec_cur)]
        return all(check_list)

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

    def _check_second_ground_boundary(self, solution):
        """
        Проверка ограничений 2-го рода
        :param solution: Текущий результат решения целевой функции
        :return: bool
        """
        check_list = []
        if self.second_ground_boundary:
            check_list = [func_dict['func'](solution, self.params, func_dict['lim']) for func_dict in
                          self.second_ground_boundary.values()]
            return all(check_list)
        else:
            return True

    def set_target_func(self, t_func) -> None:
        """
        Установка целевой функции
        :param t_func: Целевая функция(callable)
        :return:
        """
        self.t_func = t_func

    def set_out_func(self, o_func):
        self.out_func = o_func

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
        last_x = self.x_vec[:]
        self._adapt(last_x)
        last_f, last_second_ground_boundary = self.t_func(last_x, self.params)
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
                            last_f, last_x = cur_f, xx[:]
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
        return last_x

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
        steps_total = 0
        bad_steps_cur = 1
        last_x = self.x_vec[:]
        self._adapt(last_x)
        last_f, last_second_ground_boundary = self.t_func(last_x, self.params)

        while steps_total < N:
            while bad_steps_cur < M:
                yj = self._get_yj(last_x, t0)
                self._adapt(yj)
                if self._check_first_ground_boundary(yj):
                    try:
                        cur_f, cur_solution = self.t_func(yj, self.params)
                        if self._check_second_ground_boundary(cur_solution):
                            if cur_f <= last_f and abs(cur_f - last_f) > min_delta_f:
                                zj = self._get_zj(last_x, alpha, yj)
                                self._adapt(zj)
                                if self._check_first_ground_boundary(zj):
                                    try:
                                        cur_f, cur_solution = self.t_func(zj, self.params)
                                        if self._check_second_ground_boundary(cur_solution):
                                            if cur_f <= last_f and abs(cur_f - last_f) > min_delta_f:
                                                last_x, last_f = zj, cur_f
                                                t0 *= alpha
                                                steps_total += 1
                                                if self.out_func:
                                                    # break
                                                    self.out_func(zj, cur_f, cur_solution, self.params)
                                                break
                                            else:
                                                bad_steps_cur += 1
                                        else:
                                            bad_steps_cur += 1
                                    except:
                                        bad_steps_cur += 1
                                else:
                                    bad_steps_cur += 1
                            else:
                                bad_steps_cur += 1
                        else:
                            bad_steps_cur += 1
                    except:
                        bad_steps_cur += 1
                else:
                    bad_steps_cur += 1

            if t0 <= R:
                if not np.array_equal(last_x, self.x_vec):
                    print(f"Оптимизация завершилась успешно, шаг минимальный {t0=}")
                    return last_x
                else:
                    raise MinStepOptimizerError()
            else:
                t0 *= beta
                bad_steps_cur = 1
        if not np.array_equal(last_x, self.x_vec[:]):
            print("Оптимизация завершилась успешно, израсходованно максимальное число итераций")
            return last_x
        else:
            raise TooMuchItersOptimizerError()