# -*- coding: utf-8 -*-

#Marcelo E Mellimaci - Luis Maccapa
#Proyecto final de Programación Orientada a Objetos
# Clase EfectorFinal

class EfectorFinal:
    def __init__(self):
        self.estadoAbierto = False  # inicialmente la pinza está cerrada
        self.velocidad_limite= 50  # velocidad máxima mm/s
        self.velocidad= 0  # velocidad inicial 0 mm/s


    def abrir(self, Veloc):
        #abre la pinza
        self.estadoAbierto= True
        self.velocidad= Veloc

        return ("La pinza está abierta" )


    def cerrar(self, Veloc):
        #cierra la pinza
        self.estadoAbierto = False
        self.velocidad= Veloc
        
        return ("La pinza está cerrada" )