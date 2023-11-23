#%%

"""
VILLEGAS VEGA OSCAR GUILLERMO #18170798
PAYAN ANGULO ARMANDO          #18170732

ESCRIBA UN PROGRAMA QUE LEA UN ARCHIVO DE TEXTO [casg0160.20i] IMPLEMENTANDO CLASES Y METODOS
ABSTRACTOS, HERENCIA Y POLIMORFISMO. EL PROGRAMA DEBERÁ BUSCARN LA INFORMACIÓN 
(RECTÁNGULO ROJO) QUE SE MUESTRA A CONTINUACIÓN Y GRAFICAR LOS VALORES EXTRAIDOS. EL TOTAL DE
VALORES DEBERÁ SER UN VECTOR DE 54 ELEMENTOS Y EL GRAFICO DEBERÁ TENER LAS SIGUIENTES CARACTERISTICAS
- LINEA ROJA
- MALLA O GRID DE FONDO
- TITULO Y LEYENDA INDICANDO LO QUE SE ESTÁ GRAFICANDO (BIAS)
- AGREGAR SU NOMBRE EN EL GRÁFICO
- ETIQUETAS EN EJES X y Y
- FLECHA APUNTANDO EL VALOR MAXIMO ENCONTRADO
- ILUMINAR EL AREA CON LA MAYOR LONGITUD PSEUDOESTABLEEEE DE LA SERIE

"""

# %%
import numpy as np
from abc import ABC, abstractmethod
from matplotlib import pyplot as plt


class ClaseAbstracta(ABC):
    
    
    @abstractmethod
    def MetodoAbstracto(self):
       
        pass
class Texto():
    def __init__(self):
        self.txt=r"C:\Users\allen\Documents\Programacion avanzada\casg0160.20i"
        self.datos = np.loadtxt(self.txt,skiprows=24,usecols=(1),max_rows=54)
    
    def ejes(self):
        self.longitud = len(self.datos)
        self.maximo=max(self.datos)
        self.x=np.zeros(self.longitud)
        for i in range(self.longitud):
            self.x[i]=i            

class ClaseHeredera(Texto):
    def Usarplt(self):
        print("Vector de datos:", self.datos)
        plt.title("Examen Unidad 4",color='black')
        plt.plot(self.x,self.datos,color='red')
        plt.ylabel('Bias')
        plt.xlabel('Observacion')
        plt.grid(color = 'gray')
        plt.annotate('Valor Maximo', xy=(21,self.maximo),xytext=(25,9.1),arrowprops=dict())
        plt.text(-2, -11, 'Villegas Vega Oscar Guillermo')
        plt.text(-2, 12, 'Payan Angulo Armando')
        plt.axvspan(10, 21, color='violet', alpha=1, lw=1) 
        plt.legend( ('Bias',), loc = 'upper right')
        plt.show()
    
G1=ClaseHeredera()
G1.ejes()
G1.Usarplt()
# %%
