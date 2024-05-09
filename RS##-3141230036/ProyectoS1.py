import math
eleccion = ""

def CalculoRectangulo(b, h):
    return b * h

def CalculoTriangulo(b, h):
    return b * h / 2

def CalculoPi():
    acumulador = 0.0 
    contador = 0
    division_actual = 1.0
    essuma = True

    while division_actual > 0.000001:
        contador += 1
        division_actual = 1 / contador

        if contador % 2 != 0: 
            if essuma:
                acumulador += division_actual
            else: 
                 acumulador -= division_actual
            essuma = not essuma

    return acumulador * 4

def CalculoCirculo(r):
    return CalculoPi() * (r * r)
    

while eleccion != "d":
    print("Que deseas calcular el dia de hoy: ")
    print("a) Rectangulo")
    print("b) Triangulo")
    print("c) Circulo") 
    print("d) Salir") 
    eleccion = str(input())
    if eleccion == "a":
        print("Dame la base de tu rectangulo: ")
        b = float(input())
        print("Dame la altura de tu rectangulo: ")
        h = float(input())
        area_rectangulo = CalculoRectangulo(b, h)
        
        print("El area del rectangulo es: ", area_rectangulo)
    elif eleccion == "b":
        print("Dame la base del triangulo: ")
        b = float(input())
        print("Dame la altura del triangulo: ")
        h = float(input())
        area_triangulo = CalculoTriangulo(b, h)

        print("El area del triangulo es de : ", area_triangulo)
        
    elif eleccion == "c":
        print("Dame el radio de tu circulo: ")
        r = float(input())
        area_circulo = CalculoCirculo(r)

        print("El area de tu circulo es de: ", area_circulo)
        