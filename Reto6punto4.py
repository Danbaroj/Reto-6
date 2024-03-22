def vueltas (P, M, H, B):
    devolver = B - ((P*300)+(M*3300)+(H*350))
    return devolver

if __name__ == "__main__":
    P = int(input("Cuantos panes se mandaron a comprar: "))
    M = int(input("Cuantas bolsas de leche mandaron a comprar: "))
    H = int(input("Cuantos huevos mandaron a comprar: "))
    B = int(input("Cuanto dinero le dinero le dieron: "))
    dinero = vueltas (P, M, H, B)
    if dinero > 0: 
        print ("Te deberian dar de vueltas " + str(dinero) + " pesos")
    else:
        if dinero < 0: 
            debo = abs(dinero)
            print ("Deberias " + str(debo) + " pesos")