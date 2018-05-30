#!python3
import paho.mqtt.client as mqtt
import time
import sys
import json


# Function log
def on_log(client, userdata, level, buf):
    print("log: "+buf)


# Function to stablish connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection stablished :)")
        print("*********************")
    else:
        print("Disconnected, result code: ", rc)
        print("!!!!!!!!!!!!!!!!!!!!!")


# Function process message
def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8"))
    print("Message received in topic ", m_decode)


# Function to close connection
def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected result code "+str(rc))


# The broker is up and running in localhost
# MQTT Default port will be 1883
# Notice that might be
broker = "127.0.0.1"

# Create new instance for our client
# method client with all parameters -> Client(client_id="", clean_session=True,
# userdata=None, protocol=MQTTv311, transport="tcp")
client = mqtt.Client("test_client")

# Binding call functions
client.on_connect = on_connect
client.on_log = on_log
client.on_message = on_message

# Connnect to broker
# method connect with all parameters ->  Connect(host, port=1883, keepalive=60,
# bind_address="")
print ("")
print ("1")
print("***** Connecting to broker *****", broker)
client.connect(broker)

# Start loop
# We need to start a loop in order to see the callbacks. There is a specfic
# method defined loop_start()
client.loop_start()

# Subscribe test topic
print ("")
print ("2")
print("***** Subscribe to thisIsMyTopic/level *****")
client.subscribe("thisIsMyTopic/level")

# Publish in test message in topic"
# method with all parameters -> publish(topic, payload=None, qos=0, retain=False)
print ("")
print ("3")
print("***** Publish a message in topic thisIsMyTopic/level *****")
client.publish("thisIsMyTopic/level", "Hello MQTT!")
# client.publish("thisIsMyTopic/level", "Hello MQTT! with QoS 1", 1) #This is a QoS1 message

# Sleep
time.sleep(10)

# Disconnect
print ("")
print ("***** Disconnecting *****")
client.loop_stop()  # Stopping the loop
client.disconnect()  # Close connection

