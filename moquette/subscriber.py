import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected to broker with result code " + str(rc))
    # Subscribing in sub_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    print("Subscribing to topic", "house/bulb1")
    client.suscribe("house/bulb1")
    print("Subscribing to topic", "house/bulb2")
    client.suscribe("house/bulb2")
    print("Subscribing to topic", "house/bulb3")
    client.suscribe("house/bulb3")


# The callback for when a PUBLISH message is received from the server
def on_message(subclient, userdata, msg):
    print("Received message : " + str(msg.payload.decode("utf-8")) +
          " on topic : " + msg.topic + " with QoS " + str(msg.qos))


print("Creating new instance")
subclient = mqtt.Client("HB")

# attach functions to callbacks
subclient.on_connect = on_connect
subclient.on_message = on_message

print("Connecting to broker...")
subclient.connect("iot.eclipse.org", 1883, 60)

print("... and waiting for messages")
subclient.loop_forever()
