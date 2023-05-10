# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'encryption.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QLabel, QLineEdit,
    QListView, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)

class Ui_encryption(object):
    def setupUi(self, encryption):
        if not encryption.objectName():
            encryption.setObjectName(u"encryption")
        encryption.resize(800, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(encryption.sizePolicy().hasHeightForWidth())
        encryption.setSizePolicy(sizePolicy)
        encryption.setMinimumSize(QSize(760, 500))
        encryption.setMaximumSize(QSize(850, 600))
        self.encryption_pages = QStackedWidget(encryption)
        self.encryption_pages.setObjectName(u"encryption_pages")
        self.encryption_pages.setGeometry(QRect(0, 0, 800, 550))
        sizePolicy.setHeightForWidth(self.encryption_pages.sizePolicy().hasHeightForWidth())
        self.encryption_pages.setSizePolicy(sizePolicy)
        self.encryption_pages.setMinimumSize(QSize(760, 500))
        self.encryption_pages.setMaximumSize(QSize(850, 600))
        self.encryption_pages.setLineWidth(0)
        self.encryption_open_dir_page = QWidget()
        self.encryption_open_dir_page.setObjectName(u"encryption_open_dir_page")
        sizePolicy.setHeightForWidth(self.encryption_open_dir_page.sizePolicy().hasHeightForWidth())
        self.encryption_open_dir_page.setSizePolicy(sizePolicy)
        self.encryption_open_dir_page.setMinimumSize(QSize(760, 500))
        self.encryption_open_dir_page.setMaximumSize(QSize(850, 600))
        self.encryption_open_dir_button = QPushButton(self.encryption_open_dir_page)
        self.encryption_open_dir_button.setObjectName(u"encryption_open_dir_button")
        self.encryption_open_dir_button.setGeometry(QRect(0, 0, 800, 550))
        sizePolicy.setHeightForWidth(self.encryption_open_dir_button.sizePolicy().hasHeightForWidth())
        self.encryption_open_dir_button.setSizePolicy(sizePolicy)
        self.encryption_open_dir_button.setMinimumSize(QSize(760, 500))
        self.encryption_open_dir_button.setMaximumSize(QSize(850, 600))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(20)
        self.encryption_open_dir_button.setFont(font)
        self.encryption_open_dir_button.setIconSize(QSize(16, 16))
        self.encryption_pages.addWidget(self.encryption_open_dir_page)
        self.encryption_para_page = QWidget()
        self.encryption_para_page.setObjectName(u"encryption_para_page")
        sizePolicy.setHeightForWidth(self.encryption_para_page.sizePolicy().hasHeightForWidth())
        self.encryption_para_page.setSizePolicy(sizePolicy)
        self.encryption_para_page.setMinimumSize(QSize(760, 500))
        self.encryption_para_page.setMaximumSize(QSize(850, 600))
        self.encryption_output_path_button = QPushButton(self.encryption_para_page)
        self.encryption_output_path_button.setObjectName(u"encryption_output_path_button")
        self.encryption_output_path_button.setGeometry(QRect(0, 320, 800, 50))
        self.encryption_output_path_button.setFont(font)
        self.encryption_input_entry = QLineEdit(self.encryption_para_page)
        self.encryption_input_entry.setObjectName(u"encryption_input_entry")
        self.encryption_input_entry.setGeometry(QRect(200, 250, 600, 50))
        self.encryption_input_entry.setFont(font)
        self.encryption_input_label = QLabel(self.encryption_para_page)
        self.encryption_input_label.setObjectName(u"encryption_input_label")
        self.encryption_input_label.setGeometry(QRect(10, 250, 180, 50))
        self.encryption_input_label.setFont(font)
        self.encryption_import_label = QLabel(self.encryption_para_page)
        self.encryption_import_label.setObjectName(u"encryption_import_label")
        self.encryption_import_label.setGeometry(QRect(0, 0, 800, 50))
        self.encryption_import_label.setFont(font)
        self.encryption_process_button = QPushButton(self.encryption_para_page)
        self.encryption_process_button.setObjectName(u"encryption_process_button")
        self.encryption_process_button.setGeometry(QRect(0, 420, 800, 50))
        self.encryption_process_button.setFont(font)
        self.encryption_output_path_label = QLabel(self.encryption_para_page)
        self.encryption_output_path_label.setObjectName(u"encryption_output_path_label")
        self.encryption_output_path_label.setGeometry(QRect(0, 370, 800, 50))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(10)
        self.encryption_output_path_label.setFont(font1)
        self.encryption_output_path_label.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.encryption_output_path_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.encryption_import_list_view = QListView(self.encryption_para_page)
        self.encryption_import_list_view.setObjectName(u"encryption_import_list_view")
        self.encryption_import_list_view.setGeometry(QRect(0, 50, 800, 180))
        sizePolicy.setHeightForWidth(self.encryption_import_list_view.sizePolicy().hasHeightForWidth())
        self.encryption_import_list_view.setSizePolicy(sizePolicy)
        self.encryption_import_list_view.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.encryption_import_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.encryption_pages.addWidget(self.encryption_para_page)

        self.retranslateUi(encryption)

        self.encryption_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(encryption)
    # setupUi

    def retranslateUi(self, encryption):
        encryption.setWindowTitle(QCoreApplication.translate("encryption", u"encryption", None))
        self.encryption_open_dir_button.setText(QCoreApplication.translate("encryption", u"\u5bfc\u5165\u6587\u4ef6\u5939", None))
        self.encryption_output_path_button.setText(QCoreApplication.translate("encryption", u"\u8bf7\u9009\u62e9\u8f93\u51fa\u6587\u4ef6", None))
        self.encryption_input_label.setText(QCoreApplication.translate("encryption", u"\u8bf7\u8f93\u5165\u5bc6\u7801\uff1a", None))
        self.encryption_import_label.setText(QCoreApplication.translate("encryption", u"\u5df2\u5bfc\u5165\u6587\u4ef6:", None))
        self.encryption_process_button.setText(QCoreApplication.translate("encryption", u"\u5f00\u59cb\u5904\u7406", None))
        self.encryption_output_path_label.setText("")
    # retranslateUi

