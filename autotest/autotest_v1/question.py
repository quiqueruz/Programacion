"""
Empezaremos creando una clase para modelar las preguntas, los objetos de esta clase (Question)
tendrán los siguientes atributos:
    • Nombre de la pregunta.
    • Enunciado.
    • Elecciones (posibles respuestas): lista de tuplas (texto respuesta, calificación en % [0,1]).
    • Puntuación base de la pregunta (por defecto 1).
El comportamiento de esta clase permite:
    • Obtener la puntuación de la pregunta enviándole la opción escogida y, en caso de tener otra
    puntuación base, la puntuación correspondiente.
    • Esta clase es inmutable.
    • Podrá tener las propiedades necesarias para conocer el valor de los atributos que hagan falta

Práctica a realizar:
--------------------
Crear la clase Question y la probamos haciendo un examen. Nuestro examen será de cinco
preguntas tipo test con cuatro posibles respuestas. Las respuestas acertadas valen dos puntos, las no
contestadas 0 puntos y las respuestas mal contestadas restan 0.25 puntos.
"""
from typeguard import typechecked


class QuestionError(Exception):
    def __init__(self):
        super().__init__(f"La respuesta introducida no es válida.")


@typechecked
class Question:

    def __init__(self, question_name: str, statement: str, options: list[tuple[str, float]], base_score: float = 1):
        self.__question_name = question_name
        self.__statement = statement
        self.__options = options
        self.__base_score = base_score

    @property
    def question_name(self):
        return self.__question_name

    @property
    def statement(self):
        return self.__statement

    @property
    def options(self):
        return self.__options.copy()

    @property
    def base_score(self):
        return self.__base_score

    def get_question_score(self, response: int):
        if 0 <= response > len(self.__options):
            raise QuestionError()
        return self.__options[response - 1][1]
