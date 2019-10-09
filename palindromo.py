


def palindro(palabra):
    letras_reves = []

    for letra in palabra:
        letras_reves.insert(0, letra)

    palabra_invertida = ''.join(letras_reves)

    if palabra_invertida == palabra:
        return True

    return False


if __name__=='__main__':
    palabra = str(input('Escribe una palbra: '))

    resultado = palindro(palabra)

    if resultado is True:
        print('{} si es un palindromo'.format(palabra) )
    else:
        print('{} no es un palindromo'.format(palabra))