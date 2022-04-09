class Car:
    speed = 0
    color = 'color'
    name = 'name'
    is_police = False

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        return f'Car {self.name} start moving with speed {speed} km/h'

    def stop(self):
        self.speed = 0
        return f'Car {self.name} stops'

    def turn(self, direction):
        if direction not in ['left', 'right']:
            return "Car doesn't understand where should it turn"
        else:
            return f'Car {self.name} turns {direction}'

    def show_speed(self):
        return f'{self.name} speed is {self.speed} km/h'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return "Speed is exceeded!"
        else:
            return super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.color = 'red'  # only red sport cars we trust


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 20:
            return "Speed is exceeded!"
        else:
            return super().show_speed()


class PoliceCar(Car):
    is_police = True

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)
        self.is_police = True


police = PoliceCar(100, 'white', 'skoda', False)
police_car = 'police car'
not_police_car = 'not police car'
print(f'In spite of our wish {police.name} is {police_car if police.is_police else not_police_car}')

worker = WorkCar(50, 'black', 'UAZ')
print(f'And work car {worker.name} is {police_car if worker.is_police else not_police_car} by default\n'
      f'But {worker.show_speed()} So the police will catch it up!\n'
      f"{police.turn('right')} - wow, it's a police turn. Now the intruder is stopped. {worker.stop()}.")

sportcar = SportCar(0, 'rose', 'ferrari')
towncar = TownCar(40, 'red', 'oka')

print(f"{sportcar.show_speed()} and {towncar.show_speed()}. Wtf?\n"
      f"E-ron-don-don. {sportcar.go(200)}\n"
      f"Besides {sportcar.name} couldn't be rose. {sportcar.color.title()} only!")
