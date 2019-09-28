import calculadora
import unittest


class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(calculadora.Calculadora.suma(''), 0, "caso vacio")

    def test_suma_un_numero(self):
        self.assertEqual(calculadora.Calculadora.suma("7"),
                         7, "caso string con un número")
