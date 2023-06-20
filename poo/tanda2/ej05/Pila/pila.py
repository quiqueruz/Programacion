"""
Crea una clase que represente una estructura de datos tipo pila (stack) y otra tipo cola (queue).

La pila y la cola permitirán estas operaciones:

    -Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
    -Obtener el número de elementos almacenados (tamaño).
    -Saber si la pila o la cola está vacía.
    -Vaciar completamente la pila o la cola.
Para el caso de la pila:
    -Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
    -Desapilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina.
    -Leer el elemento superior de la pila sin retirarlo (top).
"""


class Pila:
    def __init__(self, *valores_pila):
        self.__valores_pila = list(valores_pila)
        if len(self.__valores_pila) == 1 and isinstance(self.__valores_pila[0], Pila):
            self.__valores_pila = list(valores_pila[0].__valores_pila)

    @propety
    def valores_pila(self):
        return self.__valores_pila

    @property
    def longitud(self):
        return len(self.__valores_pila)

    def vaciar(self):
        return self.__valores_pila.clear()

    def comprobar_vacia(self):
        return len(self.__valores_pila) == 0

    def push(self, valor):
        return self.__valores_pila.insert(0, valor)

    def pop(self, valor):
        return self.__valores_pila.pop(valor)

    def top(self):
        return self.__valores_pila[len(self.__valores_pila) - 1]

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__valores_pila}"

    def __str__(self):
        return f"{self.__valores_pila}"
