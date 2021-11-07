class TooMuchPowderError(Exception):
    def __str__(self):
        return "Слишком много пороха"

class TooMuchTime(Exception):
    def __str__(self):
        return "Превышено максимальное время выстрела"