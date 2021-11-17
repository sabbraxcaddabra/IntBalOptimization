from InternalBallistics.IntBalClasses import Powder
from InternalBallistics.ErrorClasses import NoOneCombo
from itertools import combinations

def check_Jk(powder, Jk_dop, max_tol):
    tol = abs((powder.Jk/Jk_dop)*100 - 100)
    if tol <= max_tol:
        return True

def get_powder_combination(Jk_dop_list, max_tol=15.):
    """
    Функция читающая базу порохов и по допустимым конечным импульсам(полученным в результате решения обобщенной задачи)
    возвращающая кортеж всех возможных комбинаций порохов
    :param Jk_dop_list: Итерируемый объект с допустимыми конечными импульсами(список/кортеж и тд.)
    :param max_tol: Максимальная ошибка по конечному импульсу
    :return: Кортеж всех возможных комбинаций порохов
    """
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
        comb_powders = tuple(combinations(powders_list, len(Jk_dop_list)))
        return comb_powders


if __name__ == "__main__":
    Jk_dop_list = [343.8e3, 681e3]

    comb = get_powder_combination(Jk_dop_list)


