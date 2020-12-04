# -*- coding: utf-8 -*-

#Marcelo E Mellimaci - Luis Maccapa
#Proyecto final de Programación Orientada a Objetos
# Clase Grafica

import matplotlib.pyplot as plt

class Grafica:
    def __init__(self):
        self.articulacion_1= []  # sucesivos ángulos de la articulación 1
        self.articulacion_2= []  # sucesivos ángulos de la articulación 2
        self.articulacion_3= []  # sucesivos ángulos de la articulación 3
        self.Pinza= []   # lista con los sucesivos estados de la pinza
        self.velocs_articulac_1= []  # sucesivas velocidades de la articulac 1
        self.velocs_articulac_2= []  # sucesivas velocidades de la articulac 2
        self.velocs_articulac_3= []  # sucesivas velocidades de la articulac 3
        self.velocs_pinza= []  # sucesivas velocidades de la pinza


    def graficar(self):
        # muestra gráficas de los sucesivos estados del robot
        
        # GRÁFICA 1: VELOCIDADES PARA CADA ÓRDEN
        plot2 = plt.figure(1)
        plt.suptitle("Velocidades")
        plt.plot(self.velocs_articulac_1, marker='o', label="Articulación 1")
        plt.plot(self.velocs_articulac_2, marker='o', label="Articulación 2")
        plt.plot(self.velocs_articulac_3, marker='o', label="Articulación 3")
        plt.plot(self.velocs_pinza, marker='o', color="red", label="Veloc de la Pinza")
        plt.xlabel("órdenes")
        plt.ylabel("[mm/s]")
        plt.legend()

        # GRÁFICA 2: ÁNGULOS Y ESTADO DE LA PIZA PARA CADA ÓRDEN
        plot1 = plt.figure(2)
        plt.suptitle("Secuencia de estados del robot")

        #Las gráfica de las articulaciones irá arriba (en la 1ra de las 2 filas)
        plt.subplot(2, 1, 1)
        plt.plot(self.articulacion_1, marker='o', label="Articulación 1")
        plt.plot(self.articulacion_2, marker='o', label="Articulación 2")
        plt.plot(self.articulacion_3, marker='o', label="Articulación 3")
        plt.xlabel("órdenes")
        plt.ylabel("grados")
        plt.legend()

        #Las gráfica de la pinza irá abajo (en la 2da de las 2 filas)
        plt.subplot(2, 1, 2)
        plt.plot(self.Pinza, marker='o', color="red", label="Estado de la Pinza")
        plt.xlabel("órdenes")
        plt.ylabel("0=Cerrada  1=Abierta")
        plt.legend()

        plt.show()