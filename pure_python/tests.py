import unittest
from Man import Man


class TestManSurvey(unittest.TestCase):
    def test_man_class(self):
        man = Man('Jonh', 'Snow')
        self.assertEqual(man.first_name, 'Jonh')


if __name__ == "__main__":
    unittest.main()
