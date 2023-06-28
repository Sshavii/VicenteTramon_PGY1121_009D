import numpy as np
lista_nif = []
lista_nombre = []
lista_edad = []
lista_pertenece = []
lista_conyugal = []
i = 0
poto = 0
def grabar(nif,nombre,edad,pertenece,conyugal):
    lista_nif.append(nif)
    lista_nombre.append(nombre)
    lista_edad.append(edad)
    lista_pertenece.append(pertenece)
    lista_conyugal.append(conyugal)
def buscar(nif):
    nif = input("Ingrese el NIF a Buscar: ")
    for i in range(len(lista_nif)):
        if lista_nif[i] == nif:
            print("--------------------------------")
            print("Su NIF es: ",lista_nif[i])
            print("Su Nombre es: ",lista_nombre[i])
            print("Su Edad es: ",lista_edad[i],"años")
            print("¿Pertenece a la Union Europea?: ",lista_pertenece[i])
            print("Estado Conyugal: ",lista_conyugal[i])
            print("--------------------------------")
def imprimir_certificado(certificado):
    print("------CERTIFICADOS------")
    print("1. Certificado de Nacimiento")
    print("2. Situacion Conyugal")
    print("3. Pertenece a Union Europea")
    print("------------------------")
    certificado = int(input("Ingrese la Opcion de CERTIFICADO que desee: "))
    if certificado ==1:
        certificado = "Certificado de Nacimiento"
        print("--------------------------------")
        print("Nombre del Certificado: ",certificado)
        print("Codigo NIF: ",nif)
        print("Nombre de la Persona: ",nombre)
        print("Edad de la Persona: ",edad)
        print("Pertenece a la  Union Europea: ",pertenece)
        print("--------------------------------")
    elif certificado == 2:
        certificado = "Estado Conyugal"
        print("--------------------------------")
        print("Nombre del Certificado: ",certificado)
        print("Codigo NIF: ",nif)
        print("Nombre de la Persona: ",nombre)
        print("Edad de la Persona: ",edad)
        print("Pertenece a la  Union Europea: ",pertenece)
        print("Estado Conyugal: ",conyugal)
        print("--------------------------------")
    elif certificado == 3:
        certificado = "Pertenencia Union Europea"
        print("--------------------------------")
        print("Nombre del Certificado: ",certificado)
        print("Codigo NIF: ",nif)
        print("Nombre de la Persona: ",nombre)
        print("Edad de la Persona: ",edad)
        print("Pertenece a la  Union Europea: ",pertenece)
        print("--------------------------------")
def salir():
    poto == 1
    print("--------------------------------")
    print("Hasta luego\n created by Vicente Tramon\n v.01")
def validador_nif(nif):
    if len(nif) == 12:
        for i in range(len(nif)):
            if nif[8] == "-":
                return False
    return True
def validador_nombre(nombre):
    if len(nombre) >= 8:
        return False
    return True
def validador_edad(edad):
    if edad >= 0:
        return False
    return True
def menu():
    print("------MENU------")
    print("Opcion 1. Grabar NIF")
    print("Opcion 2. Buscar")
    print("Opcion 3. Imprimir Certificados")
    print("Opcion 4. Salir del programa")
while poto == 0:
    menu()
    opcion = int(input("Ingrese la OPCION que desea: "))
    if opcion == 1:
        nif = ""
        nombre = ""
        edad = 0
        pertenece = ""
        conyugal = ""
        while validador_nif(nif):
            nif = input("Ingrese su NIF: ")
        while validador_nombre(nombre):
            nombre = input("Ingrese su Nombre: ")
        edad = int(input("Ingrese su Edad: "))
        if edad >= 0:
            pertenece = str(input("Pertenece a la Union Europea?: "))
        conyugal = input("¿Cual es su estado conyugal?: ")
        grabar(nif,nombre,edad,pertenece,conyugal)
    if opcion == 2:
        nif = ""
        buscar(nif)
    if opcion == 3:
        certificado = ""
        imprimir_certificado(certificado)
    if opcion == 4:
        salir()
        poto = 1