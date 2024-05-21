from ApiDefinition import API_DEFINITIONS


def decode_dict(d):
    out = ""
    for key, value in d.items():
        api = API_DEFINITIONS.get(key)
        out += " "+key
        value = value / api.operation
        value_bytes = "00000000"+str(hex(int(value)))[2:]
        print(value_bytes)
        value_out = ""
        for i in range(api.size):
            print(value_bytes[len(value_bytes)-2-i*2:len(value_bytes)-i*2])
            value_out = " 0x"+value_bytes[len(value_bytes)-2-i*2:len(value_bytes)-i*2] + value_out
        out += value_out

    return out


def make_response():
    r = "0xFF 0xFF 0x27 0x00"
    dictionary = {"0x01": 19.8, "0x06": 24}
    r += decode_dict(dictionary)
    r += " 0x00"
    return r
