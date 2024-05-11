# source: https://www.programmareinpython.it/video-corso-python-intermedio/08-server-client-tcp-parte-seconda/
import socket
import subprocess


def receive(conn):
    while True:
        request = conn.recv(4096)
        response = subprocess.run(request.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        data = response.stdout + response.stderr
        conn.sendall(data)


def sub_server(socket_client, backlog=1):
    server = socket.socket()

    try:
        server.bind(socket_client)
        server.listen(backlog)
        print("Server stated. Listening")

    except socket.error as e:
        print(f"Error:  --> \t{e}")
        print(f"Trying again...")
        sub_server(socket_client, backlog=1)

    conn, client_info = server.accept()
    print(f"Connection positive: {client_info}")
    receive(conn)
