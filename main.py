

from itertools import count
import sys
import random
from typing import OrderedDict
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication



import math

from matplotlib import pyplot
import cv2


class WindowView(QMainWindow):

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
    ARREGLORESULTADOFINAL = []
    ARREGLOXI = []
    ARREGLOFX = []
    ARREGLODATOSANTESPODA = []
    ARREGLOPROBABILIDADDESENDENCIA = []
    ARREGLOFINALGENERACION = []
    ARREGLO1 = []
    ARREGLO2 = []
    ARREGLOPORGENERACIONXY = []
    COUNT = 0
    OZELX = []
    OZELY = []
    ARREGLOGLOBALMAXIMO = []
    ARREGLOGLOBALMINIMO = []
    COUNTIMG = 0
    #idGeneracion

    def __init__(self):
        super().__init__()
        uic.loadUi("ui2.ui",self)
        self.btn1.clicked.connect(self.calcularCantidadSoluciones)
    

    def calcularCantidadSoluciones(self):
        self.limpiar()
        self.ARREGLOFINALGENERACION.clear()
        self.ARREGLOPORGENERACIONXY.clear()
        self.COUNTIMG = 0
        if len(self.idGeneracion.text())>0 and self.idGeneracion.text().isdigit() and len(self.inicioIntervalo.text()) >0 and self.inicioIntervalo.text().isdigit() and len(self.finalIntervalo.text()) > 0 and self.finalIntervalo.text().isdigit() and len(self.presicionText.text()) > 0 and len(self.idPoblacionInicial.text()) > 0 and self.idPoblacionInicial.text().isdigit() and len(self.idPoblacionMaxima.text()) > 0 and self.idPoblacionMaxima.text().isdigit() and len(self.idPromedio.text()) > 0  and len(self.idmutacionindividuo.text()) > 0 and len(self.idPMG.text()) > 0:
            try:
                float(self.presicionText.text())
                float(self.idPromedio.text())
                float(self.idmutacionindividuo.text())
                float(self.idPMG.text())
                self.msj_error.setText("")
                for x in range(0,int(self.idGeneracion.text())):
                    print("inicia generaciones"+ str(x))
                    inicio = self.inicioIntervalo.text() 
                    final = self.finalIntervalo.text()
                    if (int(inicio) < int(final)):
                        self.CANTIDAD = int((int(final) - int(inicio)) / float(self.presicionText.text())+1)
                        self.cantidadText.setText(str(self.CANTIDAD))
                        self.calcularCantidadEnBits()
                    else:
                        print("error")
                        break
                    self.limpiar()
                print("ARREGLOFINALGENERACION GRAFICAR")
                self.graficaHistorico()
                self.crearVideo()
            except ValueError:
                print("error")
                self.msj_error.setText("Error faltan campos por rellenar o campos invalidos")
        else:
            self.msj_error.setText("Error faltan campos por rellenar")

    def limpiar(self):
        self.CANTIDAD = 0
        self.PRESICION = 0
        self.CANTIDADBITS = 0
        self.ARREGLOCANTIDADBITS = []
        self.ARREGLOCANTIDADALAZAR = []
        self.ARREGLOUNIDOS = []
        self.PROMEDIODESCENDENCIA = 0.0
        self.ARREGLODATOSDESCENDENCIA = []
        self.ARREGLODATOSDESCENDENCIAACEPTADA = []
        self.ARREGLORESULTADOCRUZE = []
        self.ARREGLOMUTACION = []
        self.ARREGLORESULTADOFINAL = []
        self.ARREGLOXI = []
        self.ARREGLOFX = []
        self.ARREGLODATOSANTESPODA = []
        self.ARREGLOPROBABILIDADDESENDENCIA = []
        self.ARREGLO1 = []
        self.ARREGLO2 = []
        self.COUNT = 0
        self.OZELX = []
        self.OZELY = []
        self.ARREGLOGLOBALMAXIMO = []
        self.ARREGLOGLOBALMINIMO = []


    def calcularCantidadEnBits(self):
        decimal  = 0
        for x in range(self.CANTIDAD):
            decimal = 2 ** x
            if self.CANTIDAD <= decimal:
               
                self.cantidadBitsText.setText(str(x))
                self.CANTIDADBITS = x
                break
        self.representacionIndiviuo()
    #selecion

    def representacionIndiviuo(self):
        print("Representacion del Individuo")
        for x in range(int(self.idPoblacionInicial.text())):
            numeroBinario = ""
            for y in range(self.CANTIDADBITS):
                numero = random.randint(0,1)
                numeroBinario+=str(numero)
            self.ARREGLOCANTIDADBITS.append(numeroBinario)

        print(self.ARREGLOCANTIDADBITS)
        print("fin del indiviuo")
        self.selecionDePoblacionv2()
        pass

    def selecionDePoblacion(self):  
        print("selecion de poblacion")   
        numero = 0
        print(self.ARREGLOCANTIDADBITS)
        print("------------")
        for x in self.ARREGLOCANTIDADBITS:
            if numero <=4:
                self.ARREGLOCANTIDADALAZAR.append(self.ARREGLOCANTIDADBITS[numero])
            else:
                break
            numero+=1
        print(self.ARREGLOCANTIDADALAZAR)
        for x in self.ARREGLOCANTIDADALAZAR:
            self.ARREGLO1.append(x)
        #self.cruza()
        pass
    
    def selecionDePoblacionv2(self):
        print("Inicio de selecion")
        numero = 0
        numerov2 = 1
        while numero < len(self.ARREGLOCANTIDADBITS):
            binario = self.ARREGLOCANTIDADBITS[numero]
            while numerov2 < len(self.ARREGLOCANTIDADBITS):
                binario2 = self.ARREGLOCANTIDADBITS[numerov2]
                self.ARREGLOUNIDOS.append((binario,binario2,round(random.uniform(0,1),3),random.randint(1,self.CANTIDADBITS-1)))
                numerov2 += 1
            numero += 1
            numerov2 = numero + 1
        
        for x in self.ARREGLOUNIDOS:
            print(x)
        print("Terminacion de selecion")
        #self.ARREGLO2 = self.ARREGLOUNIDOS
        for x in self.ARREGLOUNIDOS:
            self.ARREGLO2.append(x)
        self.cruza()
        pass


    #cruza
    def cruza(self):
        print("Inicia Cruza")
        for x in self.ARREGLOUNIDOS:
            letra1 = x[0]
            letra2 = x[1]
            splitLetraCortada = letra1[0:x[3]]
            splitLetra2Cortada = letra2[0:x[3]]
            letraResultante = letra1[x[3]:]
            letraResultante2 = letra2[x[3]:]
            self.ARREGLORESULTADOCRUZE.append(((splitLetraCortada+letraResultante2),((random.randint(1,100))/100),(splitLetra2Cortada+letraResultante),((random.randint(1,100))/100)))
        arregloAux = []
        for x in self.ARREGLORESULTADOCRUZE:
            if x[1] <= float(self.idmutacionindividuo.text()):
                arregloAux.append((x[0],x[1]))
            if x[3] <= float(self.idmutacionindividuo.text()):
                arregloAux.append((x[2],x[3]))  
        
        print("Fin de cruza")
        self.verificarPromedioDesendencia()
        self.muta(arregloAux)

    def verificarPromedioDesendencia(self):
        print("promedio")
        print(self.idPromedio.text())
        for x in self.ARREGLOUNIDOS:
            if x[2] <= float(self.idPromedio.text()):
                self.ARREGLOPROBABILIDADDESENDENCIA.append(x)
    
    #mutacion
    def muta(self,final_list):
        print("Inicia Mutacion")
        lista_new_bin = []
        var_list = ""
        print("-----------")
        print("-----------")
        print(final_list)
        print("-----------")
        print("-----------")
        for x in final_list:
            binario = x[0]
            for y in binario:
                r = (random.randint(0,100))/100
                if r <= float(self.idPMG.text()):
                    if y == "0":
                        #lista_new_bin.append("1")
                        var_list+="1"
                    elif y == "1":
                        #lista_new_bin.append("0")
                        var_list+="0"
                else:
                    var_list+=y
                    #lista_new_bin.append(y)
            lista_new_bin.append(var_list)
            var_list=""
        
        print("Fin de mutacion")
        if len(lista_new_bin)>0:
            self.limpieza(lista_new_bin)

    def binario_a_decimal(self,numero_binario):
        numero_decimal = 0
        for posicion, digitio_string in enumerate(numero_binario[::-1]):
            numero_decimal += int(digitio_string) * 2 ** posicion
        
        return numero_decimal
    #Limpieza Mutacion

    #limpieza

    def limpieza(self,lista_new_bin):
        print("Inicio de limpieza")
        binario_a_decimal_number = []
        for x in lista_new_bin:
            if self.binario_a_decimal(x) <= (self.CANTIDAD-1):
                binario_a_decimal_number.append(self.binario_a_decimal(x))
        m = self.mejor(binario_a_decimal_number)
        p = self.peor(binario_a_decimal_number)
        pro = (m+p)/2
        self.ARREGLOFINALGENERACION.append((m,p,pro))
        print("Fin de limpieza")
        self.poda()
    
    def mejor(self,arreglo):
        max = arreglo[0]
        for x in arreglo:
            if x > max:
                max = x
        return max

    def peor(self,arreglo):
        min = arreglo[0]
        for x in arreglo:
            if x < min :
                min = x
        return min

    def promedio(m,p):
        return (m+p)/2
    
    #obtener mejor peor promedio por generacion
    #poda
    def poda(self):
        print("Inicio de poda")
        arregloUnido = []
        arregloUnido2 = []
        for x in self.ARREGLO1:
            arregloUnido.append((x,(random.randint(1,100)/100)))
        for x  in self.ARREGLO2:
            arregloUnido.append((x[0],(random.randint(1,100)/100)))
            arregloUnido.append((x[1],(random.randint(1,100)/100))) 

        pp = int(self.idPoblacionMaxima.text())/len(arregloUnido)
        for x in arregloUnido:
            if x[1] <= pp :
                arregloUnido2.append(x)
        print("Fin de Poda")
        self.transformar_binario_decimal(arregloUnido2)
        pass

    def transformar_binario_decimal(self,arreglo):
        print("transformar binario decimal")
        arreglo_decimales = []
        for x in arreglo:
            v = x[0]
            arreglo_decimales.append(self.binario_a_decimal(v))
        self.formula1(arreglo_decimales)
        self.formular2()
        print("valor de xi")
        for x in self.ARREGLOXI:
            self.OZELX.append(x)
        for x in self.ARREGLOFX:
            self.OZELY.append(x)
        
        #maximo
        if self.r1.isChecked():
            count = 0
            while count < len(self.OZELX):
                self.ARREGLOGLOBALMAXIMO.append((self.OZELX[count],self.OZELY[count]))
                count+=1
            self.ARREGLOGLOBALMAXIMO.sort(key = lambda x: x[1],reverse=True)
            if len(self.ARREGLOGLOBALMAXIMO) < int(self.idPoblacionMaxima.text()):
                self.graficaIndividuos(self.ARREGLOGLOBALMAXIMO)
            else:
                arregloaux = []
                for x in range(0,int(self.idPoblacionMaxima.text())):
                    arregloaux.append(self.ARREGLOGLOBALMAXIMO[x])
                self.graficaIndividuos(arregloaux)
            pass
        
        #minimo
        if self.r2.isChecked():
            count = 0
            while count < len(self.OZELX):
                self.ARREGLOGLOBALMINIMO.append((self.OZELX[count],self.OZELY[count]))
                count+=1
            self.ARREGLOGLOBALMINIMO.sort(key = lambda x: x[1])
            if len(self.ARREGLOGLOBALMINIMO) < int(self.idPoblacionMaxima.text()):
                self.graficaIndividuos(self.ARREGLOGLOBALMINIMO)
            else:
                arregloaux = []
                for x in range(0,int(self.idPoblacionMaxima.text())):
                    arregloaux.append(self.ARREGLOGLOBALMINIMO[x])
                self.graficaIndividuos(arregloaux)
            pass
        #print(self.ARREGLOFX)


    def formula1(self,arreglo):
        self.ARREGLOXI.clear()
        for item in arreglo:
            x = int(self.inicioIntervalo.text()) + item * float(self.presicionText.text())
            self.ARREGLOXI.append(x)
        pass

    def formular2(self): 
        self.ARREGLOFX.clear()
        for x in self.ARREGLOXI:
            y = 0.75*math.cos(1.50*x)*math.sin(0.75*x) + 0.25*math.cos(0.25*x)
            self.ARREGLOFX.append(y)
        pass


    def graficaIndividuos(self,arreglox):
        x = []
        y = []
        print("llego aqui")
        for x2 in arreglox:
            x.append(x2[0])
            y.append(x2[1])
        print("valor de x imprimir")
        print(x)
        print("valor de y imprimir")
        print(y)
        pyplot.scatter(x,y)
        pyplot.xlim(-10,50)
        pyplot.ylim(-10,50)
        pyplot.title(f"grafica{self.COUNTIMG}")
        pyplot.savefig(f"img/i{self.COUNTIMG}.png")
        #pyplot.show()
        pyplot.close()
        self.COUNTIMG += 1
        pass

    def graficaHistorico(self):
        arregloAuxMejor = []
        arreglAuxPeor = []
        arregloAuxPromedio = []
        arreglox = []
        count = 0
        for x in self.ARREGLOFINALGENERACION:
            arregloAuxMejor.append(x[0])
            arreglAuxPeor.append(x[1])
            arregloAuxPromedio.append(x[2])
            count += 1
            arreglox.append(count)
        pyplot.plot(arreglox,arregloAuxMejor,label="Mejor")
        pyplot.plot(arreglox,arreglAuxPeor,label="peor")
        pyplot.plot(arreglox,arregloAuxPromedio,label="Promedio")
        pyplot.legend()
        pyplot.show()


    def crearVideo(self):
        images = []
        for index in range(0,int(self.idGeneracion.text())):
            path = cv2.imread(f"img/i{index}.png")
            images.append(path)
        
        alto,ancho = path.shape[:2]
        video = cv2.VideoWriter("v/video_g.mp4",cv2.VideoWriter_fourcc(*"mp4v"),1,(ancho,alto))

        for img in images:
            video.write(img)
        video.release()
            
        #por cada iteracion
        #[0.21,0.4,0.12,0.26,0.09,0.52]
        #maximo 0.52
        #minimo 0.09
        #promedio 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = WindowView()
    GUI.show()
    sys.exit(app.exec_())