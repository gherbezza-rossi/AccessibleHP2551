from ServerTCP.ServerTCP import sub_server


def use_server():
    ip_client = "192.168.0.1"
    port_client = 40567
    sub_server((ip_client, port_client))


if __name__ == '__main__':
    use_server()

