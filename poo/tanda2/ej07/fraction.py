"""
    Ejercicio 7:
        Crea una clase "Fraction" inmutable (no hay setters, solo getters para numerador y denominador) de
        forma que podamos hacer las siguientes operaciones:

        Construir un objeto Fracción pasándole al constructor el numerador y el denominador. La fracción se construye
        simplificada, no se puede dividir por cero.
        Obtener resultado de la fracción (número real).
        Multiplicar la fracción por un número (el método devuelve otra fracción, simplificada).
        Multiplicar, dividir, sumar y restar fracciones (los métodos devuelven otra fracción, simplificada).
"""
from typeguard import typechecked
import math


@typechecked
class Fraction:

    def __init__(self, numerador: int, denominador: int):
        if denominador == 0:
            raise ValueError("El denominador no puede ser 0.")
        mcd = math.gcd(numerador, denominador)
        self.__numerador = numerador // mcd
        self.__denominador = denominador // mcd

    @property
    def numerador(self):
        return self.__numerador

    @property
    def denominador(self):
        return self.__denominador

    def resultado_fraccion(self):
        return self.__numerador // self.__denominador

    def __add__(self, other):
        numerador = self.__numerador * other.__denominador + self.__denominador * other.__numerador
        denominador = self.__denominador * other.__denominador
        return Fraction(numerador, denominador)

    def __sub__(self, other):
        numerador = self.__numerador * other.__denominador - self.__denominador * other.__numerador
        denominador = self.__denominador * other.__denominador
        return Fraction(numerador, denominador)

    def __mul__(self, other):
        if isinstance(other, int):
            return Fraction(self.__numerador * other, self.__denominador)
        else:
            return Fraction(self.__numerador * other.__numerador, self.__denominador * other.__denominador)

    def __rmul__(self, other):
        if isinstance(other, int):
            return Fraction(self.__numerador * other, self.__denominador)
        else:
            return Fraction(self.__numerador * other.__numerador, self.__denominador * other.__denominador)

    def __truediv__(self, other):
        return Fraction(self.__numerador * other.__denominador, self.__denominador * other.__numerador)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__numerador}/{self.__denominador})"
