#!python3
import paho.mqtt.client as mqtt #Import client
import time
import json
import sys

#Create new instance
client = mqtt.Client("clientito")

#Read input json
json_to_test=sys.argv[1]
with open("/home/r/Documents/paho/"+sys.argv[1]) as json_data:
    mqtt = json.load(json_data)

#Load input json
mqttmessage = json.dumps(mqtt)
print("************")
print("JSON to test")
print(mqttmessage)

#Function log
def on_log(client,userdata,level,buf):
    print("log: "+buf)

#Function check connection
def on_connect(client, userdata, flags, rc):
    print("Estoy haciendo algo!")
    if rc==0:
        print("Me he conectado viva :)")
        print("*********************")
    else:
        print("No me he conectado :-( Interneeeet de las cosas, error code: ",rc)
        print("!!!!!!!!!!!!!!!!!!!!!")

#Function process message
def on_message(client, userdata, msg):
    topic=msg.topic
    m_decode=str(msg.payload.decode("utf-8"))
    print("Message received in topic ", m_decode)
#    print("Converting to JSON")
#    m_in=json.loads(m_decode)
#    print(type(m_in))

#Function check disconnnect
def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected result code "+str(rc))

#The broker is up and running in localhost
broker="127.0.0.1"

#Binding call functions
client.on_connect=on_connect
client.on_log=on_log
client.on_message=on_message

#Connnect to broker
print ("")
print ("1")
print("***** Connecting to boker *****", broker)
client.connect(broker)

#Start loop
client.loop_start()

#Subscribe test topic
print ("")
print ("2")
print("***** Subscribe to caca/supercaca *****")
client.subscribe("caca/supercaca",1)

#Publish in test message in topic"
print ("")
print ("3")
print("***** Publish in topic caca/supercaca *****")
#client.publish("caca/supercaca", "AMAZING")
client.publish("caca/supercaca", mqttmessage, 1)
time.sleep(10)

#Disconnect
print ("")
print ("***** Disconnecting *****")
print("Me he desconectado viva")
client.loop_stop()
client.disconnect()
