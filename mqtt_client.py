import time
import paho.mqtt.client as paho
from paho import mqtt
import json

#Được gọi khi client kết nối thành công với broker.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

#Được gọi khi một tin nhắn được xuất bản thành công.
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# Được gọi khi client đăng ký (subscribe) một chủ đề.
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# Được gọi khi một tin nhắn mới được nhận.
def on_message(client, userdata, msg):
    json_message=msg.payload
    message_data = json.loads(json_message)
    operation = message_data["operation"]
    operands = message_data["operands"]

    # Thực hiện tính toán dựa trên dữ liệu
    result = None

    if operation == "addition":
        result = sum(operands)
    elif operation == "subtraction":
        result = operands[0] - operands[1]
    elif operation == "multiplication":
        result = operands[0] * operands[1]
    elif operation == "division":
        result = operands[0] / operands[1]

    # In kết quả tính toán
    print("Result:", result)
    client.publish("calculate/result", payload=result)


# using MQTT version 5 here, for 3.1.1: MQTTv311, 3.1: MQTTv31
# userdata is user defined data of any type, updated by user_data_set()
# client_id is the given name of the client
if __name__ == "__main__":
    client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
        #client.on_connect = on_connect
        #kết nối an toàn 
    client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
        # set username and password
    client.username_pw_set("tuyenr", "Huytuyen2003@")
        # connect to HiveMQ Cloud on port 8883 (default for MQTT)

    client.connect("c16306ec0323484d976fe2a940bbcbb4.s1.eu.hivemq.cloud", 8883)

        # cài đặt lệnh gọi lại sử dụng các hàm ở trên để hiển thị rõ hơn
        #client.on_subscribe = on_subscribe
    
    client.on_message = on_message
    #client.on_publish = on_publish
    # subscribe to all topics of encyclopedia by using the wildcard "#"
    client.subscribe("calculate")

    # a single publish, this can also be done in loops, etc.
   

    # loop_forever for simplicity, here you need to stop the loop manually
    # you can also use loop_start and loop_stop

    client.loop_forever()
