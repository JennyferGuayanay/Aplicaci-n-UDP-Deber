# Primer y segundo ejercicio de clases  
import socket
import threading

socketServer=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socketServer.bind(("localhost", 1234))  
print ("Esperando conexiones..")

def tarea(data, direccion):
    mensaje=data.decode()
    print(mensaje, "de", direccion)
    mensaje2="Hola soy el servidor"
    socketServer.sendto(mensaje2.encode(),direccion)

while True:
    data, direccion = socketServer.recvfrom(1024)
    hilo = threading.Thread(target=tarea,args=(data,direccion))
    hilo.start()

