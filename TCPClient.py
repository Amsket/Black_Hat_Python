#Script videjo del libro.

""" import socket
import requests

target_host = "www.google.com"
target_port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host,target_port))

#send data
request = "GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
client.send(request.encode())  # convertir a bytes

#receive data
response = client.recv(4096)

print(response) """

import requests

url = "https://www.python.org/"

# Hacemos la solicitud GET
response = requests.get(url)

# Guardar la respuesta en un archivo txt

with open("log_request_python_org.txt", "w", encoding="utf-8") as archivo:
  archivo.write(response.text)
