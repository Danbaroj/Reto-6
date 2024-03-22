import math

def area(b, a, r):
    area_rectangulo = b*a
    area_circulo = (r**2)*math.pi
    area_total = area_circulo + area_rectangulo
    return area_total

def perimetro (b, a ,r):
    perimetro_rectangulo = 2*b + 2*a 
    perimetro_circulo = 2*math.pi*r
    perimetro_total= perimetro_rectangulo + perimetro_circulo
    return perimetro_total

if __name__ == "__main__":
    b = float(input("Ingrese la base del rectangulo: "))
    a = float(input("Ingrese la altura del rectangulo: "))
    r = float(input("Ingrese el radio de los circulos: "))
    area = area(b, a, r)
    perimetro =  perimetro (a, b, r)
    print("El area de la figura es de " + str(area) + "y su area superficial es de " + str(perimetro))