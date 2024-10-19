from time import sleep
from random import randint
from threading import Thread, Lock


class Bank:
    def __init__(self):
        self.balance = int()
        self.lock = Lock()

    def deposit(self):
        for i in range(5):
            x = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
                self.balance += x
                print(f"Пополнение: {x}. Баланс: {self.balance}")
            else:
                self.balance += x
                print(f"Пополнение: {x}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(5):
            x = randint(50, 500)
            print(f"Запрос на {x}")
            if x > self.balance:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            else:
                self.balance -= x
                print(f"Снятие: {x}. Баланс: {self.balance}")


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
