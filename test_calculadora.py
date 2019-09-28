import calculadora
import unittest


class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(calculadora.Calculadora.suma(''), 0, "caso vacio")

    def test_suma_un_numero(self):
        self.assertEqual(calculadora.Calculadora.suma("7"),
                         7, "caso string con un número")

    def test_suma_un_numero_varios(self):
        self.assertEqual(calculadora.Calculadora.suma("5"),
                         5, "caso string con un número")
        self.assertEqual(calculadora.Calculadora.suma("10"),
                         10, "caso string con un número")
        self.assertEqual(calculadora.Calculadora.suma("77"),
                         77, "caso string con un número")

    def test_suma_dos_numeros(self):
        self.assertEqual(calculadora.Calculadora.suma(
            "1, 3"), 4, "caso dos números")
