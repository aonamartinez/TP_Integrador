from entradas import *
from funciones import *
from salidas import *
import time
#\n

def ingreso_de_datos_inicial ():
    return

def bienvenida_inicial (nombre, apellido, saldo_actual):
    print(f"BIENVENIDO/A: {nombre} {apellido}")
    print(f"SU SALDO ACTUAL ES DE: ${saldo_actual}")
    print("."*90)
    return

def menu_opciones():
    
    print("."*90)
    time.sleep(1)

    print("MENÚ DE OPCIONES")
    print("1. Ver datos personales")
    print("2. Transferir dinero")
    print("3. Ver historial de transferencias")
    print("4. Salir del sistema")

    time.sleep(0.5)
    opcion_select = input("Ingrese su opción: ")

    time.sleep(0.5)
    print("."*90)

    return opcion_select

def mostrar_datos_personales(lista:list):
    time.sleep(1)
    print("-"*10,"DATOS PERSONALES:","-"*10)
    print(f"NOMBRE DE USUARIO: {lista[0][0]}")
    print(f"SALDO ACTUAL: ${lista[0][2]}")
    print(f"CBU: {lista[0][3]}")
    print(f"ALIAS: {lista[0][4]}")
    print(f"NOMBRE: {lista[0][5]}")
    print(f"APELLIDO: {lista[0][6]}")
    print(f"DNI: {lista[0][7]}")
    print(f"EDAD: {lista[0][8]}")
    return

# lista_cbu_destino = []
# lista_montos = []
# lista_fechas = []

def validar_clave(clave_real, intentos:int, mensaje:str="ingrese", mensaje_error:str="Error")-> bool:
    bandera = False
    intento = 0
    time.sleep(1)

    while intento < intentos:
        clave_ingresada = pedir_string_rango(6,18,mensaje,mensaje_error)
        if clave_ingresada == clave_real:
            bandera = True
            break
        else:
            print(mensaje_error)
        intento +=1

    return bandera

########

def transferir_dinero(usuario:list, destinos:list, montos:list, fechas:list):
    
    time.sleep(1)
    clave = validar_clave(usuario[0][1],3,"Ingrese su clave: ","Error, clave inválida.")
    time.sleep(1)

    if clave == True :
        
        print("-"*15,"A continuación realizará una transferencia","-"*15)
        
        alias_destino = pedir_string_rango(6,16,"Ingrese alias del destinatario (entre 6 y 16 caracteres) : ","Error, alias inválido.")

        monto = pedir_float_rango_valor(0,usuario[0][2],"Ingrese el monto a transferir: $", "Error, supera su saldo actual.")

        fecha = "diadiadia"

        #Actualiza saldo del usuario actual
        usuario[0][2]= restar(usuario[0][2], monto)

        time.sleep(1)
        print("-"*15, "TRANSFERENCIA EXITOSA","-"*15,"\n")

        destinos.append(alias_destino)
        montos.append(monto)
        fechas.append(fecha)
        
    else:
        print("PROBLEMAS DE SEGURIDAD.")
        exit()
    return usuario

def ver_historial_transferencias(usuario:list,fecha:list, destino:list, monto:list):
    
    clave = validar_clave(usuario[0][1],3,"Ingrese su clave: ","Error, clave inválida.")
    if clave == True :
        
        print("-"*15,"Historial de transferencias:","-"*15)
        
        for i in range(len(fecha)):
            print(f"{fecha[i]} | Alias destino: {destino[i]} | Monto: ${monto[i]}")
    
    else:
        print("PROBLEMAS DE SEGURIDAD.")
        exit()
    return

def cerrar_programa():
    print("Aguarde por favor...")
    time.sleep(3)
    print("Cerrando el programa")
    return exit

