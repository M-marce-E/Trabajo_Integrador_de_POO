# -*- coding: utf-8 -*-

#Marcelo E Mellimaci - Luis Maccapa
#Proyecto final de Programación Orientada a Objetos
# Clase panel_de_control

from cmd import Cmd
from servidor_XmlRpc import servidor_XmlRpc

class panel_de_control(Cmd):
    doc_header = "Ayuda de comandos documentados"
    undoc_header = "Ayuda de comandos no documentados"
    ruler = "="

    servidor= servidor_XmlRpc(8000)  # El puerto usado es 8000

    def do_automatico(self, args):
        """AUTOMATICO [nombre del archivo, incluyendo extensión]
        toma órdenes para el robot desde un archivo"""
        argumentos = args.split()
        # Se lee cada línea del archivo usando readlines()
        if (len(argumentos) == 1):
            argumentos = str(args)
            archivo = open(argumentos, 'r') 
            Ordenes = archivo.readlines()

            # No se toma la primera línea que está en blanco y
            #lo único que tiene es un salto de línea /n
            # .lower() pasa a minúsculas todos los comandos para 
            #evitar errores de tipeo
            i=1
            for orden in Ordenes:
                if(i==1):
                    pass
                elif(i == len(Ordenes)):
                    self.onecmd(str(orden).lower())
                    # self.onecmd efectúa lo que se indique entre ()
                    #en la línea de comandos del panel_de_control
                else:
                    self.onecmd(str(orden[:-1]).lower())
                    # [:-1] elimina el último caracter de la línea, que
                    #en este casi es un salto de línea \n
                i += 1

            print("Se han realizado las órdenes del archivo "+argumentos)
        else:
            self.onecmd("help automatico")


    def do_efector(self, args):
        """EFECTOR [1 : abrir / 0 : cerrar] [velocidad mm/s]
        abre o cierra la pinza a la velocidad que se indique"""
        argumentos = args.split()
        if (len(argumentos) == 2):
            estadoEfector= int(argumentos[0])
            velocidadEfector= float(argumentos[1])

            if(estadoEfector == 1):
                mensaje= panel_de_control.servidor.robot_1.abrirEfector(velocidadEfector)
                # Registra en las gráficas luego de ejecutar la orden
                panel_de_control.servidor.robot_1.registrar_en_graficas()
                print(mensaje)
            elif(estadoEfector == 0):
                mensaje= panel_de_control.servidor.robot_1.cerrarEfector(velocidadEfector)
                # Registra en las gráficas luego de ejecutar la orden
                panel_de_control.servidor.robot_1.registrar_en_graficas()
                print(mensaje)
            else:
                self.onecmd("help efector")

        else:
            self.onecmd("help efector")


    def do_graficar(self, args):
        """GRAFICAR
        muestra gráfica de los sucesivos estados del robot"""
        panel_de_control.servidor.robot_1.mostrar_graficas()

        
    def do_guardar(self, args):
        """GUARDAR [nombre del archivo, incluyendo extensión]
        guarda el reporte de órdenes del robot en un archivo de texto"""
        argumentos = args.split()
        if (len(argumentos) == 1):
            argumentos = str(args)
            archivo = open(argumentos, 'w')
            archivo.writelines((panel_de_control.servidor.robot_1.get_reporte())) 
            archivo.close()

            print("Se ha guardado el reporte de órdenes en un archivo de texto")
        else:
            self.onecmd("help guardar")

    
    def do_homing(self, args):
        """HOMING
        retorna al robot a su disposición inicial"""
        mensaje= panel_de_control.servidor.robot_1.homing()
        # Registra en las gráficas luego de ejecutar la orden
        panel_de_control.servidor.robot_1.registrar_en_graficas()
        print(mensaje)


    def do_mover(self, args):
        """MOVER [nro articulación 1 a 3] [ángulo grados] [velocidad mm/s]
        mueve una articulación determinada del robot"""
        argumentos = args.split()
        if (len(argumentos) == 3):
            articulacion= int(argumentos[0])
            Angulo= float(argumentos[1])
            Velocidad= float(argumentos[2])
            
            if (articulacion == 1):
                mensaje= panel_de_control.servidor.robot_1.moverArticulacion_1(Angulo, Velocidad)
                # Registra en las gráficas luego de ejecutar la orden
                panel_de_control.servidor.robot_1.registrar_en_graficas()
                print(mensaje)
            elif(articulacion == 2):
                mensaje= panel_de_control.servidor.robot_1.moverArticulacion_2(Angulo, Velocidad)
                # Registra en las gráficas luego de ejecutar la orden
                panel_de_control.servidor.robot_1.registrar_en_graficas()
                print(mensaje)
            elif(articulacion == 3):
                mensaje= panel_de_control.servidor.robot_1.moverArticulacion_3(Angulo, Velocidad)
                # Registra en las gráficas luego de ejecutar la orden
                panel_de_control.servidor.robot_1.registrar_en_graficas()
                print(mensaje)
            
            else:
                self.onecmd('help mover')
        else:
            self.onecmd('help mover')


    def do_reporte(self, args):
        """REPORTE
        muestra un reporte de las acciones realizadas por el robot"""
        mensaje= " Reporte de órdenes:" + panel_de_control.servidor.robot_1.get_reporte() + "\n"

        mensaje += panel_de_control.servidor.robot_1.reporteArticulacion_1()
        mensaje += panel_de_control.servidor.robot_1.reporteArticulacion_2()
        mensaje += panel_de_control.servidor.robot_1.reporteArticulacion_3()
        mensaje += panel_de_control.servidor.robot_1.reporteEfector()

        print(mensaje)


    def do_quit(self, args):
        """QUIT
        sale del aplicativo"""
        print("Ejecucion de la CLI terminada")
        raise SystemExit

    def do_exit(self, args):
        """EXIT
        sale del aplicativo"""
        print("Ejecucion de la CLI terminada")
        raise SystemExit


    def do_rpc(self, args):
        """RPC
        operar el robot remotamente mediante XML-RPC"""
        print("\nSe inició el servidor XML-RPC del robot")
        panel_de_control.servidor.escuchar()


    def default(self, args):
        print("Error. El comando \'" + args + "\' no esta disponible")

    def precmd(self, args):
        #Esta función pasa a minúsculas todos los comandos que se
        #ingresen para evitar errores de tipeo
        args = args.lower()
        return(args)