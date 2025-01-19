# За честь и отвагу
import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        if isinstance(power, int) and power > 0:
            self.power = power
        else:
            raise ValueError("Сила рыцаря должна быть положительным целым числом!")

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            enemies -= self.power
            time.sleep(1)
            days += 1
            print(f'{self.name} сражается {days} день (дня), осталось {enemies} воинов!')
        print(f'{self.name} одержал победу спустя {days} дней (дня)!')

firs_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
firs_knight.start()
second_knight.start()
firs_knight.join()
second_knight.join()
print(f'Все битвы закончились!')
