from threading import Thread
from random import randint
from time import sleep
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.queue = queue.Queue()
        self.tables = args
        self.some_of_tables_is_not_empty = False

    def guest_arrival(self, *guests):
        """ Размещение гостей при открытии ресторана/кафе """
        self.guests = guests
        for guest in self.guests:
            is_ok = False
            for table in self.tables:
                if table.guest == None:
                    table.guest = guest
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    self.some_of_tables_is_not_empty = True
                    is_ok = True
                    break
                else:
                    continue
            if not is_ok:
                print(f"{guest.name} в очереди")
                self.queue.put(guest)

    def discuss_guests(self):
        while not self.queue.empty() or self.some_of_tables_is_not_empty:

            """ Обслуживание столов с гостями """
            for table in self.tables:
                if table.guest:
                    if table.guest.is_alive():
                        continue
                    else:
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        table.guest = None
                        print(f"Стол номер {table.number} свободен")
                        if self.queue.empty():
                            continue
                        else:
                            table.guest = self.queue.get()
                            table.guest.start()
                            print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

            """ Проверка: Есть ли за столами гости? """
            for table in self.tables:
                if table.guest is not None:
                    """ Попадёт в эту ветку если какой-нибудь из столов не пуст
                    [table is not None],
                    break - защелка, фиксирует состояние флага 'some_of_tables_is_not_empty'
                    """
                    self.some_of_tables_is_not_empty = True
                    break
                else:
                    """ Если каждый из столов пустой 
                    [table is None] 
                    """
                    self.some_of_tables_is_not_empty = False


if __name__ == '__main__':
    print("------------------>  if __name__ == '__main__'  <------------------")

    # Создание столов
    tables = [Table(number) for number in range(1, 6)]

    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]

    # Создание гостей
    guests = [Guest(name) for name in guests_names]

    # Заполнение кафе столами
    cafe = Cafe(*tables)

    # Приём гостей
    cafe.guest_arrival(*guests)

    # Обслуживание гостей
    cafe.discuss_guests()
