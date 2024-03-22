def interes_compuesto (c, i, n):
    int_comp = c * ((1+(i/100))**n)
    return int_comp

if __name__ == "__main__":
    c = float(input("¿De cuanto es el prestamo?: "))
    i = float(input("¿De cuanto es el porcentaje del interes?: "))
    n = float(input("¿Por cuantos meses: "))
    valor_int_comp= interes_compuesto(c, i, n)
    print("El interes compuesto es de " + str(valor_int_comp))