'''
EXAMEN UNIDAD 2: EJERCICIO 2

RESUELVA UN SISTEMA DE ECUACIONES LINEALES DE 2X2 A PARTIR DE  LOS
COEFICIENTES DADOS, EMPLEANDO UN CONSTRUCTOR Y AL MENOS UNA 
SOBRECARGA DE OPERADOR, ADEMAS LOS OBJETOS DEBEN SER DESTRUIDOS EMPLEANDO
UN DESTRUCTOR DESPUES DE IMPRIMIR EL RESULTADO EN CONSOLA

'''	

#%%
class SistemaEcuaciones:
    def __init__(self, a1, b1, c1, a2, b2, c2):
        self.a1 = a1 #c1
        self.b1 = b1 #c2
        self.c1 = c1 #b1
        self.a2 = a2 #c3
        self.b2 = b2 #c4
        self.c2 = c2 #b2

    def resolver(self):
        determinant = self.a1 * self.b2 - self.a2 * self.b1
        ds = (self.a1*self.b2) - (self.b1*self.a2)
        dx = (self.c1*self.b2) - (self.b1*self.c2)
        dy = (self.a1*self.c2) - (self.c1*self.a2)

        xalt = dx/ds 
        yalt = dy/ds

        if determinant == 0:
            return "El sistema no tiene solución única."
        else:
            x = (self.c1 * self.b2 - self.c2 * self.b1) / determinant
            y = (self.a1 * self.c2 - self.a2 * self.c1) / determinant
            return x, y, xalt, yalt

    def __str__(self):
        return f"Sistema de ecuaciones lineales:\n{self.a1}x {self.b1}y = {self.c1}\n{self.a2}x {self.b2}y = {self.c2}"

    def __del__(self):
        print("Destructor llamado. Objeto SistemaEcuaciones destruido.")

# Entrada de coeficientes
a1 = float(8)
b1 = float(-5)
c1 = float(-5)
a2 = float(3)
b2 = float(-4)
c2 = float(13)

# Instanciar la clase SistemaEcuaciones
sistema = SistemaEcuaciones(a1, b1, c1, a2, b2, c2)

# Imprimir el sistema de ecuaciones
print(str(sistema))

# Resolver el sistema y mostrar la solución
x, y, xalt, yalt = sistema.resolver()
print(f"Solución del sistema: x = {x}, y = {y}, xalt = {xalt}, yalt = {yalt}")
del sistema
# %%
