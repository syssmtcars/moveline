import paho.mqtt.client as mqtt
from time import sleep , time as timer

client = mqtt.Client()

msg = input()
client.connect('192.168.0.34',1883,60)


client.publish('syssmtcars', str(msg))


