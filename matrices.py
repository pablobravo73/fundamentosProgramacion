'''
Descripción: usando iteradores crear una lista que contenga una figura geométrica formada con espacios en blanco y el carácter.
Diseña una función que imprima en pantalla un arreglo de arreglos (matriz), que tenga un rombo del tamaño que el usuario desee 
en el momento de ejecutar el programa. La entrada del tamaño deberá ser solicitada por el programa al inicio de su ejecución.
'''

def UpWard(centro):
    for i in range(centro):
        for j in range(centro -i):
            print('   ',end='') 
        for j in range(2*i):
            print(' * ', end='')
        print(' * ') 

def DownWard(centro):
    for i in range(centro,-1,-1): 
        for j in range(centro -i):
            print('   ',end='') 
        for j in range(2*i): 
            print(' * ', end='')
        print(' * ') 


def printRhombus(centro):
    UpWard(centro)
    DownWard(centro)


if __name__=='__main__':
    try:
        size = int(input("Introduce el tamaño del rombo: "))
        centro = (size//2)
        if size % 2 == 0:
            raise ValueError("El tamaño del rombo debe ser impar")
        printRhombus(centro)
    except ValueError as ve:
        print("Error:", ve)


