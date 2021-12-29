import unittest
from roman import decompose, romanize, from_numeral_to_roman


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


class TestNumeralToRoman(unittest.TestCase):

    def test_decompose(self):
        self.assertEqual(decompose(14), [10, 4])
        self.assertEqual(decompose(79), [70, 9])
        self.assertEqual(decompose(225), [200, 20, 5])
        self.assertEqual(decompose(845), [800, 40, 5])
        self.assertEqual(decompose(2022), [2000, 20, 2])
        self.assertEqual(decompose(99999), [90000, 9000, 900, 90, 9])

    def test_romanize(self):
        self.assertEqual(romanize(4), "IV")
        self.assertEqual(romanize(7), "VII")
        self.assertEqual(romanize(30), "XXX")
        self.assertEqual(romanize(70), "LXX")
        self.assertEqual(romanize(200), "CC")
        self.assertEqual(romanize(900), "CM")
        self.assertEqual(romanize(2000), "MM")
        self.assertEqual(romanize(
            90000), "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")

    def test_numeral_to_roman(self):
        self.assertEqual(from_numeral_to_roman(14), "XIV")
        self.assertEqual(from_numeral_to_roman(79), "LXXIX")
        self.assertEqual(from_numeral_to_roman(225), "CCXXV")
        self.assertEqual(from_numeral_to_roman(845), "DCCCXLV")
        self.assertEqual(from_numeral_to_roman(2022), "MMXXII")
        self.assertEqual(from_numeral_to_roman(
            99999), "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMCMXCIX")


if __name__ == '__main__':
    unittest.main()
