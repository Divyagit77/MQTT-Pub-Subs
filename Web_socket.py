import time
import paho.mqtt.client as paho
from paho import mqtt

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
client = paho.Client(client_id="nu-able-divya-test", userdata=None, protocol=paho.MQTTv311, transport='websockets')
client.on_connect = on_connect

# enable TLS for secure connection
#client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
#client.username_pw_set("divyapriya_dhanraj", "Divya@hivemq23")


# connect to HiveMQ Cloud on port 8883 (default for MQTT)
# client.connect("a9da7498ddbd475eb817b02fb90e73e9.s1.eu.hivemq.cloud", 8883)
client.connect("broker.mqttdashboard.com", 8000)


# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message
client.on_publish = on_publish

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("testtopic/1356585", qos=1)

# a single publish, this can also be done in loops, etc.
client.publish("testtopic/68144686", payload="Hello world from Divya", qos=1)


# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_forever()