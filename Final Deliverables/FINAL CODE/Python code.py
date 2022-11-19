import wiotp.sdk.device
import time
import os
import datetime
import random

myConfig = {
    "identity":{
        "orgId":"vtc6yy",
        "typeId":"NodeMCU",
        "deviceId":"NodeMcu"
        },
    "auth":{
        "token":"12345678"
        }
    }
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

def myCommandCallback(cmd):
    print("Message received from IBM IoT platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    if(m=="Appear"):
        print("Appear")
    elif(m=="Disappear"):
        print("Disappear")
    print(" ")
while True:
    pH=random.randint(0,14)  
    temp=random.randint(-10,25)
    hum=random.randint(0,100)
    myData={'pH':pH,'temperature':temp,'humidity':hum}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data successfully: %s", myData)
    time.sleep(2)
    client.commandCallback = myCommandCallback
client.disconnect()
