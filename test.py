import paho.mqtt.client as mqtt
import time
unacked_publish=set()
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.connect("broker.chanakancloud.net",1883,60)
mqttc.loop_start()
msg = mqttc.publish("LCDMonitorInfo","Placing",qos=1)
unacked_publish.add(msg.mid)
while len(unacked_publish):
    time.sleep(0.1)
msg.wait_for_publish()
mqttc.disconnect()
mqttc.loop_stop()