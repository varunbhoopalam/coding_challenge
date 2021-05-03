import unittest

from models import Test

class ModelsTests(unittest.TestCase):

    def test_upper(self):
        foo = Test()
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
