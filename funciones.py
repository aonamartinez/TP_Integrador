from menu import *
from entradas import *
from salidas import *

def cargar_usuario() -> list:
    
    lista_usuario = []
    
    usuario_nuevo = pedir_string_minimo(6,"Ingrese su nombre de usuario (mínimo 6 caracteres): ","Error, ingrese un usuario válido.")
    clave_nueva = pedir_string_rango(6,18,"Ingrese su clave (entre 6 y 8 caracteres, una mayuscula y un carácter especial): ", "Error, ingrese una clave válida.")
    saldo_nuevo = pedir_float_minimo_val(0,"Ingrese su saldo actual: $","Error, no puede ser negativo.")
    cbu_nuevo = pedir_string_minimo(22,"Ingrese su CBU (minimo 22 caracteres y debe comenzar con 0): ","Error, ingrese CBU válido.")
    alias_nuevo = pedir_string_rango(6,16,"Ingrese su alias (entre 6 y 16 caracteres): ", "Error, ingrese un alias válido.")
    nombre_nuevo = pedir_string_rango(3,20,"Ingrese su nombre: ", "Error, ingrese correctamente.")
    apellido_nuevo = pedir_string_rango(3,20,"Ingrese su apellido: ","Error, ingrese correctamente.")
    dni_nuevo = pedir_int_rango_ext(7,9,"Ingrese su DNI: ","Error, ingrese correctamente.")
    edad_nuevo = pedir_int_rango_val(18,120,"Ingrese su edad: ","Error, ingrese correctamente.")

    lista_usuario.append(usuario_nuevo)
    lista_usuario.append(clave_nueva)
    lista_usuario.append(saldo_nuevo)
    lista_usuario.append(cbu_nuevo)
    lista_usuario.append(alias_nuevo)
    lista_usuario.append(nombre_nuevo)
    lista_usuario.append(apellido_nuevo)
    lista_usuario.append(dni_nuevo)
    lista_usuario.append(edad_nuevo)
    print("."*90)

    return lista_usuario

def restar(num1, num2)->float:
    valor = num1 - num2
    return valor

def suma_lista()->float:
    return

def menor()->float:
    return

def mayor()->float:
    return

def promedio()->float:
    return

#validar q todo sea una lista
def validar_tipos_alumnos():
    return

# def validar_monto_rango(min, max, valor_inicial, mensaje:str="Ingrese", mensaje_error:str="Error") -> bool:

#     valor_nuevo = pedir_float_minimo_val(min,valor_inicial, mensaje, mensaje_error)
#     while valor_nuevo < min or valor_nuevo > max:
#         print("Supera su saldo actual. Ingrese nuevamente.")
#         valor_nuevo = pedir_float_minimo_val(min,valor_inicial, mensaje, mensaje_error)

#     return valor_nuevo

#########################################################################
#debe tener al menos una mayuscula y un caractrer especial
def validar_string(string_actual):
    bandera_may = True
    tiene_mayuscula = any(i.isupper() for i in string_actual)
    if not tiene_mayuscula:
        bandera_may = False

    bandera_car = False
    for i in range(len(string_actual)):
        if string_actual[i] in ("!","@","#","$","%","^","&","*","(",")","_","+","-","="):
            bandera_car = True
            break

    if bandera_may == True and bandera_car == True:
        return True
    else:
        "hola mundo"
