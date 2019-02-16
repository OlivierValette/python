import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server
def sub_connect(client, userdata, flags, rc):
    print("Connected to broker with result code " + str(rc))
    client.suscribe("house/bulb1")
    client.suscribe("house/bulb2")
    client.suscribe("house/bulb3")


# The callback for when a PUBLISH message is received from the server
def sub_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client()
client.on_connect = sub_connect
client.on_message = sub_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()
