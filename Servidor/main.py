# -*- coding: utf-8 -*-

#Marcelo E Mellimaci - Luis Maccapa
#Proyecto final de Programación Orientada a Objetos
#Aplicativo de servidor para Robot 3DF con efector final
# PROGRAMA DEL SERVIDOR

from panel_de_control import panel_de_control

def main():
    print("===========================================================")
    print(" Aplicativo del servidor para Robot 3DF con efector final")
    print("===========================================================")

    try:
        CLI = panel_de_control()
        CLI.prompt = ' > '
        print('\nPresione Control+C para cerrar la línea de comandos')
        CLI.cmdloop(' Iniciando entrada de comandos...')
    except:
        print("'\n Cerrando interfaz de línea de comandos \n")


if __name__ == '__main__':
    main()
