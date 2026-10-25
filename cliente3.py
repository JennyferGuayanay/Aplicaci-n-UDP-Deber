
import socket
import json
import time

#Configuracion de socket del cliente
socketClient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

direccionServer=("localhost",5000)

while True:
    print("\n1. Registrar usuario")
    print("2. Consultar usuario")
    print("3. Recargar saldo")
    print("4. Salir")

    opcion=input("Ingrese una opcion: ")

    if opcion=="1":
        cedula=input("Cedula: ")
        correo=input("Correo: ")
        telefono=input("Telefono: ")
        nombre=input("Nombre: ")
        saldo=float(input("Saldo: "))

        mensaje2={
            "accion":"registrar",
            "cedula":cedula,
            "correo":correo,
            "telefono":telefono,
            "nombre":nombre,
            "saldo":saldo
        }

    elif opcion=="2":
        cedula=input("Cedula a consultar: ")

        mensaje2={
            "accion":"consultar",
            "cedula":cedula
        }

    elif opcion=="3":
        cedula=input("Cedula: ")
        monto=float(input("Monto a recargar: "))

        mensaje2={
            "accion":"recargar",
            "cedula":cedula,
            "monto":monto
        }

    elif opcion=="4":
        print("Cliente finalizado")
        break

    else:
        print("Opcion no valida")
        continue

    socketClient.sendto(json.dumps(mensaje2).encode(),direccionServer)

    data, direccion=socketClient.recvfrom(1024)
    mensaje=json.loads(data.decode())

    print("Respuesta del servidor: ",mensaje)
    print("/////////////")
    time.sleep(2)

socketClient.close()
