import paho.mqtt.client as mqtt
from time import sleep , time as timer

client = mqtt.Client()

msg = input()
client.connect('192.168.0.34',1883,60)


client.publish('syssmtcars', str(msg))



<<<<<<< HEAD
=======

>>>>>>> 5cec6b08afb851f8c5de7be73e0b385ac53b9b89
