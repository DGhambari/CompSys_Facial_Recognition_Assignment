import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import sys
import time
import json
from sense_hat import SenseHat
from occupant_detection import check_presence
from facial_req import detect

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("Connection Result: " + str(rc))

def on_publish(client, obj, mid):
    print("Message ID: " + str(mid))    

mqttc = mqtt.Client()

# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

# parse mqtt url for connection details
url_str = sys.argv[1]
print(url_str)
url = urlparse(url_str)
base_topic = url.path[1:]

# Connect
if (url.username):
    mqttc.username_pw_set(url.username, url.password)

mqttc.connect(url.hostname, url.port)
mqttc.loop_start()

# Publish the occupants list at the beginning and continuously scan for intruders
while True:
    occupants=check_presence()
    occupants_json=json.dumps({"occupants":occupants})
    mqttc.publish(base_topic+"/occupants", occupants_json)
    detect()
    time.sleep(10)