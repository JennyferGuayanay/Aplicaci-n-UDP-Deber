# Tercer ejercicio de clases  
import socket
import json
import time
#Configuracion de socker del cliente
socketClient=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sensores={
    "S1":["Temperatura",30],
    "S2":["Humedad",30],
    "S3":["Distancia",30],
    "S4":["Nivel agua","medio"]
}
direccionServer=("localhost",5000)

for codigo, datos in sensores.items():
    mensaje2= {"codigo":codigo,
               "sensor":datos[0],
               "valor":datos[1]
               }
    socketClient.sendto(json.dumps(mensaje2).encode(),direccionServer)
    data, direccion = socketClient.recvfrom(1024)
    mensaje=data.decode()
    print(mensaje)
    time.sleep(2)

socketClient.close()
