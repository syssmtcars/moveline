import paho.mqtt.client as mqtt
from forward import move as forward
from left import move as left
from right import move as right
from stop import move as stop
from time import sleep


# This is the Subscriber

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("syssmtcars")


def on_message(client, userdata, msg):

    if str(msg.payload.decode()) == 'right':
        right()

    elif str(msg.payload.decode()) == 'left':
        left()

    elif str(msg.payload.decode()) == 'forward':
        forward()

    elif str(msg.payload.decode()) == 'stop':
        stop()





client = mqtt.Client()
client.connect("192.168.0.34", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()