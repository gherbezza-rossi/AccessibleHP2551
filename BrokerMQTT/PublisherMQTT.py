import paho.mqtt.publish as publish


def mqtt_publisher(dictionary):
    publish.multiple(dictionary)


# mqtt_publisher([{'topic': "/weather/a", "payload": 1}, {'topic': "/weather/b", "payload": 2}])
