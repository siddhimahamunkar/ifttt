import socket
import time
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setup(5,gpio.IN)

server=socket.socket()
server.bind(('172.20.10.2',1233))
server.listen(10)
conn,addr=server.accept()

while True:
    time.sleep(2)

    x=gpio.input(5)

    if x==0:
        print("No intruder")
        time.sleep(5)

    if x==1:
        print('Intruder detected')
        conn.sendall("detected".encode())
