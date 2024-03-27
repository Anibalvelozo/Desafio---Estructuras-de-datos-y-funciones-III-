import preguntas as p


def verificar(alternativas, eleccion):
    # Convertir la elección a índice numérico
    letra_a_indice = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
    eleccion_index = letra_a_indice.get(eleccion, -1)

    # Verificar si la elección es válida
    if eleccion_index == -1:
        print("Opción no válida. Por favor, ingrese una letra válida (a, b, c o d).")
        return False

    # Verificar si la respuesta es correcta
    if alternativas[eleccion_index][1] == 1:
        print("Respuesta Correcta")
        return True
    else:
        print("Respuesta Incorrecta")
        return False


if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)
