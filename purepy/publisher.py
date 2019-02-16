import paho.mqtt.client as mqtt
import time


def pub_connect(client, userdata, flags, rc):
    print("Connected to broker with result code " + str(rc))


def pub_publish(client, userdata):
    print("\nData published : " + str(client) + str(userdata))
    pass


client1 = mqtt.Client()
client1.on_connect = pub_connect
client1.on_publish = pub_publish

client1.connect("test.mosquitto.org", 1883, 60)

while True:
    client1.publish("house/bulb1", "on")
    time.sleep(5)
