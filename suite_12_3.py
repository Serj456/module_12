import unittest
import module_12_1
import module_12_2


TestSuite_1 = unittest.TestSuite()

TestSuite_1.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
TestSuite_1.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.Tournament))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestSuite_1)