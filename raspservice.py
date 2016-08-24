#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
# from car import Car

# commands = {
#     'forward': Car.forward(),
#     'back': Car.back(),
#     'left': Car.turn_left(),
#     'right': Car.turn_right()
# }


def execute(command):
    print(command)
    # commands[command]()

HOST = '0.0.0.0'
PORT = 9876

sock = socket(AF_INET, SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
print('listening on %s:%d' % (HOST, PORT))

while True:
    conn, addr = sock.accept()
    print('Connected by:', addr)
    try:
        while True:
            data = conn.recv(1024)
            if not data.strip():
                print('recv is null')
                break
            command = data.decode('utf-8').replace('\n', '')
            if not command:
                break
            execute(command)
            conn.send('Done!'.encode('utf-8'))

    except Exception as e:
        print('Exception: ', e)
        sock.shutdown(SHUT_RDWR)
        conn.close()
        sock.close()
        print('socket closed!')
