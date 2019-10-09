import random

def run():
    numero_encontrado = False
    numero_random = random.randint(0, 20)
    
    
    while not numero_encontrado:
        numero = int(input('introduce un numero: '))

        if numero == numero_random:
            print('Felicidades!!! Encontraste el numero')
            numero_encontrado = True
        elif numero > numero_random:
            print('el numero es mas pequeño')
        else:
            print('el numero es mas grande')


if __name__=='__main__':
    run()