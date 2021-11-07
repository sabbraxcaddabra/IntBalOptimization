from dataclasses import dataclass


#__all__ = ["ArtSystem", "Powder", "IntBalParams"]


@dataclass
class ArtSystem:
    # Датакласс для данных об артиллерийской системе
    name: str  # Наименование артиллерийской системы
    d: float  # Калибр орудия
    q: float  # Масса снаряда
    S: float  # Приведенная площадь канала ствола
    W0: float  # Объем зарядной каморы
    l_d: float  # Полный путь снаряда
    l_k: float  # Длина зарядной каморы
    l0: float  # Приведенная длина зарядной каморы
    Kf: float  # Коэффициент слухоцкого


@dataclass
class Powder:
    # Датакласс для данных о порохе
    name: str  # Марка пороха
    omega: float  # Масса метательного заряда
    rho: float  # Плотность пороха
    f_powd: float  # Сила пороха
    Ti: float  # Температура горения пороха
    Jk: float  # Конечный импульс пороховых газов
    alpha: float  # Коволюм
    teta: float  # Параметр расширения
    Zk: float  # Относительная толщина горящего свода, соответствующая концу горения
    #PsiS: float # Относительная масса сгоревшего пороха к моменту распада
    kappa1: float  # 1-я, 2-я и 3-я хар-ки формы пороховых элементов до распада
    lambd1: float
    mu1: float
    kappa2: float  # 1-я, 2-я и 3-я характеристики формы пороховых элементов после распада
    lambd2: float
    mu2: float


class IntBalParams:
    # Класс начальных условий
    # Система "Орудие-заряд-снаряд"
    def __init__(self, syst, P0, PV):
        self.syst = syst  # Арт.система для задачи
        self.charge = []  # Метательный заряд
        self.P0 = P0  # Давление форсирования
        self.PV = PV # Давление воспламенителя

    def add_powder(self, powder: Powder) -> None:
        self.charge.append(powder)

    def create_params_tuple(self) -> tuple:
        # Метод для создания исходных данных
        params = [
            self.P0,
            self.PV,
            50e6**0.25,
            self.syst.S,
            self.syst.W0,
            self.syst.l_k,
            self.syst.l0,
            sum(powd.omega for powd in self.charge),
            self.syst.Kf*self.syst.q,
            self.syst.l_d
        ]
        powders = []
        for powder in self.charge:
            tmp = (
                powder.omega,
                powder.rho,
                powder.f_powd,
                powder.Ti,
                powder.Jk,
                powder.alpha,
                powder.teta,
                powder.Zk,
                powder.kappa1,
                powder.lambd1,
                powder.mu1,
                powder.kappa2,
                powder.lambd2,
                powder.mu2,
            )
            powders.append(tmp)
        params.append(tuple(powders))
        return tuple(params)