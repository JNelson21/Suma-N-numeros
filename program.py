#Esta prueba recibe n cantidad de números los suma y regresando su resultado
# Reading a file and adding the numbers in the file.
import fileinput

suma = 0
es_entero = True

for line in fileinput.input(files = 'texto.txt'):
    number = float(line.strip()) # convertir el string a un número flotante

    suma += number
    es_entero = es_entero and number.is_integer # comprobar si el número es entero

if es_entero is True:
    print(int(suma)) # si la suma es entera, imprimir como entero
else:
    print(suma) # si la suma es decimal, imprimir como flotante