

def binario(numeros, numero_encontrar, bajo, alto):
    if bajo > alto:
        return False

        medio = (bajo + alto) / 2

        if numeros[medio] == numero_encontrar:
            return True

        elif numeros[medio] > numero_encontrar:
            return binario(numeros, numero_encontrar, bajo, medio - 1)
        else:
            return binario(numeros, numero_encontrar, medio +1, alto)



if __name__ =='__main__':
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

    numero_encontrar = int(input('Ingresa un numero: '))

    resultado = binario(numeros, numero_encontrar, 0, len(numeros) -1)

    if resultado is True:
        print('Si esta en la lista')
    else:
        print('No esta en la lista')