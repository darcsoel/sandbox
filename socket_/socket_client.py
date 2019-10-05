import socket

HOST = '127.0.0.1'
PORT = 25025

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    client.send(b"I am CLIENT\n")
    from_server = client.recv(4096)
    client.close()
    print(from_server)
