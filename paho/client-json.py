#!python3
import paho.mqtt.client as mqtt
import time
import json
import sys

# Using json - probably our MQTT! :) 
with open("/home/r/Documents/paho/brokers.json") as json_data:
    brokers_out = json.load(json_data)

print(brokers_out)

data_out=json.dumps(brokers_out)# encode oject to JSON 
print("")
print("Converting to JSON")
print("*********************")
print ("data -type ",type(data_out))
print ("data out =",data_out)


#At Receiver
print("Received Data")
data_in=data_out
print ("data in-type ",type(data_in))
print ("data in=",data_in)
brokers_in=json.loads(data_in) #convert incoming JSON to object
print("brokers_in is a ",type(brokers_in))
print("")
print("")
print("broker 2 address = ",brokers_in["broker1"])

###########
###########
def on_message(client, userdata, msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    print("data Received type",type(m_decode))
    print("data Received",m_decode)
    print("Converting from Json to Object")
    m_in=json.loads(m_decode)
    print(type(m_in))
    #print("broker 2 address = ",m_in["broker2"])

##############################
##############################
topic="test/json_test"



client=mqtt.Client("pythontest1")
client.on_message=on_message
print("Connecting to broker ",brokers_out["broker1"])
client.connect(brokers_out["broker1"])
client.loop_start()
client.subscribe(topic)
time.sleep(3)
print("sending data")
client.publish(topic,data_out)
time.sleep(10)
client.loop_stop()
client.disconnect()
