import logging
from paho.mqtt import client as mqtt

from connection_to_influxdb import write_on_influx


def on_subscribe(client, userdata, mid, reason_code_list, properties):
    # Since we subscribed only for a single channel, reason_code_list contains
    # a single entry
    if reason_code_list[0].is_failure:
        print(f"Broker rejected you subscription: {reason_code_list[0]}")
    else:
        print(f"Broker granted the following QoS: {reason_code_list[0].value}")


def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client_mqtt.subscribe("wee/hi")


def on_message(client, userdata, msg):
    print(f"Saving to influx message {msg.topic}: {msg.payload}")

    write_on_influx(msg.topic, msg.payload)


client_mqtt = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

logger = logging.getLogger(__name__)
client_mqtt.enable_logger(logger)


client_mqtt.on_connect = on_connect
client_mqtt.on_message = on_message
client_mqtt.on_subscribe = on_subscribe

client_mqtt.user_data_set([])
client_mqtt.connect("localhost", 1883, 60)

client_mqtt.loop_forever()

# print(f"Received the following message: {client_mqtt.user_data_get()}")
