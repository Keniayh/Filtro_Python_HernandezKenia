import json
import modulo as mod
def title():
    print("------------------")
    print("-   BIENVENIDO   -")
    print("-     ADMIN      -")
    print("------------------")

def titleUser():
    print("--------------------")
    print("-     MODULO DE    -")
    print("-      USUARIOS    -")
    print("--------------------")

def titleServ():
    print("--------------------")
    print("-     MODULO DE    -")
    print("-     SERVICIOS    -")
    print("--------------------")

def regFun():
    print("")
    print("1. Agregar usuario \t2. Ver usuarios \n3. Actualizar Usuario \t4. Eliminar Usuarios \n5. Volver al menú anterior")
    res = input("Ingresa número según el area a la que deseas ingresar: ")
    if res == '1':
        print("--> AGREGANDO NUEVO USER <--")
        mod.addUser
        print("--> USUARIO AÑADIDO CON EXITO <--")

