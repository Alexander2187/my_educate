"""
"Простые Юнит-Тесты"
Задача "Проверка на выносливость"
"""

from unittest import TestCase
from runner import Runner


class RunnerTest(TestCase):

    def test_walk(self):
        x = Runner("SomeName")
        for i in range(10):
            x.walk()
        self.assertEqual(x.distance, 50)

    def test_run(self):
        x = Runner("SomeName")
        for i in range(10):
            x.run()
        self.assertEqual(x.distance, 100)

    def test_challenge(self):
        x = Runner("Some_Walker")
        y = Runner("Some_Runner")
        for i in range(10):
            x.walk()
            y.run()
        self.assertNotEqual(x.distance, y.distance)
