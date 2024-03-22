# Reto-6
Desarrolle la mayoría de ejercicios en clase. Para cada punto cree un programa individual. Al finalizar suba todo a un repo y subalo al canal reto_6 en slack.

1. Dado la figura de la imagen, desarrolle:

<img src="https://i.postimg.cc/FRvCmpxx/image.png" alt="" width="400" height="auto"/></br>

+ Una función matemática para calcular el volumen y el área superficial.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

```python

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

```

2. Dado la figura de la imagen, desarrolle:

<img src="https://i.postimg.cc/1t4MrzsL/image.png" alt="" width="400" height="auto"/></br>

+ Una función matemática para calcular el área y el perimetro.
+ Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
+ Revise como utilizar el valor de `pi` usando *import math* y *math.pi*

```python
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
```
3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```python
def carnes ( N , M , K):
    carnes_cantidad = N*6 + M*7 + K*1  
    return carnes_cantidad

if __name__ == "__main__":
    N = int(input("Ingrese la cantidad de gallinas: "))
    M = int(input("Ingrese la cantidad de gallos: "))
    K = int(input("Ingrese la cantidad de pollitos: "))
    cantidad = carnes (N , M, K)
    print(" La cantidad de carne en aves es de " + str(cantidad))
```
4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a  3300 cada una y H huevos a  350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```python
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
```

5. Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

```python
def interes_compuesto (c, i, n):
    int_comp = c * ((1+(i/100))**n)
    return int_comp

if __name__ == "__main__":
    c = float(input("¿De cuanto es el prestamo?: "))
    i = float(input("¿De cuanto es el porcentaje del interes?: "))
    n = float(input("¿Por cuantos meses: "))
    valor_int_comp= interes_compuesto(c, i, n)
    print("El interes compuesto es de " + str(valor_int_comp))
```

6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

```python
def num_contagiados (D, C):
    contagiados = C * (2**D)
    return contagiados

if __name__ == "__main__":
    C = int(input("¿Cuantas personas hay contagiadas actualmente?: "))
    D = int(input("¿Cuantos días pasaran?: "))
    cantidad_contagiados = num_contagiados(D, C)
    print("La cantidad de personas que se contagiaran en " +str(D) + "será de " + str(cantidad_contagiados))
```

7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:
  + El promedio
  + La mediana 
  + El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
  + Ordenar los números de forma ascendente
  + Ordenar los números de forma descendente
  + La potencia del mayor número elevado al menor número
  + La raíz cúbica del menor número

```python
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

def potencia_mayor_numero_sobre_menor_num (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero,menor_numero,mayor_numero):
    if primer_numero<segundo_numero and primer_numero<tercer_numero and primer_numero<cuarto_numero and primer_numero<quinto_numero: 
        menor_numero = primer_numero
    elif segundo_numero<primer_numero and segundo_numero<tercer_numero and segundo_numero<cuarto_numero and segundo_numero<quinto_numero:
        menor_numero= segundo_numero
    elif tercer_numero<primer_numero and tercer_numero<segundo_numero and tercer_numero<cuarto_numero and tercer_numero<quinto_numero:
        menor_numero= tercer_numero
    elif cuarto_numero<primer_numero and cuarto_numero<segundo_numero and cuarto_numero<tercer_numero and cuarto_numero<quinto_numero:
        menor_numero= cuarto_numero
    elif quinto_numero<primer_numero and quinto_numero<segundo_numero and quinto_numero<tercer_numero and quinto_numero<cuarto_numero:
        menor_numero= quinto_numero
    
    if primer_numero>segundo_numero and primer_numero>tercer_numero and primer_numero>cuarto_numero and primer_numero>quinto_numero:
        mayor_numero= primer_numero
    elif segundo_numero>primer_numero and segundo_numero>tercer_numero and segundo_numero>cuarto_numero and segundo_numero>quinto_numero:
        mayor_numero= segundo_numero
    elif tercer_numero>primer_numero and tercer_numero>segundo_numero and tercer_numero>cuarto_numero and tercer_numero>quinto_numero:
        mayor_numero= tercer_numero
    elif cuarto_numero>primer_numero and cuarto_numero>segundo_numero and cuarto_numero>cuarto_numero and cuarto_numero>quinto_numero:
        mayor_numero= cuarto_numero
    elif quinto_numero>primer_numero and quinto_numero>segundo_numero and quinto_numero>cuarto_numero and quinto_numero>quinto_numero:
        mayor_numero= quinto_numero
    potencia = mayor_numero**menor_numero
    return potencia

def raiz_cubica_menor_numero(primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero,menor_numero,):
    if primer_numero<segundo_numero and primer_numero<tercer_numero and primer_numero<cuarto_numero and primer_numero<quinto_numero: 
        menor_numero = primer_numero
    elif segundo_numero<primer_numero and segundo_numero<tercer_numero and segundo_numero<cuarto_numero and segundo_numero<quinto_numero:
        menor_numero= segundo_numero
    elif tercer_numero<primer_numero and tercer_numero<segundo_numero and tercer_numero<cuarto_numero and tercer_numero<quinto_numero:
        menor_numero= tercer_numero
    elif cuarto_numero<primer_numero and cuarto_numero<segundo_numero and cuarto_numero<tercer_numero and cuarto_numero<quinto_numero:
        menor_numero= cuarto_numero
    elif quinto_numero<primer_numero and quinto_numero<segundo_numero and quinto_numero<tercer_numero and quinto_numero<cuarto_numero:
        menor_numero= quinto_numero
    raiz_cubica = menor_numero**(1/3)
    return raiz_cubica

if __name__ == "__main__":
    primer_numero= int(input("Ingrese su primer numero real: "))
    segundo_numero= int(input("Ingrese su segundo numero real: "))
    tercer_numero= int(input("Ingrese su Tercer numero real: "))
    cuarto_numero= int(input("Ingrese su Cuarto numero real: "))
    quinto_numero= int(input("Ingrese su Quinto numero real: "))
    mayor_num = int
    menor_num = int
    promedio_num = promedio(primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero )
    promedio_multi = promedio_multiplicativo(primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero)
    mayor_num = mayor_numero (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero)
    menor_num = menor_numero (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero)
    potencia = potencia_mayor_numero_sobre_menor_num (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero,menor_num,mayor_num)
    raiz = raiz_cubica_menor_numero (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero,menor_num)
    print("El promedio de los numeros ingresados es: " + str(promedio_num))
    print("El promedio multiplicativo de los numeros ingresados es: " + str(promedio_multi))
    print("Los numeros organizados de mayor a menor son: " + str(mayor_num))
    print("Los numeros organizados de menor a mayor son: " + str(menor_num))
    print(" La potencia del mayor numero elevado a el menor numero es: " + str(potencia))
    print(" La raiz cubica del menor numero es: " + str(raiz))
```
8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

```python
from Reto6punto7 import *

promed = promedio (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero)
promed_mult = promedio_multiplicativo (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero)
ord_men_may = mayor_numero (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero)
ord_may_men = menor_numero (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero)
poten_mayor_sobre_men = potencia_mayor_numero_sobre_menor_num (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero,menor,mayor)
raiz_cubica_menor = raiz_cubica_menor_numero (primer_numero,segundo_numero,tercer_numero,cuarto_numero,quinto_numero,menor)
```

9. Consultar qué es y cómo funciona *pip* en python.

El "pip" es el sistema de gestión de paquetes usado para instalar y administrar paquetes escritos en el lenguaje de programación Python y descargarlos en el dispositivo,proporcionando funcionalidades que van desde operaciones matemáticas hsata acceso a bases de datos, simplifica los procesos de instalacion y acctualización de paquetes, ademas de la gestion de dependencias entre ellos y para usarlo en la instalacion de un paquete se usa este comando:

```python
pip install package_name
```

10. Hacer un listado de módulos populares para python que se puedan instalar com *pip* y consultar cómo instalarlos.

Módulos populares para Python:

  - Keras
  - PyTorch
  - Matplotlib
  - Scikit-learn
  - TensorFlow
  - Numpy
  - Bokeh
  - Pandas
  - Seaborn
  - Flask

Para la instalacion de los modulos se hace uso del Simbolo del Sistema del computador, escribiendo sobre este:

```python
pir install <nombre_del_modulo>
```
