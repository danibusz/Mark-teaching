import unittest

from classic import Horse

test_horse = Horse(age = 4, name = "Owerlord", gender = "male")

class HorseTester:
    def test_horse_good_age(self):
        self.assertEqual(5,test_horse.age)

    def test_horse_good_name(self):
        self.assertEqual("Owerlord", test_horse.name)

    def test_horse_dies_if_we_kill_it(self):
        self.assertTrue(test_horse.isAlive)
        test_horse.die()
        self.assertFalse(test_horse.isAlive)

    def test_horse_aging(self):
        current_age = test_horse.age
        test_horse.aging()
        self.assertEqual((current_age + 1), test_horse.age)
