from PySide6.QtWidgets import QMainWindow
from ui_caculator import Ui_MainWindow
import time
import paho.mqtt.client as paho
from paho import mqtt
import json

class Mainwindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #dùng lamba để truyền tham số vì nếu không dùng thì khi gọi phương thức clicked hàm self.press_button() sẽ ngay lập tức được chạy trước khi nút được bấm
        self.percentButton.clicked.connect(lambda : self.press_button("%"))
        self.cButton.clicked.connect(lambda : self.press_button("C"))
        self.divineButton.clicked.connect(lambda : self.press_button("/"))
        self.sevenButton.clicked.connect(lambda : self.press_button("7"))
        self.eightButton.clicked.connect(lambda : self.press_button("8"))
        self.nineButton.clicked.connect(lambda : self.press_button("9"))
        self.sixButton.clicked.connect(lambda : self.press_button("6"))
        self.fiveButton.clicked.connect(lambda : self.press_button("5"))
        self.fourButton.clicked.connect(lambda : self.press_button("4"))
        self.threeButton.clicked.connect(lambda : self.press_button("3"))
        self.twoButton.clicked.connect(lambda : self.press_button("2"))
        self.oneButton.clicked.connect(lambda : self.press_button("1"))
        self.addButton.clicked.connect(lambda : self.press_button("+"))
        self.minusButton.clicked.connect(lambda : self.press_button("-"))
        self.multiplyButton.clicked.connect(lambda : self.press_button("x"))
        self.zeroButton.clicked.connect(lambda : self.press_button("0"))

        self.decimalButton.clicked.connect(self.decimalButton_clicked)
        self.arrowButton.clicked.connect(self.remove_it)
        self.equalButton.clicked.connect(self.math_it)
        #tạo một instance ans
        self.ans="0"
        self.ansButton.clicked.connect(self.ans_it)

        # Thiết lập MQTT
        self.client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
        self.client.tls_set(tls_version=paho.ssl.PROTOCOL_TLS)
        self.client.username_pw_set("tuyenr", "Huytuyen2003@")
        self.client.connect("c16306ec0323484d976fe2a940bbcbb4.s1.eu.hivemq.cloud", 8883)
        self.client.on_message = self.on_message
        self.client.subscribe("calculate")
        self.client.loop_start()



   
    def ans_it(self):
        self.outputLabel.setText(self.ans)
    def math_it(self):
        screen = self.outputLabel.text()
        #chuyển dấu x sang * để thực hiện phép tính
        if "x" in screen:
            screen = screen.replace("x","*") 
        try:
            answer=round(eval(screen),5) #hàm eval là một hàm dùng để tính toán trong python đầu vào là một biểu thức dạng chuỗi trả về kết quả biểu thức đó
            self.ans=str(answer)
            self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText("ERROR")
    def remove_it(self):
        screen = self.outputLabel.text()
        screen = screen[:-1]
        self.outputLabel.setText(screen)
    def decimalButton_clicked(self):
        screen = self.outputLabel.text()
        self.outputLabel.setText("{}{}".format(screen,"."))
    def press_button(self,pressed):
        if pressed =="C":
            self.outputLabel.setText("0")
        else:
            if self.outputLabel.text()=="0":
                self.outputLabel.setText("") # xóa kí tự 0 ban đầu
            self.outputLabel.setText("{}{}".format(self.outputLabel.text(),pressed))

    #Được gọi khi client kết nối thành công với broker.
    def on_connect(self,client, userdata, flags, rc, properties=None):
        print("CONNACK received with code %s." % rc)

    #Được gọi khi một tin nhắn được xuất bản thành công.
    def on_publish(self,client, userdata, mid, properties=None):
        print("mid: " + str(mid))

    # Được gọi khi client đăng ký (subscribe) một chủ đề.
    def on_subscribe(self,client, userdata, mid, granted_qos, properties=None):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    # Được gọi khi một tin nhắn mới được nhận.
    def on_message(self,client, userdata, msg):
        json_message=msg.payload
        message_data = json.loads(json_message)
        operation = message_data["operation"]
        operands = message_data["operands"]

        # Thực hiện tính toán dựa trên dữ liệu
        result = None
        try:
            if operation == "addition":
                result = sum(operands)
            elif operation == "subtraction":
                result = operands[0] - operands[1]
            elif operation == "multiplication":
                result = operands[0] * operands[1]
            elif operation == "division":
                result = round((operands[0] / operands[1]),5)
        except:
            result="ERROR"
        # In kết quả tính toán
        #print("Result:", result)
        self.outputLabel.setText(str(result))
        client.publish("calculate/result", payload=result)


    
        #client.on_message = on_message
        #client.on_publish = on_publish
        # subscribe to all topics of encyclopedia by using the wildcard "#"
        #client.subscribe("calculate")

        # a single publish, this can also be done in loops, etc.
    

        # loop_forever for simplicity, here you need to stop the loop manually
        # you can also use loop_start and loop_stop

    


