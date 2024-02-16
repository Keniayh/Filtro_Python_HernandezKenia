import json
from pprint import pprint
#AGREGAR USUARIO

def addUser():
    try:
        with open('newUser.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
 

    newU = {
        'id': {
            'id': int(input("Ingrese el número de identifición: ")),
            'nombre': input("Ingresa el nombre: "),
            'apellidos': input("Ingresa los apellidos: "),
            'dir': input("Ingresa la dirección: "),
            'tel': int(input("Ingresa el número de telefono: ")),
            'fechaR': int(input("Ingrese el año en el que se registró: ")),
            'categoria': input("")
        }
    }
    
    data.append(newU)
    
    with open('newUser.json', 'w') as file:
        json.dump(data, file, indent = 4)


def viewUser():
    with open('newUser.json', 'r') as file:
        data = json.load(file)
    pprint(data)


#AGREGAR SERVICIO
        
def addServ():
    try:
        with open('newServ.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    


    planes = {
        'post': {
            'num': {
                'nombre': input("Ingrese nombre del servicio: "),
                'valor': int(input("Ingrese precio del producto:")),
                'describe': input("Has una breve descripción del producto: ")
            }
        }
    }
    
    data.append(planes)
    
    with open('newServ.json', 'w') as file:
        json.dump(data, file, indent = 4)

def antiguedadUser():
    try:
        with open('newUser.json', 'r') as archivo:
            data = json.load(archivo)
    except FileNotFoundError:
        data = []
    try:
        with open('antiguedad.json', 'r') as archivo:
            matri = json.load(archivo)
    except FileNotFoundError:
        anti = {}

    UserLeal = []

    for userLista in data:
        for entry userLista.get('id',[{"categoria": "No especicado"}]):
            if entry.get("")