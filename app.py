import sys
import random
from typing import OrderedDict
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Ozel(QMainWindow):

    CANTIDAD = 0
    PRESICION = 0
    CANTIDADBITS = 0
    ARREGLOCANTIDADBITS = []
    ARREGLOCANTIDADALAZAR = []
    ARREGLOUNIDOS = []
    PROMEDIODESCENDENCIA = 0.0
    ARREGLODATOSDESCENDENCIA = []
    ARREGLODATOSDESCENDENCIAACEPTADA = []
    ARREGLORESULTADOCRUZE = []
    ARREGLOMUTACION = []

    def __init__(self):
        super().__init__()
        uic.loadUi("proyecto/ui2.ui", self)
        self.btn1.clicked.connect(self.calcularCantidad)
    
    def msj_consola(self):
        print("holaa")
    

    def calcularCantidad(self):
        inicio = self.inicioIntervalo.text() 
        final = self.finalIntervalo.text()
        if (int(inicio) < int(final)):
            self.CANTIDAD = int((int(final) - int(inicio)) / float(self.presicionText.text())+1)
            print(self.CANTIDAD)
            self.cantidadText.setText(str(self.CANTIDAD))
            self.calcularCantidadEnBits()
        else:
            print("error")

    def calcularCantidadEnBits(self):
        decimal = 0
        potencia = 0
        for x in range(self.CANTIDAD):
            decimal = 2 ** x
            if self.CANTIDAD <= decimal:
                print(str(decimal)+"aquiiii")
                self.cantidadBitsText.setText(str(x))
                self.CANTIDADBITS = x
                break
            potencia = x
        self.selecionDePoblacion()

    def selecionDePoblacion(self):
        for x in range(10):
            numeroBinario = ""
            for y in range(self.CANTIDADBITS):
                numero = random.randint(0,1)
                numeroBinario+=str(numero)
            self.ARREGLOCANTIDADBITS.append(numeroBinario)
                
        numero = 0
        for x in self.ARREGLOCANTIDADBITS:
            if numero <=4:
                self.ARREGLOCANTIDADALAZAR.append(self.ARREGLOCANTIDADBITS[numero])
            else:
                break
            numero+=1
        for x in self.ARREGLOCANTIDADALAZAR:
            print(x)
        self.cruza()
        pass


    def cruza(self):
        print("entro a cruza")
        self.PROMEDIODESCENDENCIA = (random.randint(1,100)/100)
        numero = 0
        numerov2 = 1
        while numero < len(self.ARREGLOCANTIDADALAZAR):
            binario = self.ARREGLOCANTIDADALAZAR[numero]
            while numerov2 < len(self.ARREGLOCANTIDADALAZAR):
                binario2 = self.ARREGLOCANTIDADALAZAR[numerov2]
                self.ARREGLOUNIDOS.append((binario,binario2,round(random.uniform(0.0,self.PROMEDIODESCENDENCIA),3),random.randint(1,self.CANTIDADBITS-1)))
                numerov2 += 1
            numero += 1
            numerov2 = numero + 1
        
        print("acabo el while anterior")
        print(self.PROMEDIODESCENDENCIA)
       # print((random.randint(0.0,self.PROMEDIODESCENDENCIA)/100))
        for x in self.ARREGLOUNIDOS:
            print(x)
        self.muta()
        #self.promedioDecendencia()


#selecion

    def promedioDecendencia(self):
        self.PROMEDIODESCENDENCIA = (random.randint(1,100)/100)

        for x in range(10):
            numeroAleatorio = (random.randint(1,100)/100)
            self.ARREGLODATOSDESCENDENCIA.append(numeroAleatorio)
        
        for x in self.ARREGLODATOSDESCENDENCIA:
            if float(x) <= float(self.PROMEDIODESCENDENCIA) and float(x)<=5.0:
                self.ARREGLODATOSDESCENDENCIAACEPTADA.append(x)
        
        for x in self.ARREGLODATOSDESCENDENCIAACEPTADA:
            print(x)

        pass

    
    #mutacion

    def muta(self):
        for x in self.ARREGLOUNIDOS:
            letra1 = x[0]
            letra2 = x[1]
            splitLetraCortada = letra1[0:x[3]]
            splitLetra2Cortada = letra2[0:x[3]]
            letraResultante = letra1[x[3]:]
            letraResultante2 = letra2[x[3]:]
            self.ARREGLORESULTADOCRUZE.append(((splitLetraCortada+letraResultante2),(self.binario_a_decimal(splitLetraCortada+letraResultante2)),(splitLetra2Cortada+letraResultante),(self.binario_a_decimal(splitLetra2Cortada+letraResultante))))

        print("mutacion")
        arregloAux = []
        for x in self.ARREGLORESULTADOCRUZE:
            print(x)
            arregloAux.append(x[1])
            arregloAux.append(x[3])
        
        print("ordenado")
        final_list = list(OrderedDict.fromkeys(arregloAux))
        final_list.sort()
        for x in final_list:
            print(x)
        pass

    def binario_a_decimal(self,numero_binario):
        numero_decimal = 0
        for posicion, digitio_string in enumerate(numero_binario[::-1]):
            numero_decimal += int(digitio_string) * 2 ** posicion
        
        return numero_decimal/100


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = Ozel()
    GUI.show()
    sys.exit(app.exec_())