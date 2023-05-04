# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wait.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
    QWidget)
import images_rc

class Ui_wait(object):
    def setupUi(self, wait):
        if not wait.objectName():
            wait.setObjectName(u"wait")
        wait.resize(300, 200)
        wait.setMinimumSize(QSize(300, 200))
        wait.setMaximumSize(QSize(300, 200))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        wait.setFont(font)
        wait.setCursor(QCursor(Qt.WaitCursor))
        icon = QIcon()
        icon.addFile(u":/images/images/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        wait.setWindowIcon(icon)
        self.proc_label = QLabel(wait)
        self.proc_label.setObjectName(u"proc_label")
        self.proc_label.setGeometry(QRect(100, 40, 100, 50))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(20)
        self.proc_label.setFont(font1)
        self.procress_bar = QProgressBar(wait)
        self.procress_bar.setObjectName(u"procress_bar")
        self.procress_bar.setGeometry(QRect(30, 120, 241, 23))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.procress_bar.sizePolicy().hasHeightForWidth())
        self.procress_bar.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(10)
        self.procress_bar.setFont(font2)
        self.procress_bar.setMaximum(0)
        self.procress_bar.setValue(0)
        self.procress_bar.setAlignment(Qt.AlignCenter)
        self.procress_bar.setTextVisible(True)

        self.retranslateUi(wait)

        QMetaObject.connectSlotsByName(wait)
    # setupUi

    def retranslateUi(self, wait):
        wait.setWindowTitle(QCoreApplication.translate("wait", u"\u8868\u683c\u5de5\u5177", None))
        self.proc_label.setText(QCoreApplication.translate("wait", u"\u5904\u7406\u4e2d...", None))
    # retranslateUi

