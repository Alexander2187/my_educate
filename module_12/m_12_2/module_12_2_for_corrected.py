from unittest import TestCase
import runner_and_tournament_corrected as cr_t

"""
Тесты для конфликтных ситуаций:
    Один участник участвует в нескольких забегах.
    Тестирование забегов на разные дистанции.
    Порядок обработки списка бегунов в классе не должен влиять на результат забега.
    Скорость двух или более бегунов превышает длину дистанции забега.
    Скорость двух или более бегунов одинакова или два или более бегуна/ов финишируют одновременно.
"""


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(self):
        """
        Создает атрибут хранящий результаты работы тестов.
        """
        self.all_results = []

    def setUp(self):
        """
        setUp - метод, где создаются объекты класса Runner
        """
        #
        # Для test_1, test_runner, test_toutnaments
        # Бегуны с разной скоростью.
        self.a = cr_t.Runner("Первый", 100)
        self.b = cr_t.Runner("Второй", 10)
        self.c = cr_t.Runner("Третий", 1)
        self.test_participants = self.a, self.b, self.c
        #
        # Для test_2
        # Участники со скоростью больше длины дистанции.
        # Значения скорости могут быть произвольными,
        # т.к. для длины дистанции берётся наименьшая из них.
        self.bb1 = cr_t.Runner("Последний", 8)
        self.bb2 = cr_t.Runner("Второй_равный", 32)
        self.bb3 = cr_t.Runner("Третий_равный", 32)
        self.participants_with_speed_greater_than_distance = self.bb1, self.bb2, self.bb3
        #
        # Для test_3
        # Бегуны с одинаковой скоростью.
        self.aa1 = cr_t.Runner("Первый_равный", 10)
        self.aa2 = cr_t.Runner("Второй_равный", 10)
        self.aa3 = cr_t.Runner("Третий_равный", 10)
        self.participants_with_equal_speeds = self.aa1, self.aa2, self.aa3

    @classmethod
    def tearDownClass(self):
        """
        Печатает в консоль результаты работы тестов (содержимое списка self.all_results)
        """
        print('JR')
        for item in self.all_results:
            print(*item)

    def test_runner(self):
        """
        Одни и те же участники учавствуют в нескольких забегах.
        Результаты участников в предыдущем забеге не должны влиять на результаты последующего.
        """
        # Зададим некоторые значения дистанции для каждого из участников.
        # Проверим обнуляются ли значения дистанции с предыдущего забега.
        self.a.distance, self.b.distance, self.c.distance = 100, 1000, 10000
        x = cr_t.Tournament(90, self.a, self.b, self.c)
        f = x.start()
        self.assertTrue(len(f) == len(self.test_participants))
        prt = self.test_participants
        self.all_results.append([f'{self.test_runner.__name__}: '])
        for key in f.keys():
            # Сравним имена победителей, со списком участников.
            # Проверка работает корректно при условии
            # что имена всех участников уникальны, а их скорости и дистанция заданны верно.
            self.assertTrue(f[key][0].name == prt[key - 1].name)
            self.all_results.append([f'\t\tМесто:  {key} {f[key][0].name} {prt[key - 1].name}'])

    def test_tournaments(self):
        """
        Тестирование забегов на разные дистанции.
        """
        #
        # Заголовки столбцов таблицы и их ширина
        t_place = 'Место'.center(10, " ")
        t_name = 'Имя участника'.center(14, " ")
        t_speed = 'Скорость уч-ка'.center(10, " ")
        t_distance = 'Дистанция уч-ка'.center(11, " ")
        #
        for len_distance in range(23, 0, -1):
            #
            # Заголовок таблицы
            self.all_results.append([f'{self.test_tournaments.__name__}: '
                                     f'\n\nДистанция забега {len_distance}:'])
            #
            # Забег
            x = cr_t.Tournament(len_distance, self.test_participants)
            f = x.start()
            f_keys = f.keys()
            #
            # Сводная таблица участников забега на дистанцию: {len_distance}
            self.all_results.append([f'| {t_place}| {t_name}| {t_speed}| {t_distance}|'])
            for key in f_keys:
                for fin in f[key]:
                    self.all_results.append([f'| {str(key).center(len(t_place), " ")}'
                                             f'| {str(fin.name).ljust(len(t_name), " ")}'
                                             f'| {str(fin.speed).rjust(len(t_speed), " ")}'
                                             f'| {str(fin.distance).rjust(len(t_distance), " ")}'
                                             f'|'])
            self.all_results.append(["-" * (len(t_place) + len(t_name)
                                            + len(t_speed) + len(t_distance) + 9), "\n"])

    def test_1(self):
        """
        Порядок обработки списка бегунов в классе не должен влиять на результат забега.
        """
        len_distance = 3
        #
        # Прямой порядок участников
        self.test_participants = self.a, self.b, self.c
        x_abc = cr_t.Tournament(len_distance, self.test_participants)
        t_abc = x_abc.start()
        #
        # Обратный порядок участников
        self.test_participants = self.c, self.b, self.a
        x_cba = cr_t.Tournament(len_distance, self.test_participants)
        t_cba = x_cba.start()
        #
        # Сравним результаты двух забегов
        self.assertTrue(len(t_abc) == len(t_cba))
        self.assertTrue(t_abc.keys() == t_cba.keys())
        # Перебор мест в турнирной таблице
        self.all_results.append([f'{self.test_1.__name__}:'])
        for key in t_abc.keys():
            # Сравним два множества имен победителей, занявших одно и то же место.
            # Проверка работает корректно при условии что имена всех участников уникальны.
            var_1 = set([t_abc[key][index].name for index in range(len(t_abc[key]))])
            var_2 = set([t_cba[key][index].name for index in range(len(t_cba[key]))])
            self.assertTrue(var_1 == var_2)
            self.all_results.append([f'\t\tМесто:  {key} {var_1}\n\t\tМесто:  {key} {var_2}'])

    def test_2(self):
        """
        Скорость двух или более бегунов равна или превышает длину дистанции забега.
        """
        # Cкорость самого медленного бегуна.
        distance = min([x.speed for x in self.participants_with_speed_greater_than_distance])
        x = cr_t.Tournament(distance, self.participants_with_speed_greater_than_distance)
        #
        # Забег, участники которого имеют скорость больше чем длинна забега
        finishers = x.start()
        self.assertTrue(len(finishers) == 1)
        great_p = self.participants_with_speed_greater_than_distance
        for key in finishers.keys():
            """
            Сравним множество имен победителей, со множеством имен участников.

            Вне зависимости от скорости все участники займут первое место,
                из-за особенностей наших классов Runner и Tournament.
            Из-за того что единицей измерения служит скорость в рамках одного "Рывка",
                получается что точность измерений стала меньше измеряемой величины,
                а значит и разницы между участниками нет.
            Разумеется это не совсем верно, но без дополнительного усложнения и\или переписывания
                классов Runner и Tournament, с точным замером прохождения участниками последнего "Рывка" 
                или отрезка дистанции, решить эту делему не представляется возможным.
            Более того, в случае радикальных изменений в классах Runner и Tournament, 
                соответственно придётся полностью переписывать тесты.

            Проверка работает корректно при условии что имена всех участников уникальны.
            """
            var_1 = set([finishers[key][index].name for index in range(len(finishers[key]))])
            var_2 = set([great_p[index].name for index in range(len(great_p))])
            self.assertTrue(var_1 == var_2)
            self.all_results.append([f'{self.test_2.__name__}:  \n\t\t{var_1}  \n\t\t{var_2}'])

    def test_3(self):
        """
        Скорость двух или более бегунов одинакова или два или более бегуна/ов финишируют одновременно.
        """
        x = None
        # Произвольное число, но больше чем скорость бегуна.
        distance = 72
        if self.aa1.speed == self.aa2.speed == self.aa3.speed and distance > self.aa1.speed:
            x = cr_t.Tournament(distance, self.participants_with_equal_speeds)
        else:
            raise ValueError("Скорости бегунов не равны или меньше длинны дистанции!!!")
        #
        # Забег участники которого имеют одинаковую скорость
        finishers = x.start()
        self.assertTrue(len(finishers) == 1)
        equal_p = self.participants_with_equal_speeds
        for key in finishers.keys():
            # Сравним множество имен победителей, со множеством имен участников.
            # Все участники займут первое место
            # Проверка работает корректно при условии что имена всех участников уникальны.
            var_1 = set([finishers[key][index].name for index in range(len(finishers[key]))])
            var_2 = set([equal_p[index].name for index in range(len(equal_p))])
            self.assertTrue(var_1 == var_2)
            self.all_results.append([f'{self.test_3.__name__}:  \n\t\t{var_1}  \n\t\t{var_2}'])
