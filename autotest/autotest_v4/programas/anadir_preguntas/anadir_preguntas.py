"""
3. Añadir pregunta al test.

    - Si no se ha seleccionado o creado fichero de test se debe indicar al usuario y terminar con esta opción.

    - Pedimos los datos correspondientes a la pregunta, teniendo en cuenta que el enunciado puede tener varias líneas.

    - Comprobamos que los datos son correctos,  para ello podríamos crear un objeto Question y si no lanza excepción
        es que están bien.

    - Añadimos la pregunta al fichero en el formato que tenga (JSON o XML).
            - Para hacer esto cargamos el JSON o XML desde el fichero a una variable, la modificamos y
                escribimos de nuevo en el fichero.
"""
import sys
from repaso.autotest.autotest_v1.question import Question
import xml.etree.ElementTree as ET
import json


def check_question(titulo_pregunta, enunciado_pregunta, opciones, puntuacion):
    try:
        Question(titulo_pregunta, enunciado_pregunta, opciones, puntuacion)
    except ValueError:
        print("El formato de la pregunta no es correcto.", file=sys.stderr)
        sys.exit(1)


def add_questions(filename):
    extension = filename[-5:]
    if extension == ".json":
        question_title = input("Introduce el titulo de la pregunta: ")
        base_score = int(input("Introduce la puntuación de la pregunta: "))
        question_statement = input("Introduce el enunciado de la pregunta: ")

        question_data = {
            'name': question_title,
            'base_score': base_score,
            'statement': question_statement,
            'options': []
        }

        QUESTION_NUMBER = 4

        for i in range(QUESTION_NUMBER):
            option = input(f"Escribe la opción {i + 1}: ")
            weight = input(f"Escribe el valor de la opción {i + 1}: ")
            option_data = {
                'option': option,
                'weight': weight
            }
            question_data['options'].append(option_data)

        with open(filename, 'r', encoding='utf-8') as f:
            try:
                questions = json.load(f)
            except ValueError:
                questions = []

        questions.append(question_data)

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(questions, f, indent=2)

    elif extension[1:] == ".xml":
        total_questions = 4
        options_list = []

        tree = ET.parse(filename)
        root = tree.getroot()

        question_title = input("Introduce el titulo de la pregunta: ")
        base_score = int(input("Introduce la puntuación base de la pregunta: "))
        question_statement = input("Introduce el enunciado de la pregunta: ")

        name = ET.Element('question', {'name': question_title, 'base_score': str(base_score)})
        statement = ET.SubElement(name, 'statement')
        statement.text = question_statement
        options = ET.SubElement(statement, 'options')

        for i in range(total_questions):
            option = input(f"Escribe la opción {i + 1}: ")
            weight = input(f"Escribe el valor de la opción {i + 1}: ")
            posible_option = ET.SubElement(options, 'option', {'weight': weight})
            posible_option.text = option
            options_list.append((option, float(weight)))

        check_question(question_title, question_statement, options_list, int(base_score))

        root.append(name)
        ET.indent(root, space='  ')
        tree.write(filename, encoding='utf-8', xml_declaration=True)
