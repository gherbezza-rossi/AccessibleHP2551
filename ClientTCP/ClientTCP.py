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


def connection_packet(command: int):
    heather = [255, 255]
    size = 3
    checksum = (command + size) % 256

    return [bytes(heather), bytes(hex(command), 'utf-8'), bytes(hex(size), 'utf-8'), bytes(hex(checksum), 'utf-8')]


"""
connecting to gateway and sending packet to hp2551
"""