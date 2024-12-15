"""
"Простые Юнит-Тесты"
Задача "Проверка на выносливость"
"""
from unittest import TestCase, skipIf
import lessons.module_12.m_12_1.runner as rn


class RunnerTest(TestCase):
    is_frozen = False

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        x = rn.Runner("SomeName")
        for i in range(10):
            x.walk()
        self.assertEqual(x.distance, 50)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        x = rn.Runner("SomeName")
        for i in range(10):
            x.run()
        self.assertEqual(x.distance, 100)

    @skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        x = rn.Runner("Some_Walker")
        y = rn.Runner("Some_Runner")
        for i in range(10):
            x.walk()
            y.run()
        self.assertNotEqual(x.distance, y.distance)
