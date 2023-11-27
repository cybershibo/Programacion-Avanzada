#%%
#UNIDAD 4 APUNTES
# Armando Payán Angulo #18170732

#Archivos y Manejo de Archivos

import numpy as np
from matplotlib import pyplot as plt

datos = np.loadtxt('D:\\Ago-Dic 23\\Progra Avanzada\\3dic2016.txt', delimiter = (skiprows=1, usecols=(1, 2, 3, 4), dtype=float)')

datos = np.where(datos[:,3] >= 30)

#%%
import numpy as np

datos = np.loadtxt('D:\\Ago-Dic 23\\Progra Avanzada\\3dic2016.txt', delimiter=',', skiprows=1, usecols=(0, 1, 2, 3), dtype=float)

criterios = (
    (datos[:, 1] < 23)
    (datos[:, 1] > 35)
    (datos[:, 2] < 40)
    (datos[:, 2] > 60)
    ((datos[:, 3] >= 30) & (datos[:, 3] <= 31)))

datos_filtrados = datos[criterios]

np.savetxt('D:\\Ago-Dic 23\\Progra Avanzada\\datos_filtrados.txt', datos_filtrados, delimiter=',')

print(datos_filtrados)



#POLIMORFISMO

class universidad:
    def evaluaciones(self):
        print('la universidad realiza evaluaciones')
    
    def inscripciones(self):
        print('la universidad permite inscripciones')
    
class departamentos(universidad):
    
#%%
import numpy as np
from matplotlib import pyplot as plt

datos = np.loadtxt('D:\\Ago-Dic 23\\Progra Avanzada\\3dic2016.txt', delimiter=',', skiprows=1, usecols=(1, 2, 3, 4), dtype=float)

datos = datos[datos[:, 3] >= 30]

print(datos)


# %%

#POLIMORFISMO


class universidad:
    def metodo1(self):
        print ('la universidad realiza evaluaciones')
    
    def metodo2(self):
        print ('la universidad permite inscripciones')
        
    def metodo3(self):
        print ('la universidad permite inscripciones')
    
class departamentos(universidad):
    def metodo1(self):
        print ('los departamentos ofrecen materias')
    
    def metodo2(self):
        print ('los departamentos permite inscripciones')
        
    def metodo3(self):
        print ('la universidad permite inscripciones')
        
        
class estudiantes(universidad):
    def metodo1(self):
        print('los estudiantes pueden reprobar')
        
    def metodo2(self):
        print ('los estudiantes se inscriben en una carrera')
        
    def metodo3(self):
        print ('la universidad permite inscripciones')
    
    
objeto1=universidad()
objeto1.metodo1()
objeto1.metodo2()
objeto1.metodo3()

objeto2=departamentos()
objeto2.metodo1()
objeto2.metodo2()
objeto2.metodo3()

objeto3=estudiantes()
objeto3.metodo1()
objeto3.metodo2()
objeto3.metodo3()



for objeto in universidad(), departamentos(), estudiantes():
    objeto.metodo1()
    objeto.metodo2()
    objeto.metodo3()




# %%

'''
EJERCICIO 4:
HACER UN PROGRAMA DONDE SE DEFINAN 2 CLASES: PAIS1 Y PAIS2 (DEFINIR NOMBRE),
DONDE CADA CLASE DEBERÁ TENER 3 METODOS: CAPITAL, IDIOMA Y MONEDA; CADA METODO
DEBERÁ IMPRIMIR SU PROPIO MENSAJE EN CONSOLA DEPENDIENDO DE SU CONTEXTO.
FINALMENTE, UTILIZAR UN CICLO "FOR" PARA MOSTRAR LOS MENSAJES DE AMBAS CLASES.

'''

class pais1:
    
    capital1 = 'Ciudad de Mexico'
    idioma1 = 'Español'
    Moneda1 = 'Peso Mexicano'
    def capital(self):
        print('La capital de México es '{self.pais1})
    
    def idioma(self):
        print('El idioma de México es el español')
        
    def moneda(self):
        print('La moneda de México es el peso mexicano')

class pais2:
    def capital(self):
        print('La capital de Estados Unidos es Wasgington')
    
    def idioma(self):
        print('El idioma de Estados Unidos es el Inlgés')
        
    def moneda(self):
        print('La moneda de Estados Unidos es elñ Dolar')

pais1 = mexico()
pais2=EstadosUnidos()


for pais in mexico(), EstadosUnidos():
    pais.capital()
    pais.idioma()
    pais.moneda()



#%%
# CLASES Y METODOS ABSTRACTOS | AEGUMENTOS DINAMICOS

import numpy as np

class ejemplo_1:
    
    def suma_estatica(self, n1, n2, n3, n4):
        return n1 + n2 + n3 + n4
    
    
    def suma_dinamica(self, *args):
        vector1 = np.asarray(args, dtype=int).flatten()
        return sum(vector1)
    
objeto1 = ejemplo_1()
print (f'La suma de los valores es: {objeto1.suma_estatica(1, 2, 3, 4)}')

print (f'La suma dinamica es: {objeto1.suma_dinamica(1, 2, 3)}')

from abc import ABC, abstractmethod

class base(ABC):
    @abstractmethod
    def metodo1(self):
        print('hola')
    
    @abstractmethod
    def metodo2(self):
        print('como estas?')

class sec(base):
    def metodo1(self):
        super().metodo1()
        print('clase secundaria')
    
    def metodo2(self):  # Agregar el parámetro self
        print('metodo faltante')

obj1 = sec()
obj1.metodo1()
obj1.metodo2()


# %%

# Tipos y manejo de excepciones

# Tipos: (A) Integradas (B) Definidas (por el usuario o el programador)

class Clase1:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tipo = "Tipo1"
    
    def imprime_info(self):
        print(f"Nombre: {self.nombre}, Tipo: {self.tipo}")

class Clase2:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def imprime_info(self):
        print(f"Nombre: {self.nombre}, Tipo: {self.tipo}")

try:
    # En este bloque se escribe el código que se desea probar:
    Persona1 = Clase1("Jose")
    Persona2 = Clase2("Diego", "Mayor")
        
except Exception as e:
    # En este bloque se escribe el código que se ejecutará en caso de que surja algún error (excepción)
    import numpy as np
    print(f"Oye!!, se necesitan dos argumentos como mínimo para funcionar. Error: {e}")
    
else:
    # En este bloque se escribe el código que se ejecutará en caso de que no ocurra algún error:
    print(Persona1.nombre, Persona1.tipo, Persona2.nombre, Persona2.tipo)
    Persona1.imprime_info()
    Persona2.imprime_info()
    
finally:
    # En este bloque se escribe el código que se ejecutará si o si, sin importar qué suceda con los errores.
    print("¡Finalizado!")

        
        
#%%

dividendo = 5
divisor = 0

try:
    Cociente = dividendo/divisor

except:
    print("No se puede dividir entre 0")

#%%

try:
    archivo = open("C:\\Usuario\\mi_archivo_para_abrir.bin")
except (IOError, FileNotFoundError, NameError):
    print("Error al abrir el,archivo: Por favor revisar que el nombre sea correcto.")
except NameError:
    print("La variable no existe ")
except FileNotFoundError:
    print("Nombre incorrecto ")
else:
    if not(archivo.closed):
        archivo.close()

#%%

while True:
    try:
        x = int(input(f"Ingrese un valor entero >> "))
        break
    except ValueError:
        print("Por favor ingresa un numero entero, otro tipo no es permitido.")

# %%
