"""
1. Crear fichero de test.

    - Pedirá al usuario una cadena con el nombre del fichero donde se almacenarán las preguntas.

    - La extensión del fichero debe ser json o xml, si no es así hay que advertir de que no es posible hacerlo porque
        este programa únicamente maneja estos dos formatos.

    - Si el fichero existe, se debe advertir al usuario/a de esta circunstancia y darle la opción de volver atrás.

    - Finalmente se creará el fichero correspondiente.
"""
import os
import xml.etree.ElementTree as ET


def check_if_file_exists(file):
    if os.path.exists(file):
        return True
    return False


def ask_file():
    filename = input('Introduce el nombre del archivo con extensión XML o JSON: ')
    extension = filename[-5:]
    return filename, extension


def create_test_file():
    while True:
        filename, extension = ask_file()
        if ".json" == extension:
            if not check_if_file_exists(filename):
                f = open(filename, "wt", encoding='utf-8')
                f.close()
                print(f"Fichero '{filename}' creado correctamente.")
                break
            else:
                overwrite = input(f"El archivo '{filename}' ya existe. Si no quiere sobreescribirlo escriba 'N': ")
                if overwrite.upper() == "N":
                    continue
                else:
                    f = open(filename, "wt", encoding='utf-8')
                    f.close()
                    print(f"Fichero '{filename}' creado correctamente")
                    break
        elif ".xml" == extension[1:]:
            if not check_if_file_exists(filename):
                root = ET.Element('test')
                tree = ET.ElementTree(root)
                with open(filename, 'wb') as f:
                    tree.write(f, encoding='utf-8', xml_declaration=True)
                    print(f"Fichero '{filename}' creado correctamente.")
                    break
            else:
                overwrite = input(f"El archivo '{filename}' ya existe. Si no quiere sobreescribirlo escriba 'N': ")
                if overwrite.upper() == "N":
                    continue
                else:
                    root = ET.Element('test')
                    tree = ET.ElementTree(root)
                    with open(filename, 'wb') as f:
                        tree.write(f, encoding='utf-8', xml_declaration=True)
                    print(f"Fichero {filename} creado correctamente")
                    break
        else:
            print("Tiene que ser un archivo '.json' o '.xml'.")
            continue
    return filename


if __name__ == '__main__':
    create_test_file()
