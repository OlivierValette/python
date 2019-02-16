import paho.mqtt.client as mqtt
import time


def on_connect(pubclient, userdata, flags, rc):
    print("Connected to broker with result code " + str(rc))


def on_publish(client, userdata):
    print("\nData published : " + str(client) + str(userdata))
    pass


pubclient = mqtt.Client()
pubclient.on_connect = on_connect
pubclient.on_publish = on_publish
print("connecting to broker...")
pubclient.connect("test.mosquitto.org", 1883, 60)

while True:
    print("Publishing message to topic", "house/bulb1")
    pubclient.publish("house/bulb1", "on")
    time.sleep(5)
