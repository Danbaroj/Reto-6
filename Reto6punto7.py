def promedio (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero):
    prom = (primer_numero+segundo_numero+tercer_numero+cuarto_numero+quinto_numero)/5
    return prom

def promedio_multiplicativo (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero):
    prom_multipli = (((primer_numero*segundo_numero*tercer_numero*cuarto_numero*quinto_numero)**(1/5)))
    return prom_multipli

def menor_numero (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero):
    numeros = [primer_numero, segundo_numero, tercer_numero, cuarto_numero, quinto_numero]
    orden_mayor_menor = sorted(numeros)
    return orden_mayor_menor

def mayor_numero (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero):
    numeros = [primer_numero, segundo_numero, tercer_numero, cuarto_numero, quinto_numero]
    orden_menor_mayor = sorted(numeros, reverse=True)
    return orden_menor_mayor

def potencia_mayor_numero_sobre_menor_num (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero,menor,mayor):
    if primer_numero<segundo_numero and primer_numero<tercer_numero and primer_numero<cuarto_numero and primer_numero<quinto_numero: 
        menor = primer_numero
    elif segundo_numero<primer_numero and segundo_numero<tercer_numero and segundo_numero<cuarto_numero and segundo_numero<quinto_numero:
        menor= segundo_numero
    elif tercer_numero<primer_numero and tercer_numero<segundo_numero and tercer_numero<cuarto_numero and tercer_numero<quinto_numero:
        menor= tercer_numero
    elif cuarto_numero<primer_numero and cuarto_numero<segundo_numero and cuarto_numero<tercer_numero and cuarto_numero<quinto_numero:
        menor= cuarto_numero
    elif quinto_numero<primer_numero and quinto_numero<segundo_numero and quinto_numero<tercer_numero and quinto_numero<cuarto_numero:
        menor= quinto_numero
    
    if primer_numero>segundo_numero and primer_numero>tercer_numero and primer_numero>cuarto_numero and primer_numero>quinto_numero:
        mayor= primer_numero
    elif segundo_numero>primer_numero and segundo_numero>tercer_numero and segundo_numero>cuarto_numero and segundo_numero>quinto_numero:
        mayor= segundo_numero
    elif tercer_numero>primer_numero and tercer_numero>segundo_numero and tercer_numero>cuarto_numero and tercer_numero>quinto_numero:
        mayor= tercer_numero
    elif cuarto_numero>primer_numero and cuarto_numero>segundo_numero and cuarto_numero>cuarto_numero and cuarto_numero>quinto_numero:
        mayor= cuarto_numero
    elif quinto_numero>primer_numero and quinto_numero>segundo_numero and quinto_numero>cuarto_numero and quinto_numero>quinto_numero:
        mayor= quinto_numero
    potencia = mayor**menor
    return potencia

def raiz_cubica_menor_numero(primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero,menor):
    if primer_numero<segundo_numero and primer_numero<tercer_numero and primer_numero<cuarto_numero and primer_numero<quinto_numero: 
        menor = primer_numero
    elif segundo_numero<primer_numero and segundo_numero<tercer_numero and segundo_numero<cuarto_numero and segundo_numero<quinto_numero:
        menor= segundo_numero
    elif tercer_numero<primer_numero and tercer_numero<segundo_numero and tercer_numero<cuarto_numero and tercer_numero<quinto_numero:
        menor= tercer_numero
    elif cuarto_numero<primer_numero and cuarto_numero<segundo_numero and cuarto_numero<tercer_numero and cuarto_numero<quinto_numero:
        menor= cuarto_numero
    elif quinto_numero<primer_numero and quinto_numero<segundo_numero and quinto_numero<tercer_numero and quinto_numero<cuarto_numero:
        menor= quinto_numero
    raiz_cuadrada = menor**(1/3)
    return raiz_cuadrada

if __name__ == "__main__":
    primer_numero= int(input("Ingrese su primer numero real: "))
    segundo_numero= int(input("Ingrese su segundo numero real: "))
    tercer_numero= int(input("Ingrese su Tercer numero real: "))
    cuarto_numero= int(input("Ingrese su Cuarto numero real: "))
    quinto_numero= int(input("Ingrese su Quinto numero real: "))
    mayor = int
    menor = int
    promedio_num = promedio(primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero )
    promedio_multi = promedio_multiplicativo(primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero)
    mayor = mayor_numero (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero)
    menor = menor_numero (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero)
    potencia = potencia_mayor_numero_sobre_menor_num (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero,menor,mayor)
    raiz = raiz_cubica_menor_numero (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero,menor)
    print("El promedio de los numeros ingresados es: " + str(promedio_num))
    print("El promedio multiplicativo de los numeros ingresados es: " + str(promedio_multi))
    print("Los numeros organizados de mayor a menor son: " + str(mayor))
    print("Los numeros organizados de menor a mayor son: " + str(menor))
    print(" La potencia del mayor numero elevado a el menor numero es: " + str(potencia))
    print(" La raiz cubica del menor numero es: " + str(raiz))