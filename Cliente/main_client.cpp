//Marcelo E Mellimaci - Luis Maccapa
//Proyecto final de Programación Orientada a Objetos
//Aplicativo de cliente para Robot 3DF con efector final
// PROGRAMA DEL CLIENTE

#include <iostream>
#include <stdlib.h>
using namespace std;

#include "XmlRpc.h"
using namespace XmlRpc;


int main(){
    cout  <<  "========================================================" <<endl
            <<" Aplicativo de cliente para Robot 3DF con efector final" <<endl
            <<"========================================================" <<endl;
    
    //El hostname es "localhost" (idéntico a 127.0.0.1) y el puerto usado es 8000
    //En este caso el servidor y el cliente correrán sobre la misma máquina
    XmlRpcClient c("localhost", 8000);
    
    //Se crean variables declaradas para enviar y recibir mensajes entre
    //el cliente y el servidor
    XmlRpcValue noArgs, result;
    double a1, a2;
    
    while(true){
        //Se muestran las operaciones que puede realizar el servidor
        cout  <<   "   1. Mover Articulación 1" <<endl
                << "   2. Mover Articulación 2" <<endl
                << "   3. Mover Articulación 3" <<endl
                << "   4. Abrir Pinza" <<endl
                << "   5. Cerrar Pinza" <<endl
                << "   6. Homing" <<endl
                << "   7. Mostrar Reporte" <<endl
                << "   8. Cerrar el Servidor" <<endl
                << "   9. Salir de la aplicación" <<endl
                <<"=======================================" <<endl;
        cout<< "Opcion: ";
        
        char opcion;
        cin>> opcion;
        
        if (opcion == '1'){
            //1: mueve la articulación 1 un determinado ángulo a la velocidad que se indique
            cout<< "Ángulo [grados]: ";
            cin>> a1;
            cout<< "Velocidad [mm/s]: ";
            cin>> a2;
            noArgs[0] = a1;
            noArgs[1] = a2;
            c.execute("mover_1", noArgs, result);
            cout<< result <<endl;
        }
        
        else if(opcion == '2'){
            //2: mueve la articulación 2 un determinado ángulo a la velocidad que se indique
            cout<< "Ángulo [grados]: ";
            cin>> a1;
            cout<< "Velocidad [mm/s]: ";
            cin>> a2;
            noArgs[0] = a1;
            noArgs[1] = a2;
            c.execute("mover_2", noArgs, result);
            cout<< result <<endl;
        }
        
        else if(opcion == '3'){
            //3: mueve la articulación 3 un determinado ángulo a la velocidad que se indique
            cout<< "Ángulo [grados]: ";
            cin>> a1;
            cout<< "Velocidad [mm/s]: ";
            cin>> a2;
            noArgs[0] = a1;
            noArgs[1] = a2;
            c.execute("mover_3", noArgs, result);
            cout<< result <<endl;
        }
        
        else if(opcion == '4'){
            //4: abre la pinza [1 : abrir / 0 : cerrar]
            a1= 1;
            cout<< "Velocidad [mm/s]: ";
            cin>> a2;
            noArgs[0] = a1;
            noArgs[1] = a2;
            c.execute("pinza", noArgs, result);
            cout<< result <<endl;
        }
        
        else if(opcion == '5'){
            //5: cierra la pinza [1 : abrir / 0 : cerrar]
            a1= 0;
            cout<< "Velocidad [mm/s]: ";
            cin>> a2;
            noArgs[0] = a1;
            noArgs[1] = a2;
            c.execute("pinza", noArgs, result);
            cout<< result <<endl;
        }
        
        else if(opcion == '6'){
            //6: retorna al robot a su disposición inicial
            c.execute("h", noArgs, result);
            cout<< result <<endl;
        }
        
        else if(opcion == '7'){
            //7: muestra un reporte de las acciones realizadas por el robot
            c.execute("report", noArgs, result);
            cout<< result <<endl;
        }
        
        else if(opcion == '8'){
            //8: envía una solicitud de cierre al servidor del robot
            cout<< "¿Quiere cerrar el servidor? [S/n] ";
            cin>> opcion;
            
            if(opcion == 'S' || opcion == 's'){
                c.execute("fin", noArgs, result);
                cout<< result <<endl;
            }
        }
        
        else if(opcion == '9'){
            //9: sale de esta aplicación
            cout<< "¿Quiere salir del aplicativo? [S/n] ";
            cin>> opcion;
            
            if(opcion == 'S' || opcion == 's'){
                cout<< "\n HA CERRADO EL CLIENTE" <<endl;
                return 0;
            }

        }
        
        else{
            cout<< "\n ERROR: La orden ingresada no corresponde a una opción válida" <<endl;
        }
    }
    
}