# Блокировки и обработка ошибок. Банковские операции
import threading
import random
import time


class Bank:
    def __init__(self, balance):
        self.lock = threading.Lock()
        if isinstance(balance,int):
            self.balance = balance
        else:
            raise ValueError("Баланс - целое число!")

    def deposit(self):
        i = 0
        while i <= 100:
            number = random.randint(50, 500)
            self.balance += number
            print(f'Пополнение: {number}. Баланс: {self.balance}.')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)
            i += 1

    def take(self):
        i = 0
        while i <= 100:
            number = random.randint(50, 500)
            print(f'Запрос на {number}.')
            if number <= self.balance:
                self.balance -= number
                print(f'Снятие {number}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)
            i += 1

bk = Bank(7500)
th1 = threading.Thread(target=Bank.deposit, args=(bk, ))
th2 = threading.Thread(target=Bank.take, args=(bk, ))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')