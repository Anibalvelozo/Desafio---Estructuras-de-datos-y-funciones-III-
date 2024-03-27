import preguntas as p

def print_pregunta(enunciado, alternativas):
    
    # Imprimir enunciado y alternativas
    ###############################################################
    print(enunciado)
    print("Alternativas")
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for pos, alternativa in enumerate(alternativas):
        print(f'{letters[pos]}. {alternativa[0]}')
    
    
    
    ###############################################################
        
if __name__ == '__main__':
    # Las preguntas y alternativas deben mostrarse según lo indicado
    pregunta = p.pool_preguntas['basicas']['pregunta_1']
    print_pregunta(pregunta['enunciado'], pregunta['alternativas'])
