# Pide cadena de caracteres con extension mínima
def pedir_string_minimo(min:int,mensaje:str ="Ingrese ",mensaje_error:str="ERROR") -> str :
    valor = input(str(mensaje))
    while len(valor) < min:
        print(mensaje_error)
        valor = input(str(mensaje))
    return valor

# Pide cadena de caracteres con extension dentro de un rango
def pedir_string_rango(min:int, max:int,mensaje:str ="Ingrese ",mensaje_error:str="ERROR") -> str:
    valor = input(str(mensaje))
    while len(valor) < min or len(valor) > max:
        print(mensaje_error)
        valor = input(str(mensaje))
    return valor

# Pide entero con valor numérico dentro de un rango
def pedir_int_rango_val(min:int, max:int,mensaje:str ="Ingrese ",mensaje_error:str="ERROR") -> int:
    valor = int(input(mensaje))
    while valor < min or valor > max:
        print(mensaje_error)
        valor = int(input(mensaje))
    return valor

# Pide entero con extención dentro de un rango
def pedir_int_rango_ext(min:int,max:int,mensaje:str ="Ingrese ",mensaje_error:str="ERROR") -> int :
    valor = input(mensaje)
    while len(valor) < min or len(valor) > max:
        print(mensaje_error)
        valor = input(mensaje)
    return valor

# Pide float con valor numérico mínimo
def pedir_float_minimo_val(min:int,mensaje:str ="Ingrese ",mensaje_error:str="ERROR") -> float:
    valor = float(input(mensaje))
    while valor < min:
        print(mensaje_error)
        valor = float(input(mensaje))
    return valor

# Pide float con una extensión mínima
def pedir_float_minimo_ext(min:int,mensaje:str = "", mensaje_error:str = "") -> float:
    valor = float(input(mensaje))
    while len(valor) < min:
        print(mensaje_error)
        valor = float(input(mensaje))
    return valor

# Pide float con valor numérico mínimo
def pedir_float_rango_valor(min:int, max:int,mensaje:str ="Ingrese ",mensaje_error:str="ERROR") -> float:
    valor = float(input(mensaje))
    while valor < min or valor > max:
        print(mensaje_error)
        valor = float(input(mensaje))
    return valor
