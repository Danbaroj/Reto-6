import math

def volumen_figura(r1,r2,h):
    volumen_esfera = (4/3)*math.pi*(r1**3)
    volumen_cono = (math.pi*(r2**2)*h)/3
    volumen_total = volumen_esfera+volumen_cono
    return volumen_total

def area_superficial_figura(r1,r2,h):
    area_superficial_esfera = 4*math.pi*(r1**2)
    area_superficial_cono = math.pi*(math.sqrt((h**2)+(r2**2)))*r2
    area_superficial_total = area_superficial_esfera + area_superficial_cono
    return area_superficial_total

if __name__ == "__main__":
    r1 = float(input("Ingrese el radio de la esfera: "))
    r2 = float(input("Ingrese el radio del cono: "))
    h = float(input("Ingrese la altura del cono: "))
    volumen = volumen_figura(r1, r2, h)
    area_superficial =  area_superficial_figura (r1, r2, h)
    print("El volumen de la figura es de " + str(volumen) + "y su area superficial es de " + str(area_superficial))