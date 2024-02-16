import json
import funcionesD as fun
import modulo as mod

x = True
while x == True:
    fun.title()
    print("")
    print("1. Modulo de Usuario \n2.Modulo de Servicios \n3.Salir")
    rta = input("Digite número según el area a la cual deseas ingresar")
    if rta == '1':
        y = True
        while y == True:
            print("")
            fun.titleUser()
            print("")
            print("Opciones: ")
            print("1. Registro y gestión \n2. Historial \n3.Personalización de servicios")
            print("4. Interacción \n5. Volver al menú anterior")
            option = input("Digite un número según la opción a la que seas ingresar: ")
            if option == '1':
                s = True
                while s == True:
                    print("")
                    fun.title()
                    print("")
                    print("Has ingresado al area de registro y gestion de los datos del usuario.")
                    print("Qué deseas hacer?")
                    fun.regFun()
            elif option == '2':
                print(2)
            elif option == '3':
                print("")
            elif option == '4':
                print("")
            elif option > '5':
                print("Error: ")
                print("Favor ingresar número entero que este detro de 1 - 5.")
            else:
                if option == '5':
                    s = False
    elif rta == '2':
        z = True
        while z == True:
            print("")
            fun.titleServ()
