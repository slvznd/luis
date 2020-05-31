class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} поворачивает направо'

    def turn_left(self):
        return f'{self.name} поворачивает налево'

    def show_speed(self):
        return f'Текущая скорость у {self.name} равна {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f'Текущая скорость у {self.name} равна {self.speed}'

        if self.speed > 40:
            return f'{self.name} двигается с превышением скорости на {self.speed - 40}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f'Текущая скорость у {self.name} равна {self.speed}'

        if self.speed > 60:
            return f'{self.name} двигается с превышением скорости на {self.speed - 40}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} машина копов'
        else:
            return f'{self.name} нормальный парень'


car1 = SportCar(100, 'красный', 'Audi', False)
car2 = TownCar(30, 'белоый', 'kamaz', False)
car3 = WorkCar(70, 'синий', 'Lada', True)
car4 = PoliceCar(110, 'голубой', 'Ford', True)
print(car3.turn_left())
print(f'Когда {car2.turn_right()}, тогда {car1.stop()}')
print(f'{car3.go()}')
print(f'{car3.show_speed()}')
print(f'Цвет {car3.name} {car3.color}')
print(f'{car1.name} полиция? - {"да" if car1.is_police else "нет"}')
print(f'{car3.name} полиция? - {"да" if car3.is_police else "нет"}')
print(car1.show_speed())
print(car2.show_speed())
print(car4.show_speed())
print(car4.police())
