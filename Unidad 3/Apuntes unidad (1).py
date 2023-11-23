#%%
# UNIDAD 3 APUNTES
# Payan Angulo Armando 18170732

class principal:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def metodo_principal(self):
        print("Soy el método de la clase principal")

objeto_principal = principal(1, 2, 3)
print(objeto_principal.x)
print(objeto_principal.y)
print(objeto_principal.z)
objeto_principal.metodo_principal()

# Caso 1: Heredan todos los atributos y todos los métodos

class secundaria1(principal):
    def metodo_secundaria1(self):
        print("Soy el método del caso 1")

objeto_secundario1 = secundaria1(4, 5, 6)
print(objeto_secundario1.x)
print(objeto_secundario1.y)
print(objeto_secundario1.z)
objeto_secundario1.metodo_principal()
objeto_secundario1.metodo_secundaria1()

# Caso 2: Heredan todos los métodos y todos los atributos 
# pero además se agregan otros nuevos.

class secundaria2(principal):
    def __init__(self, x, y, z, w):
        super().__init__(x, y, z)
        self.w = w

    def metodo_secundario2(self):
        print("Soy el método del caso 2")

objeto_secundario2 = secundaria2(1, 2, 3, 4)
print(objeto_secundario2.x)
print(objeto_secundario2.y)
print(objeto_secundario2.z)
print(objeto_secundario2.w)
objeto_secundario2.metodo_principal()
objeto_secundario2.metodo_secundario2()

# Caso 3: Heredan todos los métodos y todos los atributos pero además 
# se agregan otros nuevos.

class secundaria3(principal):
    def __init__(self, x, y, z, w):
        super().__init__(x, y, z)
        self.w = w

    def metodo_secundario3(self):
        print("Soy el método del caso 3")

objeto_secundario3 = secundaria3(7, 8, 9, 10)
print(objeto_secundario3.x)
print(objeto_secundario3.y)
print(objeto_secundario3.z)
print(objeto_secundario3.w)
objeto_secundario3.metodo_principal()
objeto_secundario3.metodo_secundario3()


#%%

import numpy as np

class ejemplo_matriz:
    def __init__(self, matriz):
        self.mat = matriz
    
    def llena_matriz(self):
        filas = self.mat.shape[0]
        columnas = self.mat.shape[1]

        for i in range(filas):
            for j in range(columnas):
                self.mat[i][j] = int(input(f"MAT[{i}][{j}]:"))

        for i in range(filas):
            for j in range(columnas):
                print(f"MAT [{i}][{j}]: {self.mat[i][j]}") 
        
        return self.mat

filas = int(input("Ingrese las filas: "))
columnas = int(input("Ingrese el número de columnas: "))
matriz1 = np.zeros((filas, columnas)) 
objeto1 = ejemplo_matriz(matriz1)
matriz1 = objeto1.llena_matriz()  

# %%

import numpy as np

class ejemplo_matriz:
    def __init__(self, matriz):
        self.mat = matriz
    
    def llena_matriz(self):
        filas = self.mat.shape[0]
        columnas = self.mat.shape[1]

        for i in range(filas):
            for j in range(columnas):
                self.mat[i][j] = int(input(f"MAT[{i}][{j}]:"))

        for i in range(filas):
            for j in range(columnas):
                print(f"MAT [{i}][{j}]: {self.mat[i][j]}")

        return self.mat

matriz1 = np.zeros((4, 5))
objeto1 = ejemplo_matriz(matriz1)
matriz1 = objeto1.llena_matriz()

x1 = matriz1[2, 3]  # Acceder a un solo valor
x2 = matriz1[1, :]   # Acceder a una fila con todas las columnas
x3 = matriz1[:, 0]   # Acceder a una columna con todas las filas
x4 = matriz1[1:3, 0] # Acceder a un rango de filas con una columna
x5 = matriz1[1:3, 3:5] # Acceder a un subconjunto de la matriz

# %%
class b1:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def met1(self):
        print(f"Metodo 1: {self.a} {self.b}")

class b2:
    def __init__(self, c, d):
        self.c = c
        self.d = d
    
    def met2(self):
        print(f"Metodo 2: {self.c} {self.d}")

class multiple(b1, b2):
    def __init__(self, a, b, c, d, z):
        b1.__init__(self, a, b)
        b2.__init__(self, c, d)
        self.z = z
    
    def met3(self):
        print(f"{self.a} {self.b} {self.c} {self.d} {self.z}")

objeto_multiple = multiple(1, 2, 3, 4, 5)
objeto_multiple.met1()
objeto_multiple.met2()
objeto_multiple.met3()


#%%

 #Herencia Multinivel
class b1:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def met1(self):
        print(f"Metodo 1: {self.a} {self.b}")

class b2:
    def __init__(self, c, d):
        self.c = c
        self.d = d
    
    def met2(self):
        print(f"Metodo 2: {self.c} {self.d}")

class multiple(b1, b2):
    def __init__(self, a, b, c, d, z):
        b1.__init__(self, a, b)
        b2.__init__(self, c, d)
        self.z = z
    
    def met3(self):
        print(f"{self.a} {self.b} {self.c} {self.d} {self.z}")

objeto_multiple = multiple(1, 2, 3, 4, 5)
objeto_multiple.met1()
objeto_multiple.met2()
objeto_multiple.met3()
   
# %%
