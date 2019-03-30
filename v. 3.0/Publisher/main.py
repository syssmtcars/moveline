import paho.mqtt.client as mqtt
from time import sleep , time as timer

client = mqtt.Client()


client.connect('192.168.1.141',1883,60)

while True:
    msg = input()
    client.publish('syssmtcars', str(msg))


