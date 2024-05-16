from datetime import datetime, UTC
import influxdb_client
from influxdb_client.client.write.point import Point
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.domain.write_precision import WritePrecision


TOKEN_INFLUX = "-Bsx6E7g7jsOPSD1djOguQy_asXTAgAAOpgf70QU4y62VX4BaiUUhLnC45Ic8v24VFpxao_PiUSdh-lkd7SYVA=="
URL_INFLUX = "http://localhost:8086"
ORG_INFLUX = "MyInfluxDB"
BUCKET_INFLUX = "WeatherStation"

client = influxdb_client.InfluxDBClient(url=URL_INFLUX,
                                        token=TOKEN_INFLUX,
                                        org=ORG_INFLUX)

write_api = client.write_api(write_options=SYNCHRONOUS)


def write_on_influx(topic, payload):
    point = Point(topic).field("value", payload).time(datetime.now(UTC), WritePrecision.NS)

    write_api.write(bucket=BUCKET_INFLUX, org=ORG_INFLUX, record=point)


#write_on_influx('temp', 4)
