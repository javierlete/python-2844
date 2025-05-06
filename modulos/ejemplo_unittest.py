from ejemplo_doctest import sumar
import unittest

class TestEjemploDocTest(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-2, 5), 3)

unittest.main()  # Calling from the command line invokes all tests