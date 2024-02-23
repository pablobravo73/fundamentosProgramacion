def validateNumber(num):
    try:
        num = int(num)
        if num >= 0:
            return num
        else:
            print(f'{num} no es válido, ingrese un número válido.')
            return None
    except ValueError:
        print(f'{num} no es un número válido.')
        return None

    
def numerosPrimos(min_value, max_value):
    ListNumbers=[]
    for i in range(min_value, max_value + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                ListNumbers.append(i)
    return ListNumbers

def requireNumbers():
    min_value = validateNumber(input('Ingrese el número menor del rango: '))
    max_value = validateNumber(input('Ingrese el número mayor del rango: '))

    if min_value is not None and max_value is not None:
        return numerosPrimos(min_value, max_value)
    else:
        return None

if __name__ == '__main__':
    result = requireNumbers()
    if result is not None:
        print(result)
    else:
        print('Solicitud incorrecta.')
