import logging
from unittest import TestCase, skipIf
from rt_with_exceptions import Runner


class RunnerTest(TestCase):
    logging.basicConfig(level=logging.INFO, filemode='w', encoding='utf-8', filename='runner_tests.log',
                        format="%(asctime)s || %(levelname)s || %(message)s")

    is_frozen = False
    reason_ = 'Тесты в этом кейсе заморожены'

    @skipIf(is_frozen, reason_)
    def test_walk(self):
        try:
            name = "SomeName"
            speed = -5  # 5
            runner = Runner(name, speed)
            count = 10
            for i in range(count):
                runner.walk()
            self.assertEqual(runner.distance, speed * count)
            #
            logging.info(f'"test_walk" выполнен успешно')
        except Exception as e:
            logging.warning(f'"Неверная скорость для Runner" {e}', exc_info=False)

    @skipIf(is_frozen, reason_)
    def test_run(self):
        try:
            name = 3.14  # "SomeName"
            speed = 5
            runner = Runner(name, speed)
            count = 10
            for i in range(count):
                runner.run()
            self.assertEqual(runner.distance, (speed * 2) * count)
            #
            logging.info(f'"test_run" выполнен успешно')
        except Exception as e:
            logging.warning(f'"Неверный тип данных для объекта Runner" {e}', exc_info=False)

    @skipIf(is_frozen, reason_)
    def test_challenge(self):
        walker = Runner("Some_Walker")
        runner = Runner("Some_Runner")
        for i in range(10):
            walker.walk()
            runner.run()
        self.assertNotEqual(walker.distance, runner.distance)
