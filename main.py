from PySide6.QtWidgets import QApplication
from mainwindow import Mainwindow

import sys #import các thư viện hệ thống
if __name__  == "__main__":
    app= QApplication(sys.argv) #tạo một đối tượng
    window=Mainwindow() #tạo một cửa sổ cho app
    window.show()
    app.exec() #bắt đầu 1 vòng lặp lệnh khởi tạo
    
