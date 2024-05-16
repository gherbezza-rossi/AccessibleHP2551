import logging
import paho.mqtt.client as mqtt

from influxdb.client import InfluxDBClient

from SubscriberMQTT.connection_to_influxdb import write_on_influx

client_influx = InfluxDBClient(username="ester", password="admin2024")


def on_message(userdata, msg):
    if userdata:
        print(f"Saving to influx message {msg.topic}: {msg.payload}")
        write_on_influx(msg.topic, msg.payload)


client = mqtt.Client()

logger = logging.getLogger(__name__)
client.enable_logger(logger)

client.connect("localhost", 1883, 60)
client.subscribe("weather/#")

client.loop_forever()

client.on_message = on_message
