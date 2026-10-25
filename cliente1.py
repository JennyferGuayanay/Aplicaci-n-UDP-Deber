# Primer y segundo ejercicio de clases  
import socket
#Configuracion de socker del cliente
socketClient=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

direccionServer=("localhost",5000)

while True: 
    mensaje2= input("Hola soy el cliente: ")

    if mensaje2.lower() == "salir":
        break
    socketClient.sendto(mensaje2.encode(), direccionServer)

    data, direccion = socketClient.recvfrom(1024)
    mensaje=data.decode()
    print(mensaje, "de", direccion)
socketClient.close()



