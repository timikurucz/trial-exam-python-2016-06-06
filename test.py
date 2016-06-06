import unittest
from greeter import greeter

class TestGreeter(unittest.TestCase):
    def test_length_is_greater_than_zero(self):
        self.assertEqual(greeter('Bela'), 'Hello, Bela!')

    def test_empty_input(self):
        self.assertEqual(greeter(''), 'Hello, Mr Nobody!')

    # def test_input_is_not_a_string(self):
    #     self.assertRaises(greeter(4), TypeError)

if __name__ == '__main__':
    unittest.main()
