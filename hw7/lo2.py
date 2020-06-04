from abc import abstractmethod


class Dress:
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return str(f'Общий расход ткани на проекты \n'
                   f' {(self.param / 6.5 + 0.5) + (other.param * 2 + 0.3):.02f}')

    @abstractmethod
    def my_square(self):
        pass


class Coat(Dress):
    def __init__(self, param):
        super().__init__(param)
        self.param = param

    def __str__(self):
        return f'Площадь на пальто {self.my_square:.02f}'

    @property
    def my_square(self):
        return self.param / 6.5 + 0.5


class Jacket(Dress):
    def __init__(self, param):
        super().__init__(param)
        self.param = param

    def __str__(self):
        return f'Площадь на костюм {self.my_square:.02f}'

    @property
    def my_square(self):
        return self.param * 2 + 0.3


coat = Coat(20)
jacket = Jacket(10)
print(coat)
print(jacket)
print()
print(coat + jacket)
