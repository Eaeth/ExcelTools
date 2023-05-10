# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)
import images_rc

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(805, 610)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main.sizePolicy().hasHeightForWidth())
        main.setSizePolicy(sizePolicy)
        main.setMinimumSize(QSize(805, 610))
        main.setMaximumSize(QSize(805, 610))
        icon = QIcon()
        icon.addFile(u":/images/images/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        main.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolsWidget = QTabWidget(main)
        self.toolsWidget.setObjectName(u"toolsWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.toolsWidget.sizePolicy().hasHeightForWidth())
        self.toolsWidget.setSizePolicy(sizePolicy1)
        self.toolsWidget.setMinimumSize(QSize(760, 570))
        self.toolsWidget.setMaximumSize(QSize(840, 630))
        self.toolsWidget.setLayoutDirection(Qt.LeftToRight)
        self.toolsWidget.setAutoFillBackground(False)
        self.toolsWidget.setStyleSheet(u"")
        self.toolsWidget.setTabPosition(QTabWidget.North)
        self.toolsWidget.setTabShape(QTabWidget.Rounded)
        self.toolsWidget.setIconSize(QSize(192, 50))
        self.toolsWidget.setElideMode(Qt.ElideMiddle)
        self.toolsWidget.setUsesScrollButtons(True)
        self.toolsWidget.setDocumentMode(False)
        self.toolsWidget.setTabsClosable(False)
        self.toolsWidget.setMovable(False)
        self.toolsWidget.setTabBarAutoHide(True)
        self.split = QWidget()
        self.split.setObjectName(u"split")
        sizePolicy1.setHeightForWidth(self.split.sizePolicy().hasHeightForWidth())
        self.split.setSizePolicy(sizePolicy1)
        self.split.setMinimumSize(QSize(760, 500))
        self.split.setMaximumSize(QSize(850, 600))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/splite.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolsWidget.addTab(self.split, icon1, "")
        self.merge = QWidget()
        self.merge.setObjectName(u"merge")
        sizePolicy1.setHeightForWidth(self.merge.sizePolicy().hasHeightForWidth())
        self.merge.setSizePolicy(sizePolicy1)
        self.merge.setMinimumSize(QSize(760, 500))
        self.merge.setMaximumSize(QSize(840, 600))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/merge.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolsWidget.addTab(self.merge, icon2, "")
        self.encryption = QWidget()
        self.encryption.setObjectName(u"encryption")
        icon3 = QIcon()
        icon3.addFile(u":/images/images/password.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolsWidget.addTab(self.encryption, icon3, "")

        self.verticalLayout.addWidget(self.toolsWidget)


        self.retranslateUi(main)

        self.toolsWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"\u8868\u683c\u5de5\u5177", None))
        self.toolsWidget.setTabText(self.toolsWidget.indexOf(self.split), QCoreApplication.translate("main", u"\u8868\u683c\u5206\u5272", None))
        self.toolsWidget.setTabText(self.toolsWidget.indexOf(self.merge), QCoreApplication.translate("main", u"\u8868\u683c\u5408\u5e76", None))
        self.toolsWidget.setTabText(self.toolsWidget.indexOf(self.encryption), QCoreApplication.translate("main", u"\u8868\u683c\u52a0\u5bc6", None))
    # retranslateUi

