from menu import *
from funciones import *
import time

def bienvenida_sistema():
    print(":"*20 + " BIENVENIDO A PAYUT "+ ":"*20)
    print("Una billetera virtual para gestionar y agilizar tus pagos.")
    print("Su finalidad es poder realizar transferencia de forma simple y rápida")
    print("."*90)
    time.sleep(1)

def bienvenida_personal (nombre, apellido, saldo_actual):
    print(f"BIENVENIDO/A: {nombre} {apellido}")
    print(f"SU SALDO ACTUAL ES DE: ${saldo_actual}")
    print("."*90)

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


def mostrar_menu():
    return
