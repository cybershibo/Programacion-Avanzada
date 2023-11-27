#%%
# Armando Payán Angulo #18170732

'''
EJERCICIOS UNIDAD 4

Ejercicio: Realizar una busqueda de valores columna 3, con dos condiciones:
datos de temperatura >= 30 y <= 31
'''

import numpy as np
from matplotlib import pyplot as plt

datos = np.loadtxt("C:\\Users\\tarea\\Downloads\\3dic2016.txt", delimiter=' ', skiprows=1, usecols=(1, 2, 3, 4), dtype=float)

condicion = (datos[:, 3] >= 30) & (datos[:, 3] <= 31)
valores_filtrados = datos[condicion]
print(valores_filtrados)

#%%
'''
Ejercicio 1:

Eje X: numero de punto.
Eje Y: temperatura.
annotate: el ultimo punto de la grafica (azul).
texto: el valor de la temperatura maxima y minima.
axvspan: seleccionar un color HTML de su gusto y que represente 
el rango de temperatura mayor.
grid: puntos en color gris.
guardar el plot: en formato png, con dpi = 1200
'''
import numpy as np
from matplotlib import pyplot as plt

datos = np.loadtxt("C:\\Users\\tarea\\Downloads\\3dic2016.txt", delimiter=' ', skiprows=1, usecols=(1, 2, 3, 4), dtype=float)

condicion = (datos[:, 3] >= 30) & (datos[:, 3] <= 31)
valores_filtrados = datos[condicion]


temp_maxima = np.max(valores_filtrados[:, 3])
temp_minima = np.min(valores_filtrados[:, 3])

x = np.arange(len(valores_filtrados))
y = valores_filtrados[:, 3]

plt.plot(x, y, 'b-')


plt.annotate('Último punto', xy=(x[-1], y[-1]), xytext=(x[-1] - 5, y[-1] + 1), arrowprops=dict(facecolor='black', shrink=0.05))

plt.text(x[-1], temp_maxima, f'Máxima: {temp_maxima}', ha='right', va='bottom')
plt.text(x[-1], temp_minima, f'Mínima: {temp_minima}', ha='right', va='top')

plt.axvspan(xmin=x[0], xmax=x[-1], color='cyan', alpha=0.5)


plt.grid(color='gray', linestyle='--', linewidth=0.5)

plt.title("Temperaturas filtradas")
plt.xlabel("Número de punto")
plt.ylabel("Temperatura (ºC)")

plt.savefig("C:\\Users\\tarea\\Downloads\\3dic2016.png", dpi=1200)
plt.show()
# %%
'''
Ejercicio 2: Criterios de busqueda:
temp < 23
temp > 35
humedad < 40
humedad > 60
rango temp >= 30 y <=31
Extraer los datos de intereses, concatenarlos y guardarlos 
 en un archivo [resultado: 1 archivo].
'''

import numpy as np

datos = np.loadtxt("C:\\Users\\tarea\\Downloads\\3dic2016.txt", delimiter=' ', skiprows=1, usecols=(0, 1, 2, 3), dtype=float)

condicion = ((datos[:, 3] < 23) |
             (datos[:, 3] > 35) |
             (datos[:, 2] < 40) |
             (datos[:, 2] > 60) |
             ((datos[:, 3] >= 30) & (datos[:, 3] <= 31)))

datos_filtrados = datos[condicion]

np.savetxt("C:\\Users\\tarea\\Downloads\\datos_filtrados.txt", datos_filtrados, delimiter=' ', fmt='%1.6f %1.6f %1.6f %1.6f')

# %%

'''
EJERCICIO 4:
HACER UN PROGRAMA DONDE SE DEFINAN 2 CLASES: PAIS1 Y PAIS2 (DEFINIR NOMBRE),
DONDE CADA CLASE DEBERÁ TENER 3 METODOS: CAPITAL, IDIOMA Y MONEDA; CADA METODO
DEBERÁ IMPRIMIR SU PROPIO MENSAJE EN CONSOLA DEPENDIENDO DE SU CONTEXTO.
FINALMENTE, UTILIZAR UN CICLO "FOR" PARA MOSTRAR LOS MENSAJES DE AMBAS CLASES.

'''

class mexico:
    def capital(self):
        print('La capital es Ciudad de Mexico')
    def idioma(self):
        print('El idioma es el Español')
    def moneda(self):
        print('La moneda son los Pesos mexicanos')
class EUA:
    def capital(self):
        print('La capital es Washington D. C.')
    def idioma(self):
        print('el idioma es el Ingles')
    def moneda(self):
        print('la moneda es el Dolar')

for object in mexico(),EUA():
    object.capital()
    object.idioma()
    object.moneda()

# %%

'''
Ejercicio 5:

Hacer un programa donde se implementen clases y polimorfismo como sigue:

Clase base: Poligono -> Metodos abstractos: Area y perimetro
Clases sec: Triangulo, pentagono, hexagono, trapecio, mixto

Las clases sec deberan calcular el area y perimetro de cada una de las
figuras (usando los metodos abstractos). La clase "MIXTO" a traves
de un metodo debera reconocer cualquiera de las figuras anteriores.
finalmente, llamar los metodos e imprimir los resultados en consola.

obj1 = mixto()
obj1.todas_figuras(3, 5, 7) #Triangulo
obj1.todas_figuras(1, 2, 3, 4) #Trapecio
obj1.todas_figuras(1, 2, 3, 4, 5) #Pentagono
obj1.todas_figuras(1, 2, 3, 4, 5, 6) #Hexagono

TRIANGULO:
AREA: BASE X ALTURA / 2
PER: LADO + LADO + LADO

PENTAGONO Y HEXAGONO:
AREA: PERIMETRO X APOTEMA / 2
PER: LADO + LADO + LADO + LADO + LADO

TRAPECIO:
AREA: AREA (B + b / 2) * h
PER: LADO + LADO + LADO + LADO

'''

from abc import ABC, abstractmethod
import numpy as np


class poligono(ABC):
    @abstractmethod
    def todas_figuras(self,*args):
            pass
          
       
class mixto(poligono):
    def todas_figuras(self,*args):
        
        self.vector= np.asarray(args,dtype=int).flatten()
        self.n_lados=len(self.vector)
        area=0
        per=0
        if self.n_lados == 3:
            base=float(input('ingrese la base: '))
            altura=float(input('ingrese la altura: '))
            area=base*altura/2
            per=sum(self.vector)
            print('Triangulo')
            print(f'el area es= {area}')
            print(f'el perimetro es= {per}\n')
        elif self.n_lados == 5 or self.n_lados == 6:
            per=sum(self.vector)
            apotema=float(input('ingrese la apotema: '))
            area=per*apotema/2
            if self.n_lados==5:
                print('pentagono')
            else:
                print('hexagono')
            print(f'el area es= {area}')
            print(f'el perimetro es= {per}\n')
            
        elif self.n_lados == 4:
            b=float(input('ingrese b: '))
            B=float(input('ingrese B: '))
            h=float(input('ingrese h: '))
            per=sum(self.vector)
            area=  (B+b/2)*h
            print('trapacio')
            print(f'el area es = {area}')
            print(f'el perimetro es = {per}\n')
        else:
            print('No esta la figura en la base de datos')
obj=mixto()
obj.todas_figuras(1,2,3)
obj.todas_figuras(1,2,3,4)
obj.todas_figuras(1,2,3,4,5)
obj.todas_figuras(1,2,3,4,5,6)
# %%


