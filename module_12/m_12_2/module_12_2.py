"""
Примечания:
Ваш код может отличаться от строгой последовательности описанной в задании.
    Главное - схожая логика работы тестов
        и наличие всех перечисленных переопределённых методов из класса TestCase.
"""
from unittest import TestCase, skipIf
import lessons.module_12.m_12_2.RunAndTor as r_t


class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(self):
        """
        setUpClass
        """
        self.all_results = []

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        """
        setUp
        """
        self.a = r_t.Runner("Первый", 100)
        self.b = r_t.Runner("Второй", 10)
        self.c = r_t.Runner("Третий", 1)
        self.participants = self.a, self.b, self.c
        self.finishers = self.a, self.b, self.c

    @classmethod
    def tearDownClass(self):
        """
        tearDownClass
        """
        # for item in self.all_results:
        #     print(*item)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        """
        Забег на дистанцию
        """
        #  Дистанция забега, любое целое число
        t_dist = 90
        x = r_t.Tournament(t_dist, *self.participants)
        res = x.start()
        #
        self.all_results.append([f'{self.test_1.__name__}: '])
        for index in range(len(self.finishers)):
            self.assertTrue(res[index + 1] == self.finishers[index])
            self.all_results.append([f'\t"{res[index + 1]}" равно "{self.finishers[index]}"\tOk'])
        self.all_results.append([])

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        """
        Влияние результатов первого забега на последующий
        """
        self.a.distance, self.b.distance, self.c.distance = 0, 0, 0
        participants = self.a, self.b, self.c
        #
        # Первый забег участников
        x = r_t.Tournament(1000, *participants)
        res = x.start()
        #
        self.all_results.append([f'{self.test_2.__name__}: Первый забег участников'])
        for index in range(len(self.finishers)):
            self.assertTrue(res[index + 1] == self.finishers[index])
            self.all_results.append([f'\t"{res[index + 1]}" равно "{self.finishers[index]}"\tOk'])
        self.all_results.append([])
        #
        # Влияние результатов первого забега на последующий
        x = r_t.Tournament(90, *participants)
        res = x.start()
        #
        self.all_results.append([f'{self.test_2.__name__}: Влияние результатов первого забега на последующий'])
        for index in range(len(self.finishers)):
            self.assertTrue(res[index + 1] == self.finishers[index])
            self.all_results.append([f'\t"{res[index + 1]}" равно "{self.finishers[index]}"\tOk'])
        self.all_results.append([])

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        """
        Тестирование забегов на разные дистанции
        """
        self.all_results.append([f'{self.test_3.__name__}:'])
        for distance in range(2000, 0, -1):
            self.a.distance, self.b.distance, self.c.distance = 0, 0, 0
            participants = self.a, self.b, self.c
            x = r_t.Tournament(distance, self.a, self.b, self.c)
            finishers = x.start()
            self.assertTrue(len(finishers.keys()) == 3)
            for key in finishers:
                self.assertTrue(finishers[key] == participants[key - 1])
            self.all_results.append([f'\tДлина дистанции забега: {distance}\tOk'])
