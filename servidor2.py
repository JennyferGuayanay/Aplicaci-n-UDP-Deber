# Tercer ejercicio de clases  
import socket
import threading
import json 

socketServer=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socketServer.bind(("localhost", 5000))  
print ("Esperando conexiones..")

def tarea(data, direccion):
    mensaje=json.loads(data.decode())
    print(mensaje)
    print("Direccion cliente: ", direccion)
    print("Codigo: ", mensaje["codigo"])
    print("Sensor: ",mensaje["sensor"])
    print("Valor: ",mensaje["valor"])
    print("/////////////")
    print(mensaje, "de", direccion)
    mensaje2="Datos recibidos correctamente"
    socketServer.sendto(mensaje2.encode(),direccion)

while True:
    data, direccion = socketServer.recvfrom(1024)
    hilo = threading.Thread(target=tarea,args=(data,direccion))
    hilo.start()

