"""
En esta segunda versión el fichero de preguntas va a ser json, se adjunta un ejemplo. Adecuar la ejecución del
test a este fichero en vez de al que se había propuesto inicialmente.
"""
import time
from repaso.autotest.autotest_v1.question import Question, QuestionError
import json
import sys

TOTAL_SCORE = 0


def main():
    global TOTAL_SCORE
    if len(sys.argv) != 2:
        raise ValueError("La cantidad de argumentos es erronea")

    filename = sys.argv[1]
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)

    for question in data:
        options = question['options']
        question['options'] = [(str(option), float(score)) for option, score in options]

        name = (question['name'])
        statement = (question['statement'])
        options = (question['options'])
        points = (question['points'])

        q = Question(name, statement, options, points)
        print("────────────────────────────────────\n" + q.question_name + "\n────────────────────────────────────\n\n"
              + q.statement + "\n------------------------------------\n")
        num_question = 1
        for o in q.options:
            print(f"{num_question}) {o[0]}")
            num_question += 1
        try:
            answer = int(input("\n¿Cuál es la respuesta correcta? "))
            question_score = q.get_question_score(answer)
            time.sleep(1)
            print(f"Puntuación: {question_score}\n")
            TOTAL_SCORE += question_score
        except QuestionError as e:
            print(f"Error en la respuesta. {e}")

    print(f"La puntuación total sobre 10 es: {TOTAL_SCORE / len(data) * 10}")


if __name__ == '__main__':
    main()
