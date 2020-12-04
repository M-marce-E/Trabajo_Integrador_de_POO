# -*- coding: utf-8 -*-

#Marcelo E Mellimaci - Luis Maccapa
#Proyecto final de Programación Orientada a Objetos
# Clase servidor_XmlRpc

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from robot import Robot

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


class servidor_XmlRpc:
    def __init__(self, Puerto):
        # El hostname es "localhost" (idéntico a 127.0.0.1) 
        #En este caso el servidor y el cliente correrán sobre la misma máquina        
        self.IP= 'localhost'
        self.puerto= Puerto
        #Se instancia el robot aquí para evitar usar el objeto como variable global
        self.robot_1= Robot()
        
    def escuchar(self):
        # Mantiene activo el servidor del robot
        with SimpleXMLRPCServer((self.IP, self.puerto),
                                requestHandler=RequestHandler) as server:
            server.register_introspection_functions()

            # Se registra una función con un nombre diferente, usando 
            #"register_function(" como decorador
            # De la documentación: *name* can only be given as a keyword argument

            @server.register_function(name='mover_1')
            def mover_articulac_1(angulo, velocidad):
                # mueve la articulación 1 del robot
                articulacion= int(1)
                Angulo= float(angulo)
                Velocidad= float(velocidad)
                
                if (articulacion == 1):
                    msje= (self.robot_1.moverArticulacion_1(Angulo, Velocidad))
                    print (msje)
                    # Registra en las gráficas luego de ejecutar la orden
                    self.robot_1.registrar_en_graficas()
                    return(msje)
                elif(articulacion == 2):
                    msje= self.robot_1.moverArticulacion_2(Angulo, Velocidad)
                    print (msje)
                    # Registra en las gráficas luego de ejecutar la orden
                    self.robot_1.registrar_en_graficas()
                    return(msje)
                elif(articulacion == 3):
                    msje= self.robot_1.moverArticulacion_3(Angulo, Velocidad)
                    print (msje)
                    # Registra en las gráficas luego de ejecutar la orden
                    self.robot_1.registrar_en_graficas()
                    return(msje)
                


            @server.register_function(name='mover_2')
            def mover_articulac_2(angulo, velocidad):
                """mueve la articulación 2 del robot"""
                articulacion= int(2)
                Angulo= float(angulo)
                Velocidad= float(velocidad)
                
                if (articulacion == 1):
                    msje= (self.robot_1.moverArticulacion_1(Angulo, Velocidad))
                    print (msje)
                    # Registra en las gráficas luego de ejecutar la orden
                    self.robot_1.registrar_en_graficas()
                    return(msje)
                elif(articulacion == 2):
                    msje= self.robot_1.moverArticulacion_2(Angulo, Velocidad)
                    print (msje)
                    # Registra en las gráficas luego de ejecutar la orden
                    self.robot_1.registrar_en_graficas()
                    return(msje)
                elif(articulacion == 3):
                    msje= self.robot_1.moverArticulacion_3(Angulo, Velocidad)
                    print (msje)
                    # Registra en las gráficas luego de ejecutar la orden
                    self.robot_1.registrar_en_graficas()
                    return(msje)


            @server.register_function(name='mover_3')
            def mover_articulac_3(angulo, velocidad):
                """mueve la articulación 3 del robot"""
                articulacion= int(3)
                Angulo= float(angulo)
                Velocidad= float(velocidad)
                
                if (articulacion == 1):
                    msje= (self.robot_1.moverArticulacion_1(Angulo, Velocidad))
                    print (msje)
                    # Registra en las gráficas luego de ejecutar la orden
                    self.robot_1.registrar_en_graficas()
                    return(msje)
                elif(articulacion == 2):
                    msje= self.robot_1.moverArticulacion_2(Angulo, Velocidad)
                    print (msje)
                    # Registra en las gráficas luego de ejecutar la orden
                    self.robot_1.registrar_en_graficas()
                    return(msje)
                elif(articulacion == 3):
                    msje= self.robot_1.moverArticulacion_3(Angulo, Velocidad)
                    print (msje)
                    # Registra en las gráficas luego de ejecutar la orden
                    self.robot_1.registrar_en_graficas()
                    return(msje)


            @server.register_function(name='pinza')
            def efector(estadoAbierto, Velocidad):
                #abre y cierra la pinza [1 : abrir / 0 : cerrar] [velocidad mm/s]
                estadoEfector= int(estadoAbierto)
                velocidadEfector= float(Velocidad)

                if (estadoEfector == 1):
                    msje= self.robot_1.abrirEfector(velocidadEfector)
                    print (msje)
                    # Registra en las gráficas luego de ejecutar la orden
                    self.robot_1.registrar_en_graficas()
                    return(msje)
                elif(estadoEfector == 0):
                    msje= self.robot_1.cerrarEfector(velocidadEfector)
                    print (msje)
                    # Registra en las gráficas luego de ejecutar la orden
                    self.robot_1.registrar_en_graficas()
                    return(msje)
        

            @server.register_function(name='h')
            def Homing(noArgs, noArgs0):
                # retorna al robot a su disposición inicial
                msje= self.robot_1.homing()
                print (msje)
                # Registra en las gráficas luego de ejecutar la orden
                self.robot_1.registrar_en_graficas()
                return(msje)


            @server.register_function(name='report')
            def Reporte(noArgs, noArgs0):
                # reporte de las acciones realizadas por el robot
                mensaje= " Reporte de órdenes:" + self.robot_1.get_reporte() + "\n"

                mensaje += self.robot_1.reporteArticulacion_1()
                mensaje += self.robot_1.reporteArticulacion_2()
                mensaje += self.robot_1.reporteArticulacion_3()
                mensaje += self.robot_1.reporteEfector()

                print (mensaje)
                return(mensaje)


            @server.register_function(name='fin')
            def Cerrar_Servidor(noArgs, noArgs0):
                # muestra una petición de cierre del servidor del robot
                print('\n Se quiere cerrar remotamente el servidor XML-RPC')
                print(' Presione Control+C para cerrar el servidor \n')
                print(exit)
                return("Se ha enviado una petición de cierre al servidor del robot")
            

            # Incia el servidor
            try:
                print(' Presione Control+C para cerrar el servidor')
                server.serve_forever()
            except KeyboardInterrupt:
                print('\n Se ha cerrado el servidor XML-RPC \n')
            except:
                print('\n Se ha cerrado el servidor XML-RPC \n')
        