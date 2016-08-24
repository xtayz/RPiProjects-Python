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

while 1:
    conn, addr = sock.accept()
    print('Connected by:', addr)
    try:
        while 1:
            data = conn.recv(1024)
            if not data.strip():
                print('recv is null')
                break

            print('--------------------------------------')
            print(conn.recv(1024))
            print(b'\xe5\x93\x88\xe5\x93\x88\xe5\x93\x88'.decode('utf-8'))
            print('--------------------------------------')
            print(conn.recv(1024).decode())
            print('--------------------------------------')
            print(conn.recv(1024).decode('utf-8').strip())
            print('--------------------------------------')
            command = conn.recv(1024).replace('\n', '')
            if not command:
                break
            execute(command)
            # conn.send('Done!')
            # conn.close()

    except Exception as e:
        print('Exception: ', e)
        sock.shutdown(SHUT_RDWR)
        conn.close()
        sock.close()
        print('socket closed!')
