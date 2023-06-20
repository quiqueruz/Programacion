"""
Crea una clase que represente una estructura de datos tipo pila (stack) y otra tipo cola (queue).

La pila y la cola permitirán estas operaciones:

    -Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
    -Obtener el número de elementos almacenados (tamaño).
    -Saber si la pila o la cola está vacía.
    -Vaciar completamente la pila o la cola.
Para el caso de la cola:
    -Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
    -Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola,
        es decir, el primer elemento que entró.
    -Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).
"""


class Cola:
    def __init__(self, *valores_cola):
        self.__valores_cola = list(valores_cola)
        if len(self.__valores_cola) == 1 and isinstance(self.__valores_cola[0], Cola):
            self.__valores_cola = list(valores_cola[0].__valores_cola)

    @property
    def valores_cola(self):
        return self.__valores_cola

    @property
    def longitud(self):
        return len(self.__valores_cola)

    def vaciar(self):
        return self.__valores_cola.clear()

    def comprobar_vacia(self):
        return len(self.__valores_cola) == 0

    def enqueue(self, valor):
        return self.__valores_cola.append(valor)

    def dequeue(self):
        return self.__valores_cola.pop(0)

    def front(self):
        return self.__valores_cola[0]

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__valores_cola}"

    def __str__(self):
        return f"{self.__valores_cola}"
