#%%
# UNIDAD 3 EJERCICIOS
# Payan Angulo Armando 18170732
'''
 Ejercicio 1:
Aplicar el concepto de herencia a traves de un esquema donde la clase
principal "ave" va a heredar otras tres clases "Ganso", "Pato"
y "gallina" las cuales deberan tener tres atributos y dos metodos
'''


class Ave:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def volar(self):
        print(f"{self.nombre} está volando")

    def sonido(self):
        print(f"{self.nombre} hace un sonido de ave")

class Ganso(Ave):
    def __init__(self, nombre, edad, color, tamaño_cuello):
        super().__init__(nombre, edad, color)
        self.tamaño_cuello = tamaño_cuello

    def sonido(self):
        print(f"{self.nombre} gira su cuello ")

class Pato(Ave):
    def __init__(self, nombre, edad, color, tamaño_pico):
        super().__init__(nombre, edad, color)
        self.tamaño_pico = tamaño_pico

    def sonido(self):
        print(f"{self.nombre} hace un ruido de pato")

class Gallina(Ave):
    def __init__(self, nombre, edad, color, numero_huevos):
        super().__init__(nombre, edad, color)
        self.numero_huevos = numero_huevos

    def sonido(self):
        print(f"{self.nombre} hace un sonido de gallina")

ganso = Ganso("Ganso", 3, "blanco", "largo")
pato = Pato("Pato", 2, "verde", "corto")
gallina = Gallina("Gallina", 1, "roja", 5)
ganso.volar()
ganso.sonido()
print(f"El cuello del ganso es {ganso.tamaño_cuello}")
pato.volar()
pato.sonido()
print(f"El pico del pato es {pato.tamaño_pico}")
gallina.volar()
gallina.sonido()
print(f"La gallina pone {gallina.numero_huevos} huevos")





#%%
'''
Ejercicio 2:
Realizar un programa que reciba por consola una matriz de datos
(De un orden definido) y me diga si se trata de una matriz identidad.
'''
def matriz_identidad(matriz):
    n = len(matriz)
    if n != len(matriz[0]):
        return False

    for i in range(n):
        for j in range(n):
            if i == j and matriz[i][j] != 1:
                return False
            elif i != j and matriz[i][j] != 0:
                return False

    return True

def matriz():
    orden = int(input("Ingrese el orden de la matriz: "))
    
    matriz = []
    for i in range(orden):
        fila = []
        for j in range(orden):
            elemento = int(input(f"Ingrese el valor para MAT[{i+1}][{j+1}]: "))
            fila.append(elemento)
        matriz.append(fila)

    if matriz_identidad(matriz):
        print("La matriz es una matriz identidad.")
    else:
        print("La matriz no es una matriz identidad.")

if __name__ == "__main__":
    matriz()


#%%
'''
Ejercicio 3:
Escribir un programa que reciba una matriz de 4 x 4. Si la sumatoria
de cada una de las columnas es mayor a la sumatoria de cada una
de las filas, entonces se debera concatenar horizontalmente otra
matriz del mismo orden donde cada elemento sera el resultado
de la sumatoria. Ademas, la ultima columna debera ser el resultado
de la fila. Caso contrario, la concatenacion sera vertical y la ultima
fila debera ser el resultado de las columnas.
Nota: Usar herencia simple.


 | 1 1 2 1 | -> 5    col_max = 0    si col_max > fil_max      si fil_max > col_max
 | 2 1 2 1 | -> 6    fil_max = 8    |col col col fil |        |fil fil fil fil |
 | 3 1 2 1 | -> 7                   |col col col fil |        |fil fil fil fil |
 | 4 1 2 1 | -> 8                   |col col col fil |        |fil fil fil fil |
 ___________                        |col col col fil |        |col col col col |
  10 4 8 4                          concat.Horizontal         concat.Vertical
'''
class MatrizResultante(Matriz):
    def __init__(self, orden, filas, columnas):
        super().__init__(orden)
        self.sumas_filas = filas
        self.sumas_columnas = columnas
        self.construir_matriz_resultante()

    def construir_matriz_resultante(self):
        if max(self.sumas_columnas) > max(self.sumas_filas):
            for i in range(self.orden):
                fila_resultante = self.matriz[i] + [self.sumas_filas[i]]
                self.matriz[i] = fila_resultante
            self.matriz[-1] = self.sumas_columnas  
        else:
            matriz_resultante = self.matriz + [self.sumas_columnas] + [self.sumas_filas]
            self.matriz = matriz_resultante

def main():
    orden = 4
    print("Ingrese la matriz original:")
    matriz_original = Matriz(orden)
    matriz_original.ingresar_matriz()

    filas = matriz_original.sumar_filas()
    columnas = matriz_original.sumar_columnas()

    matriz_original.imprimir_matriz()
    print("Suma de filas:", filas)
    print("Suma de columnas:", columnas)

    matriz_resultante = MatrizResultante(orden, filas, columnas)

    print("\nMatriz Resultante:")
    matriz_resultante.imprimir_matriz()

if __name__ == "__main__":
    main()

#%%
'''
Ejercicio 4:
Escribir un programa que aplique herencia multinivel mediante
la siguiente estructura:
    
    {Articulo} ------ video, audio, altavoces
    {Audio}---------- Radio, Cassete, CD, Amplificador.

La clase padre debera tener al menos 2 atributos y cada clase
hija debera agregar al menos 1 atributo nuevo. Ademas, todas las 
clases deberan tener un metodo que imprima la informacion de 
los atributos.
Finalmente: Instanciar un objeto por cada clase hija y llamar
los metodos. Los atributos deberan llamarse en funcion de la 
clase donde se encuentran.
        Total de clases = 8
        Total de objetos = 7
'''        
class Articulo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio}")


class Audio(Articulo):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo

    def info(self):
        super().info()
        print(f"Tipo de audio: {self.tipo}")


class Radio(Audio):
    def __init__(self, nombre, precio, tipo, marca):
        super().__init__(nombre, precio, tipo)
        self.marca = marca

    def info(self):
        super().info()
        print(f"Marca: {self.marca}")


class Cassette(Audio):
    def __init__(self, nombre, precio, tipo, duracion):
        super().__init__(nombre, precio, tipo)
        self.duracion = duracion

    def info(self):
        super().info()
        print(f"Duración: {self.duracion} minutos")


class CD(Audio):
    def __init__(self, nombre, precio, tipo, capacidad):
        super().__init__(nombre, precio, tipo)
        self.capacidad = capacidad

    def info(self):
        super().info()
        print(f"Capacidad: {self.capacidad} MB")


class Amplificador(Audio):
    def __init__(self, nombre, precio, tipo, potencia):
        super().__init__(nombre, precio, tipo)
        self.potencia = potencia

    def info(self):
        super().info()
        print(f"Potencia: {self.potencia} watts")


class Video(Articulo):
    def __init__(self, nombre, precio, resolucion):
        super().__init__(nombre, precio)
        self.resolucion = resolucion

    def info(self):
        super().info()
        print(f"Resolución: {self.resolucion}")


class Altavoces(Articulo):
    def __init__(self, nombre, precio, potencia):
        super().__init__(nombre, precio)
        self.potencia = potencia

    def info(self):
        super().info()
        print(f"Potencia de salida: {self.potencia} watts")


articulo = Articulo("Artículo genérico", 100)
radio = Radio("Radio", 50, "Radio FM", "Sony")
cassette = Cassette("Cassette Player", 30, "Reproductor de casets", 60)
cd = CD("Reproductor de CD", 40, "Reproductor de CD", 700)
amplificador = Amplificador("Amplificador de audio", 80, "Amplificador estéreo", 100)
video = Video("Televisor LED", 300, "1920x1080")
altavoces = Altavoces("Altavoces 2.1", 70, 20)
print("Información del artículo:")
articulo.info()
print("\nInformación del radio:")
radio.info()
print("\nInformación del reproductor de casets:")
cassette.info()
print("\nInformación del reproductor de CD:")
cd.info()
print("\nInformación del amplificador:")
amplificador.info()
print("\nInformación del televisor:")
video.info()
print("\nInformación de los altavoces:")
altavoces.info()


        
        
#%%

'''
Ejercicio 5:  

Modificar el ejemplo anterior de modo que se utilice herencia
multiple donde ambas clases padre contengan al menos un atributo
protegido. La clase hija debera contener todos los atributos
de las clases base e imprimir en un metodo la informacion de 
los atributos heredados.
Nota: Agregar nombre a cada atributo
'''

class Articulo:
    def __init__(self, nombre_articulo, precio_articulo):
        self._nombre_articulo = nombre_articulo
        self._precio_articulo = precio_articulo

    def info(self):
        print(f"Nombre del artículo: {self._nombre_articulo}")
        print(f"Precio del artículo: ${self._precio_articulo}")


class Audio:
    def __init__(self, tipo_audio):
        self._tipo_audio = tipo_audio

    def info(self):
        print(f"Tipo de audio: {self._tipo_audio}")


class Radio(Articulo, Audio):
    def __init__(self, nombre_articulo, precio_articulo, tipo_audio, marca_radio):
        Articulo.__init__(self, nombre_articulo, precio_articulo)
        Audio.__init__(self, tipo_audio)
        self._marca_radio = marca_radio

    def info(self):
        Articulo.info(self)
        Audio.info(self)
        print(f"Marca del radio: {self._marca_radio}")


radio = Radio("Radio FM", 50, "Receptor FM", "Sony")

radio.info()


# %%
