import socket


def create_drive(username):
    TCP_IP = '192.168.10.14'
    TCP_PORT = 6972
    BUFFER_SIZE = 1024
    MESSAGE = str(username)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()

    print "received data:", data


