from menu import *
from entradas import *
from funciones import *
from salidas import *
import time

#marianofernandez@fra.utn.edu.ar
bienvenida_sistema()

lista_usuarios = []
usuario = cargar_usuario()
lista_usuarios.append(usuario)

bienvenida_personal(lista_usuarios[0][5],lista_usuarios[0][6],lista_usuarios[0][2])

#CBU: 0321456789123456789123
lista_cbu_destino = []
lista_montos = []
lista_fechas = []

seguir= "si"

while seguir == "si":
    
    opcion = mostrar_menu_principal()
    match opcion:
        case "1":
            mostrar_datos_personales(lista_usuarios)
        case "2":
            transferir_dinero(lista_usuarios,lista_cbu_destino,lista_montos,lista_fechas)
        case "3":
            ver_historial_transferencias(lista_usuarios,lista_cbu_destino,lista_montos,lista_fechas)
        case "4":
            cerrar_programa()

    seguir = input("¿Desea volver al menú? (si/no): ")
    
cerrar_programa()

# opcion = menu_opciones()
# while opcion != "4":
#     match opcion:
#         case "1":
#             ver_datos_personales(lista_usuarios)
#             print()
#         case "2":
#             transferir_dinero(lista_usuarios,lista_cbu_destino,lista_montos,lista_fechas)
#             print()
#         case "3":
#             ver_historial_transferencias(lista_usuarios,lista_cbu_destino,lista_montos,lista_fechas)
#             print()

#     seguir = input("¿Desea volver al menú?")
    
#     if seguir == "si":
#         time.sleep(3)
#         opcion = menu_opciones()
#     else:
#         cerrar_programa()
