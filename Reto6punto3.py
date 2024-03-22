def carnes ( N , M , K):
    carnes_cantidad = N*6 + M*7 + K*1  
    return carnes_cantidad

if __name__ == "__main__":
    N = int(input("Ingrese la cantidad de gallinas: "))
    M = int(input("Ingrese la cantidad de gallos: "))
    K = int(input("Ingrese la cantidad de pollitos: "))
    cantidad = carnes (N , M, K)
    print(" La cantidad de carne en aves es de " + str(cantidad))