def num_contagiados (D, C):
    contagiados = C * (2**D)
    return contagiados

if __name__ == "__main__":
    C = int(input("¿Cuantas personas hay contagiadas actualmente?: "))
    D = int(input("¿Cuantos días pasaran?: "))
    cantidad_contagiados = num_contagiados(D, C)
    print("La cantidad de personas que se contagiaran en " +str(D) + "será de " + str(cantidad_contagiados))