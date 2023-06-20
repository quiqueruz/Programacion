import sys
from repaso.autotest.autotest_v4.programas.crear_fichero_test.crear_fichero_test import create_test_file
from repaso.autotest.autotest_v4.programas.seleccionar_fichero.seleccionar_fichero import select_file
from repaso.autotest.autotest_v4.programas.anadir_preguntas.anadir_preguntas import add_questions
from repaso.autotest.autotest_v4.programas.menu.menu import Menu


def main():
    filename = ""
    menu = Menu("Crear fichero de test", "Seleccionar fichero de test", "Añadir preguntas al test", "Finalizar",
                title="\nAutotest V4")
    while True:
        opc = menu.choose()
        match opc:
            case 1:
                filename = create_test_file()
            case 2:
                try:
                    filename = select_file()
                except FileNotFoundError:
                    print("El fichero no existe.\n")
            case 3:
                if filename == "":
                    print("Primero debes crear o seleccionar un fichero.")
                    continue
                add_questions(filename)
            case 4:
                print("Hasta la próxima :-)")
                sys.exit(0)
            case _:
                print("Ha introducido una opción incorrecta, vuelva a intentarlo.")


if __name__ == '__main__':
    main()
