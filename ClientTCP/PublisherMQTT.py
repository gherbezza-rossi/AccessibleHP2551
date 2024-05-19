import paho.mqtt.publish as publish


def mqtt_publisher(dictionary):
    publish.multiple(dictionary)
    print("published")


# mqtt_publisher([{'topic': "weather/temp", "payload": 10}, {'topic': "weather/humidity", "payload": 15}])
