"""
Esta versión hará lo mismo que la versión 2, pero con ficheros XML.

Se adjunta un fichero XML de muestra.

Tened en cuenta que el atributo name correspondiente a la pregunta podría no estar y en este caso
el nombre de la pregunta es la cadena vacía.
"""
from repaso.autotest.autotest_v1.question import Question, QuestionError
import xml.etree.ElementTree as ET
import time

TOTAL_SCORE = 0


def main():
    global TOTAL_SCORE
    nombre_fichero = 'test.xml'
    archivo = ET.parse(nombre_fichero)
    root = archivo.getroot()
    for i in range(len(root)):
        name = root[i].get('name')
        base_score = root[i].get('base_score')
        statement = root[i][0].text.strip()
        options = root[i][1]
        options_list = []
        for j in range(len(options)):
            option = root[i][1][j].text.strip()
            weight = root[i][1][j].get('weight')
            options_list.append((option, float(weight)))

        question = Question(name, statement, options_list, int(base_score))

        print("────────────────────────────────────\n" + question.question_name +
              "\n────────────────────────────────────\n\n"
              + question.statement + "\n------------------------------------\n")
        num_question = 1
        for o in question.options:
            print(f"{num_question}) {o[0]}")
            num_question += 1
        try:
            answer = int(input('¿Cuál es la respuesta correcta?: '))
            time.sleep(1)
            question_score = question.get_question_score(answer)
            print(f'Puntuación obtenida: {question_score}')
            TOTAL_SCORE += question_score
        except ValueError:
            print("La respuesta introducida no es válida")
        except QuestionError as e:
            print(f'ERROR: {e}')

    print(f"La puntuación total sobre 10 es: {TOTAL_SCORE / len(root) * 10}")


if __name__ == '__main__':
    main()
