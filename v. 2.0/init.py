import paho.mqtt.client as mqtt
from forward import move as forward
from left import move as left
from right import move as right
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

<<<<<<< HEAD

=======
>>>>>>> 5cec6b08afb851f8c5de7be73e0b385ac53b9b89




client = mqtt.Client()
client.connect("192.168.0.34", 1883, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
