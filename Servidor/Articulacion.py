# -*- coding: utf-8 -*-

#Marcelo E Mellimaci - Luis Maccapa
#Proyecto final de Programación Orientada a Objetos
# Clase Articulacion

import math

class Articulacion:
    def __init__(self, Radio):
        self.angulo_limite = 90  # ángulo tope máximo grados°
        self.velocidad_limite= 50  # velocidad máxima mm/s
        self.radio = Radio  # radio extensión de la articulación mm
        self.angulo= 0  # ángulo inicial 0 grados°
        self.velocidad= 0  # velocidad inicial 0 mm/s
        self.desplazamiento= 0  # desplazamiento neto realizado mm


    def mover_art(self, Angulo, Velocidad):
        # mueve la articulación determinada dentro de los límites de trabajo
        if (Angulo > self.angulo_limite):
            Angulo = self.angulo_limite
        if (Angulo < (-self.angulo_limite)):
            Angulo = -self.angulo_limite

        if (Velocidad > self.velocidad_limite):
            Velocidad= self.velocidad_limite
        if (Velocidad < (-self.velocidad_limite)):
            Velocidad= -self.velocidad_limite

        self.angulo= Angulo
        self.velocidad= Velocidad
        self.desplazamiento = self.radio*(Angulo*math.pi/180)

        return("se movió a "+str(Angulo)+"° a "+str(Velocidad)+
        " mm/s desplazandosé "+str(self.desplazamiento)+" mm del origen")