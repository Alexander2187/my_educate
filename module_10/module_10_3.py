from time import sleep
from random import randint
from threading import Thread, Lock


class Bank:
    def __init__(self):
        self.balance = int()
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.lock.locked():
                x = randint(50, 500)
                self.balance += x
                print(f"Пополнение: {x}. Баланс: {self.balance}")
                if self.balance >= 500:
                    sleep(0.001)
                    self.lock.release()
                else:
                    sleep(0.001)
            else:
                sleep(0.001)


    def take(self):
        for i in range(100):
            if self.lock.locked():
                sleep(0.001)
                continue
            else:
                sleep(0.001)
                x = randint(50, 500)
                print(f"Запрос на {x}")
                if x <= self.balance:
                    self.balance -= x
                    print(f"Снятие: {x}. Баланс: {self.balance}")
                else:
                    print(f"Запрос отклонён, недостаточно средств")
                    self.lock.acquire()

bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
