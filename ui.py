# -*- coding: utf-8 -*-



################################################################################

## Form generated from reading UI file 'untitled.ui'

##

## Created by: Qt User Interface Compiler version 6.7.0

##

## WARNING! All changes made in this file will be lost when recompiling UI file!

################################################################################



from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,

    QMetaObject, QObject, QPoint, QRect,

    QSize, QTime, QUrl, Qt)

from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,

    QFont, QFontDatabase, QGradient, QIcon,

    QImage, QKeySequence, QLinearGradient, QPainter,

    QPalette, QPixmap, QRadialGradient, QTransform)

from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,

    QWidget)



class Ui_Form(object):

    def setupUi(self, Form):

        if not Form.objectName():

            Form.setObjectName(u"Form")

        Form.resize(400, 300)

        self.label1 = QLabel(Form)

        self.label1.setObjectName(u"label1")

        self.label1.setGeometry(QRect(140, 80, 91, 71))

        font = QFont()

        font.setPointSize(15)

        self.label1.setFont(font)

        self.pushButton1 = QPushButton(Form)

        self.pushButton1.setObjectName(u"pushButton1")

        self.pushButton1.setGeometry(QRect(150, 170, 75, 23))



        self.retranslateUi(Form)



        QMetaObject.connectSlotsByName(Form)

    # setupUi



    def retranslateUi(self, Form):

        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))

        self.label1.setText(QCoreApplication.translate("Form", u"\u4f60\u597d\u4e16\u754c", None))

        self.pushButton1.setText(QCoreApplication.translate("Form", u"\u6309\u94ae", None))

    # retranslateUi



