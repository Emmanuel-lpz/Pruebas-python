import random


IMAGENES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''
        
        
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

PALABRAS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado',
    'chiforimpula',
    'lukitas'
]

def palabra_aleatoria():
    idx = random.randint(0, len(PALABRAS) -1)
    return PALABRAS[idx]


def tablero_juego(palabra_escondida, errores):
    print(IMAGENES[errores])
    print('')
    print(palabra_escondida)
    print('---- * ---- * ----- * ----- * -----')


def run():
    palabra = palabra_aleatoria()
    palabra_escondida = ['-'] * len(PALABRAS)
    errores = 0

    while True:
        tablero_juego(palabra_escondida, errores)
        conteo_letra = str(input('Escoge una letra: '))

        letra_indice = []
        for idx in range(len(palabra)):
            if palabra[idx] == conteo_letra:
                letra_indice.append(idx)

        if len(letra_indice) == 0:
            errores += 1
        else:
            for idx in letra_indice:
                palabra_escondida[idx] = conteo_letra

            letra_indice = []

if __name__ == '__main__':
    print("B I E N V E N I D O S  A  E L  A H O R C A D O ")
    run()