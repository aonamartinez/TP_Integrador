from entradas import *
from funciones import *
from salidas import *
import time
import platform
import subprocess
#\n

def limpiar_consola():
    if platform.system() == "Windows":
        subprocess.run("cls",shell=True)
        subprocess.run("cls",shell=True)
    else:
        subprocess.run("clear",shell=True)
        subprocess.run("clear",shell=True) 

def refrescar_menu(tiempo_menu:int = 0,mensaje_menu:str = "Toque enter para continuar...", ) -> None:
    time.sleep(tiempo_menu)
    if tiempo_menu == 0:
        input(mensaje_menu)
    limpiar_consola()

def mostrar_menu_principal():
    print("----- MENÚ DE OPCIONES -----")
    print("1. Ver datos personales")
    print("2. Transferir dinero")
    print("3. Ver historial de transferencias")
    print("4. Salir del sistema")
    time.sleep(0.5)
    opcion_select = input("Ingrese su opción: ")

    return opcion_select

def ejecutar_menu_principal():
    return


