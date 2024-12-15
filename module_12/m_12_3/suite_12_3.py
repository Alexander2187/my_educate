import unittest
import lessons.module_12.m_12_1.module_12_1 as m12_1
import lessons.module_12.m_12_2.module_12_2 as m12_2

some_TS = unittest.TestSuite()
some_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(m12_1.RunnerTest))
some_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(m12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(some_TS)
