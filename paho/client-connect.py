#!python3
import paho.mqtt.client as mqtt #Import client
import time

#The broker is up and running in localhost
broker="localhost"

#Create new instance
client = mqtt.Client("python1" )

#Connnect to broker
print("Connecting to boker ", broker)
client.connect(broker)

#Estoy conectadoooo
time.sleep(4)

#Desconectamos
print("Me desconecto")
client.disconnect()
