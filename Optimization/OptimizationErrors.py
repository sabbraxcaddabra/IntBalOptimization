class FirstStepOptimizationError(Exception):
    def __str__(self):
        return "Ошибка при первой попытке вычисления целевой функции.\nПроверьте исходные данные"

class TooMuchItersOptimizerError(Exception):
    def __str__(self):
        return "Не найдено ни одного оптимума. Израсходовано максимальное число итераций\n" \
               "Попробуйте меньший шаг или большее максимальное число итераций"

class MinStepOptimizerError(Exception):
    def __str__(self):
        return "Не найдено ни одного оптимума. Достигнут минимальный шаг\n" \
               "Попробуйте меньший шаг или большее максимальное число итераций"

class SecondGroundBoundaryError(Exception):
    pass

class FirstGroundBoundaryError(Exception):
    pass

class LimitExeedEroor(Exception):
    pass