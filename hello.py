# 导入sys
import sys

# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QObject, Signal, Slot
# 导入我们生成的界面
from ui import Ui_Form
 
# 继承QWidget类，以获取其属性和方法
class MyWidget(QWidget):
    mysingal = Signal(str)
    def __init__(self):
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Form()
        
        self.ui.setupUi(self)
        self.label = self.ui.label1
        self.pushButton = self.ui.pushButton1
        self.pushButton.clicked.connect(self.button_clicked)
        self.mysingal.connect(self.myslot)
    def button_clicked(self):
        self.mysingal.emit('Hello haha')
        self.label.setText('Hello World')
    def myslot(self, text):
        print(text)
# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)
 
    # 初始化并展示我们的界面组件
    window = MyWidget()
    window.show()
    
    # 结束QApplication
    sys.exit(app.exec())
