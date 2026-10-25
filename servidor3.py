
import socket
import threading
import json

socketServer=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socketServer.bind(("localhost",5000))
print("Esperando conexiones..")

usuarios=[]

def registrar(mensaje, direccion):
    aux=False

    for u in usuarios:
        if u["cedula"]==mensaje["cedula"]:
            aux=True
            break

    if aux==True:
        mensaje2={"respuesta":"Usuario ya registrado"}
    else:
        usuario={
            "cedula":mensaje["cedula"],
            "correo":mensaje["correo"],
            "telefono":mensaje["telefono"],
            "nombre":mensaje["nombre"],
            "saldo":mensaje["saldo"]
        }

        usuarios.append(usuario)
        mensaje2={"respuesta":"Usuario registrado correctamente"}

    socketServer.sendto(json.dumps(mensaje2).encode(),direccion)


def consultar(mensaje, direccion):
    aux=False

    for u in usuarios:
        if u["cedula"]==mensaje["cedula"]:
            aux=True
            break

    if aux==True:
        mensaje2={
            "nombre":u["nombre"],
            "cedula":u["cedula"],
            "correo":u["correo"],
            "telefono":u["telefono"],
            "saldo":u["saldo"]
        }
    else:
        mensaje2={"respuesta":"Usuario no encontrado"}

    socketServer.sendto(json.dumps(mensaje2).encode(),direccion)


def recargar(mensaje, direccion):
    aux=False

    for u in usuarios:
        if u["cedula"]==mensaje["cedula"]:
            aux=True
            break

    if aux==True:
        if mensaje["monto"]>0:
            u["saldo"]=u["saldo"]+mensaje["monto"]

            mensaje2={
                "respuesta":"Saldo recargado correctamente",
                "saldo":u["saldo"]
            }
        else:
            mensaje2={"respuesta":"Monto no valido"}
    else:
        mensaje2={"respuesta":"Usuario no encontrado"}

    socketServer.sendto(json.dumps(mensaje2).encode(),direccion)


def tarea(data, direccion):
    mensaje=json.loads(data.decode())

    print(mensaje)
    print("Direccion cliente: ",direccion)

    if mensaje["accion"]=="registrar":
        registrar(mensaje,direccion)

    elif mensaje["accion"]=="consultar":
        consultar(mensaje,direccion)

    elif mensaje["accion"]=="recargar":
        recargar(mensaje,direccion)

    else:
        mensaje2={"respuesta":"Opcion no valida"}
        socketServer.sendto(json.dumps(mensaje2).encode(),direccion)

    print("/////////////")


while True:
    data, direccion=socketServer.recvfrom(1024)
    hilo=threading.Thread(target=tarea,args=(data,direccion))
    hilo.start()
