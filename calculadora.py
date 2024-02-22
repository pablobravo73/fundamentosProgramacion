# import re

variables = {}

def realizar_operaciones(expresion):
    try:
        # Buscar y reemplazar variables por su valor
        for var in variables:
            expresion = expresion.replace(var, str(variables[var]))
        
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
            raise ValueError("Expresión matemática inválida.")

        resultado = float(numeros[0])
        for i in range(1, len(numeros)):
            operador = operadores[i - 1]
            numero = float(numeros[i])
            resultado = operaciones[operador](resultado, numero)

        return resultado
    
    except ZeroDivisionError:
        raise ZeroDivisionError("No se puede dividir entre cero.")
    except Exception as e:
        raise ValueError(str(e))

def evaluar_expresion(expresion):
    expresion = expresion.replace(' ', '')  
    while '(' in expresion:
        parentesis_regex = re.compile(r'\(([^()]*)\)')
        subexpresion = parentesis_regex.search(expresion).group(1)
        resultado_subexpresion = realizar_operaciones(subexpresion)
        expresion = expresion.replace(f'({subexpresion})', str(resultado_subexpresion))
    return realizar_operaciones(expresion)

def main():
    usar_variables = input("¿Planea utilizar variables? (s/n): ")
    if usar_variables.lower() == 's':
        while True:
            entrada = input('Ingrese la asignación de variable (variable = valor): ')
            variable, valor_expresion = entrada.split('=')
            variable = variable.strip()
            valor = valor_expresion.strip()
            
            if re.match(r'^-?\d+(\.\d+)?$', variable):
                print("El nombre de la variable no puede ser un número.")
                continue
            
            try:
                valor = evaluar_expresion(valor)
                variables[variable] = valor
            except ValueError as ve:
                print(f"Error: {ve}")
                continue
                
            continuar = input("¿Desea ingresar otra variable? (s/n): ")
            if continuar.lower() != 's':
                break
        
        while True:
            expresion = input('Ingrese la expresión matemática: ')
            try:
                resultado = evaluar_expresion(expresion)
                print("El resultado de la operación es:", resultado)
            except ValueError as ve:
                print(f"Error: {ve}")
            except ZeroDivisionError as zde:
                print(f"Error: {zde}")

            continuar = input("¿Desea realizar otra operación? (s/n): ")
            if continuar.lower() != 's':
                break
    else:
        while True:
            expresion = input('Ingrese la expresión matemática: ')
            try:
                resultado = evaluar_expresion(expresion)
                print("El resultado de la operación es:", resultado)
            except ValueError as ve:
                print(f"Error: {ve}")
            except ZeroDivisionError as zde:
                print(f"Error: {zde}")

            continuar = input("¿Desea realizar otra operación? (s/n): ")
            if continuar.lower() != 's':
                break

if __name__ == "__main__":
    main()
