


def promedio_temperaturas(temperaturas):
    suma_temps = 0

    for temperatura in temperaturas:
        suma_temps += temperatura

    return suma_temps / len(temperaturas)

if __name__ =='__main__':
    temperaturas = [22, 24, 24, 22, 20, 23, 24]
    
    promedio = promedio_temperaturas(temperaturas)

    print('La temperatura promedi es: {}'.format(promedio) )