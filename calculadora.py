import re

def realizar_operaciones(expresion):
    operaciones = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '^': lambda x, y: x ** y
    }

    numeros = re.findall(r'\d+\.?\d*', expresion)
    operadores = re.findall(r'[\+\-\*\/\^]', expresion)

    if not numeros or not operadores:
        print("Error: Expresión matemática inválida.")
        return None

    resultado = float(numeros[0])
    for i in range(1, len(numeros)):
        operador = operadores[i - 1]
        numero = float(numeros[i])
        resultado = operaciones[operador](resultado, numero)

    return resultado

def evaluar_expresion(expresion):
    expresion = expresion.replace(' ', '')  
    parentesis_regex = re.compile(r'\([^()]+\)')
    while '(' in expresion:
        subexpresion = parentesis_regex.search(expresion).group()
        resultado_subexpresion = realizar_operaciones(subexpresion[1:-1])
        expresion = expresion.replace(subexpresion, str(resultado_subexpresion))
    return realizar_operaciones(expresion)

def main():
    while True:
        expresion = input('Ingrese la expresión matemática: ')
        resultado = evaluar_expresion(expresion)
        if resultado is not None:
            print("El resultado de la operación es:", resultado)

        continuar = input("¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()

