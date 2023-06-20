"""
2. Seleccionar fichero de test.

    - Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.

    - La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque
        este programa únicamente maneja estos dos formatos.

            - Pensad que estos dos apartados son iguales que la opción anterior,
                igual podemos modularizar para ahorrar código.

    - Comprobamos que el fichero existe, si no es así acabamos advirtiendo del error.
"""
from repaso.autotest.autotest_v4.programas.crear_fichero_test.crear_fichero_test import ask_file, check_if_file_exists


def select_file():
    while True:
        filename, extension = ask_file()
        if ".json" == extension or ".xml" == extension[1:]:
            if not check_if_file_exists(filename):
                raise FileNotFoundError("El fichero no existe")
            break
        else:
            print("Selecciona un archivo .xml o . json")
    return filename


if __name__ == '__main__':
    select_file()
