#%%
'''
Alumno: Armando Payán Angulo
num. de control: 18170732

Realizar un programa donde usando herencia se resuelva la siguiente serie:

s=x+x^2/2!+x^3/3!+x^4/4!+x^5/5!+...+x^n/n!

'''

import math

class ecuacion:
    def __init__(self):
        pass
    def eslabon(self, x, n):
        self.x = x
        self.n = n
        xt = x ** (n+1)
        xf = math.factorial(n+1)
        return xt/xf
class captura(ecuacion):
    def __init__(self, x,n):
        ecuacion.__init__(self)
        self.x = x
        self.n = n
    def sumatoria(self):
        suma = 0
        for i in range(0, self.n+1):
            suma += self.eslabon(self.x, i)
        return suma
    def mostrar(self):
        self.sumatoria()
        print(f"El resultado de la sumatoria es: {self.sumatoria()}")

x = float(input("Ingrese el valor de x: "))
n = int(input("Ingrese el valor de n: "))

e1 = captura(x,n)
e1.mostrar()
# %%
