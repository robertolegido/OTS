#!python3
import paho.mqtt.client as mqtt #Import client
import time

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

#Function check disconnnect
def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected result code "+str(rc))

#The broker is up and running in localhost
broker="127.0.0.1"

#Create new instance
client = mqtt.Client("clientito")

#Binding call functions
client.on_connect=on_connect
client.on_log=on_log

#Connnect to broker
print("Connecting to boker ", broker)
client.connect(broker)

#Start loop
client.loop_start()

#Estoy conectadoooo
#Publicacion de prueba"
print("***** Publico mensaje *****")
client.publish("topic/test", "viva el vino")
time.sleep(10)

#Desconectamos
print("Me he desconectado viva")
client.loop_stop()
client.disconnect()
