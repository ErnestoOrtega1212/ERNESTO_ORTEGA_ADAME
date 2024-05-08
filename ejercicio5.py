import math 
divisiones = 10000

cuarto_area = 0.0

acumulador = 0

for i in range(divisiones):
    acumulador += 1
    base_triangulo = float(acumulador)/float(divisiones)
    altura = math.sqrt(1 - base_triangulo * base_triangulo)
    base = 1/float(divisiones)
    cuarto_area += (1/divisiones) * altura


print("El cuarto de area es: ", cuarto_area)
pi = cuarto_area * 4

print("pi es igual a: ", pi)