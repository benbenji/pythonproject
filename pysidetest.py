"""
用pyside实现一个计算器
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit

class Calculator(QWidget):

    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 300, 400)

        layout = QVBoxLayout()

        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for button in buttons:
            button_object = QPushButton(button)
            button_object.clicked.connect(self.button_clicked)
            layout.addWidget(button_object)

        self.setLayout(layout)

    def button_clicked(self):
        button = self.sender().text()
        if button == '=':
            try:
                result = str(eval(self.line_edit.text()))
                self.line_edit.setText(result)
            except Exception as e:
                self.line_edit.setText('Error')
        else:
            self.line_edit.setText(self.line_edit.text() + button)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())