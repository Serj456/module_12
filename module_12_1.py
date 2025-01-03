import unittest
from runner import Runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walk_name = Runner('walk_name')
        for i in range(10):
            walk_name.walk()
        self.assertEqual(walk_name.distance, 50)

    def test_run(self):
        run_name = Runner('run_name')
        for i in range(10):
            run_name.run()
        self.assertEqual(run_name.distance, 100)

    def test_challenge(self):
        challenge_name_1 = Runner("Challenge_name_1")
        challenge_name_2 = Runner("Challenge_name_2")
        for i in range(10):
            challenge_name_1.walk()
            challenge_name_2.run()
        self.assertNotEqual(challenge_name_1.distance, challenge_name_2.distance)