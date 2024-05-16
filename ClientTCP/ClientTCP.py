import socket
import sys

from ApiDefinition import API_DEFINITIONS
from PublisherMQTT import mqtt_publisher


def request_encoding(command: int = 39):
    """
    source: https://blog.meteodrenthe.nl/2023/02/03/how-to-use-the-ecowitt-gateway-gw1000-gw1100-local-api/

    aim: using the API of the weather station
    parts of the TCP the station requires (using Ecowitt protocol):
    - fixed heather: 2x 0xff bytes
    - command: to establish connection (requiring live data) CMD_GW1000_LIVEDATA 39 (dec)
    - payload: not necessary in this case
    - size: sum of sizes of command, payload, size and checksum (not in hex form)
    - checksum: aggregating the byte values of the command, the size and any optional payload bytes (in module 256) in hex
    """
    heather = [255, 255]
    size = 3
    checksum = (command + size) % 256

    return bytes([255, 255, hex(command), hex(size), hex(checksum)])


def response_decoding(response: list):
    """
    Decoding received response from station's gateway.
    The formatting is:
    - first 2 bytes: fixed heather
    - 3rd byte: command
    - 4th byte: size
    - payload: all the data with the code describing the value (1 byte) and the value in n bytes
    - last byte: checksum

    Process of decoding of the payload:
    - read the marker of the value
    - associate the marker (hex format) with the number of bytes associated with the value
    - removing the '0x' in every byte to obtain the hex value
    - the hex value is converted to decimal

    All the values, with marker byte and value are inserted in a dictionary, where the marker is the topic and the
    payload are an int.

    The dictionary will then be used by the mqtt publisher.
    :param response: list of bytes
    :return: decoded response
    """
    print(response)
    decoded_response = []

    i = 5
    while i < len(response) - 1:
        marker = response[i]
        api = API_DEFINITIONS.get(marker)
        if api is None:
            print(f"Unknown marker {marker}")
            return None

        size = api.size
        value: list = response[(i + 1):(i + 1 + size)]
        for h in range(size):
            value[h] = str(value[h]).replace('0x', '')

        value_str = "".join(value)
        value_int = int(value_str, 16)

        decoded_response.append({"topic": "weather/"+api.name, "payload": value_int})
        i += size + 1

    return decoded_response


def send_smt(s):
    while True:
        command = input("(Q for quitting) -> ")
        if command == "Q":
            print("Closing connection")
            s.close()
            sys.exit()
        else:
            request = request_encoding()
            s.send(request)
            response = s.recv(1024)
            response_list = response.split()
            dictionary = response_decoding(response_list)
            print(dictionary)
            mqtt_publisher(dictionary)


def conn_sub_server(gateway_add=("172.20.10.1", 45000)):
    """
    connecting to gateway and sending packet to hp2551
    source: https://www.programmareinpython.it/video-corso-python-intermedio/07-server-client-tcp-parte-prima/
    """
    try:
        s = socket.socket()
        s.connect(gateway_add)
        print(f"Connection to {gateway_add} done.")
    except socket.error as e:
        print(f"Connection refused: \t{e}")
        sys.exit()
    send_smt(s)


# conn_sub_server()

response_example = ("0xFF 0xFF 0x27 0x00 0x45 0x01 0x00 0x9B 0x06 0x37 0x08 0x27 0xA7 0x09 0x27 0xA7 0x02 0x00 0x35 "
                    "0x07 0x58 0x0A 0x00 0xEA 0x0B 0x00 0x0B 0x0C 0x00 0x0F 0x15 0x00 0x00 0x00 0x00 0x16 0x00 0x00 "
                    "0x17 0x00 0x20 0x00 0x9A 0x28 0x3A 0x19 0x00 0x24 0x0E 0x00 0x00 0x10 0x00 0x19 0x11 0x00 0x30 "
                    "0x12 0x00 0x00 0x00 0x19 0x13 0x00 0x00 0x00 0x30 0x0D 0x00 0x00 0x3B")
