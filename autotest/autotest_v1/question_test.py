"""
Question Test
"""
import time

from question import Question, QuestionError

TOTAL_SCORE = 0

questions = [Question("Capital España", "¿Cuál es la capital de España?", [("Madrid", 1), ("Barcelona", -0.25),
                                                                           ("Sevilla", -0.25), ("Valencia", -0.25)]),
             Question("Pregunta 2", "¿Cuál es el río más largo del mundo?", [("Amazonas", -0.25), ("Nilo", 1),
                                                                             ("Yangtsé", -0.25), ("Misisipi", -0.25)]),
             Question("Pregunta 3", "¿Quién pintó La Mona Lisa?", [("Leonardo da Vinci", 1), ("Miguel Ángel", -0.25),
                                                                   ("Rafael", -0.25), ("Van Gogh", -0.25)]),
             Question("Pregunta 4", "¿En qué año se proclamó la Segunda República española?", [("1931", 1),
                                                                                               ("1936", -0.25),
                                                                                               ("1978", -0.25),
                                                                                               ("1981", -0.25)]),
             Question("Pregunta 5", "¿Qué país africano es conocido como la 'perla del África'?", [("Tanzania", -0.25),
                                                                                                   ("Kenia", -0.25),
                                                                                                   ("Uganda", 1),
                                                                                                   ("Etiopía", -0.25)])
             ]


for q in questions:
    num_question = 1
    print("────────────────────────────────────\n" + q.question_name + "\n────────────────────────────────────\n\n"
          + q.statement + "\n------------------------------------\n")
    for o in q.options:
        print(f"{num_question}) {o[0]}")
        num_question += 1

    try:
        answer = int(input("\n¿Cuál es la respuesta correcta? Introduce '0' si no quieres responder: "))
        if answer == 0:
            question_score = 0
            print(f"Puntuación: {question_score}\n")
        else:
            question_score = q.get_question_score(answer)
            time.sleep(1)
            print(f"Puntuación: {question_score}\n")
            TOTAL_SCORE += question_score
    except (QuestionError, ValueError) as e:
        print(f"Error en la respuesta.")

print(f"La puntuación total sobre 10 es: {TOTAL_SCORE / len(questions) * 10}")
