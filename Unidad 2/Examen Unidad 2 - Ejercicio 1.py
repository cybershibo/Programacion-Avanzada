'''
EXAMEN UNIDAD 2:

HACER UN PROGRAMA QUE CALULE EL AREA Y VOLUMEN DE UN TANQUE ELIPTICO. ASI MISMO,
EL ATRIBUTO EJE MAYOR DEBERA ESTAR PROTEGIDO Y SE DEBERA EMPLEAR UN CONSTRUCTOR
Y AL MENOS UNA SOBRECARGA DE OPERADORES. FINALEMNTE, SE DEBERA IMPRIMIR EL RESUILTADO
DEL AREA Y VOLUMEN EN CONSOLA
'''
#%%
import math

class tanque:
    def __init__(self, major_axis, minor_axis, height):
        self._major_axis = major_axis
        self.minor_axis = minor_axis
        self.height = height
    
    def area(self):
        return math.pi * (self._major_axis/2) * (self.minor_axis/2)
    
    def volume(self):
        return self.area() * self.height
    
    def __str__(self):
        return f"Eje mayor:{self._major_axis}\nEje menor:{self.minor_axis}\nAltura:{self.height}\n"

tank1 = tanque(10, 5, 20)

print(tank1)
print(f"Area del tanque: {round(tank1.area(),3)}") 
print(f"Volumen del tanque: {round(tank1.volume(),3)}")

# %%
