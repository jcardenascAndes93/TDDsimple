import calculadora
import unittest


class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(calculadora.Calculadora.suma(''), 0, "caso vacio")
