# -*- coding: utf-8 -*-

#Marcelo E Mellimaci - Luis Maccapa
#Proyecto final de Programación Orientada a Objetos
# Clase Robot

from Articulacion import Articulacion
from EfectorFinal import EfectorFinal
from time import sleep
from Grafica import Grafica

class Robot:
    def __init__(self):
        self.articulac_1 = Articulacion(120) # las tres articulaciones del robot:
        self.articulac_2 = Articulacion(120) #dos de ellas tienen 120 mm de longitud
        self.articulac_3 = Articulacion(0)   #la otra no tiene extensión
        self.efectorfinal = EfectorFinal()  # el efector del robot es una pinza
        self.reporte= []   # reporte de órdenes del robot
        self.graficas= Grafica()  # registra los estados del robot en gráficas


    def registrar_en_graficas(self):
        #Registra el estado actual del robot en las gráficas
        anguloArticulacion_1= self.articulac_1.angulo
        self.graficas.articulacion_1.append(anguloArticulacion_1)

        anguloArticulacion_2= self.articulac_2.angulo
        self.graficas.articulacion_2.append(anguloArticulacion_2)

        anguloArticulacion_3= self.articulac_3.angulo
        self.graficas.articulacion_3.append(anguloArticulacion_3)

        estadoAbierto_pinza= self.efectorfinal.estadoAbierto
        self.graficas.Pinza.append(estadoAbierto_pinza)

        velocidadArticulacion_1= self.articulac_1.velocidad
        self.graficas.velocs_articulac_1.append(velocidadArticulacion_1)

        velocidadArticulacion_2= self.articulac_2.velocidad
        self.graficas.velocs_articulac_2.append(velocidadArticulacion_2)

        velocidadArticulacion_3= self.articulac_3.velocidad
        self.graficas.velocs_articulac_3.append(velocidadArticulacion_3)

        velocidad_Pinza= self.efectorfinal.velocidad
        self.graficas.velocs_pinza.append(velocidad_Pinza)


    def mostrar_graficas(self):
        # muestra gráficas de los sucesivos estados del robot
        self.graficas.graficar()


    def homing(self):
        # retorna al robot a su disposición inicial
        self.reporte.append("HOMING")
        self.articulac_1.mover_art(0,0)
        self.articulac_2.mover_art(0,0)
        self.articulac_3.mover_art(0,0)
        self.efectorfinal.cerrar(0)
        sleep(0.3) 
        # Se genera un breve delay durmuendo el hilo durante 0.3 segundos para
        #simular los tiempos de demora de la propia cinemática del robot
        return ("El robot ha vuelto sus posiciones iniciales")


    def moverArticulacion_1(self, Angulo, Velocidad):
        #mueve la articulación 1 un determinado ángulo a la velocidad que se indique
        mensaje= self.articulac_1.mover_art(Angulo, Velocidad)
        self.reporte.append("MOVER 1 "+str(Angulo)+" "+str(Velocidad))
        sleep(0.3) 
        # Se genera un breve delay durmuendo el hilo durante 0.3 segundos para
        #simular los tiempos de demora de la propia cinemática del robot
        return ("Articulación 1 : " + mensaje)


    def moverArticulacion_2(self, Angulo, Velocidad):
        #mueve la articulación 2 un determinado ángulo a la velocidad que se indique
        mensaje= self.articulac_2.mover_art(Angulo, Velocidad)
        self.reporte.append("MOVER 2 "+str(Angulo)+" "+str(Velocidad))
        sleep(0.3) 
        # Se genera un breve delay durmuendo el hilo durante 0.3 segundos para
        #simular los tiempos de demora de la propia cinemática del robot
        return ("Articulación 2 : " + mensaje)


    def moverArticulacion_3(self, Angulo, Velocidad):
        #mueve la articulación 3 un determinado ángulo a la velocidad que se indique
        mensaje= self.articulac_3.mover_art(Angulo, Velocidad)
        self.reporte.append("MOVER 3 "+str(Angulo)+" "+str(Velocidad))
        sleep(0.3) 
        # Se genera un breve delay durmuendo el hilo durante 0.3 segundos para
        #simular los tiempos de demora de la propia cinemática del robot
        return ("Articulación 3 : " + mensaje)


    def abrirEfector(self, Velocidad):
        #abre la pinza a la velocidad que se indique
        self.reporte.append("EFECTOR 1 "+str(Velocidad))
        sleep(0.3) 
        # Se genera un breve delay durmuendo el hilo durante 0.3 segundos para
        #simular los tiempos de demora de la propia cinemática del robot
        return self.efectorfinal.abrir(Velocidad)


    def cerrarEfector(self, Velocidad):
        #cierra la pinza a la velocidad que se indique
        self.reporte.append("EFECTOR 0 "+str(Velocidad))
        sleep(0.3) 
        # Se genera un breve delay durmuendo el hilo durante 0.3 segundos para
        #simular los tiempos de demora de la propia cinemática del robot
        return self.efectorfinal.cerrar(Velocidad)


    def reporteArticulacion_1(self):
        # entrega el estado actual de la articulación 1
        infoA1= ("\n Articulación 1:\t"+str(self.articulac_1.angulo)+"°\t"+
        str(self.articulac_1.desplazamiento)+" mm\tÚltima veloc: "+str(self.articulac_1.velocidad)+" mm/s")
        return infoA1


    def reporteArticulacion_2(self):
        # entrega el estado actual de la articulación 2
        infoA2= ("\n Articulación 2:\t"+str(self.articulac_2.angulo)+"°\t"+
        str(self.articulac_2.desplazamiento)+" mm\tÚltima veloc: "+str(self.articulac_2.velocidad)+" mm/s")
        return infoA2


    def reporteArticulacion_3(self):
        # entrega el estado actual de la articulación 3
        infoA3= ("\n Articulación 3:\t"+str(self.articulac_3.angulo)+"°\t"+
        str(self.articulac_3.desplazamiento)+" mm\tÚltima veloc: "+str(self.articulac_3.velocidad)+" mm/s")
        return infoA3


    def reporteEfector(self):
        # muestra el estado actual de la pinza
        pinza= ""
        if (self.efectorfinal.estadoAbierto == True):
            pinza= "Abierto"
        elif(self.efectorfinal.estadoAbierto == False):
            pinza= "Cerrado"

        infoEfector= ("\n Efector final:\t"+str(pinza)+
        "\tÚltima veloc: "+str(self.efectorfinal.velocidad)+" mm/s")

        return infoEfector


    def get_reporte(self):
        # dá el reporte de órdenes del robot
        Reporte= ""
        for orden in self.reporte:
            Reporte += "\n"
            Reporte += orden

        return Reporte
