from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power=1):
        super().__init__()
        self.name = name
        self.power = abs(power)


    def run(self):
        print(f"{self.name}, на нас напали!")
        days_ = 0
        enemies = 100
        while enemies > 0:
            enemies -= self.power
            days_ += 1
            print(f"{self.name} сражается {days_} дней(дня)..., осталось {enemies} воинов.")
            sleep(1)
        print(f"{self.name} одержал победу спустя {days_} дней(дня)!")

first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()