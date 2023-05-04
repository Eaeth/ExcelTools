# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'merge.ui'
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

class Ui_merge(object):
    def setupUi(self, merge):
        if not merge.objectName():
            merge.setObjectName(u"merge")
        merge.resize(800, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(merge.sizePolicy().hasHeightForWidth())
        merge.setSizePolicy(sizePolicy)
        merge.setMinimumSize(QSize(760, 500))
        merge.setMaximumSize(QSize(850, 600))
        self.merge_pages = QStackedWidget(merge)
        self.merge_pages.setObjectName(u"merge_pages")
        self.merge_pages.setGeometry(QRect(0, 0, 800, 550))
        sizePolicy.setHeightForWidth(self.merge_pages.sizePolicy().hasHeightForWidth())
        self.merge_pages.setSizePolicy(sizePolicy)
        self.merge_pages.setMinimumSize(QSize(760, 500))
        self.merge_pages.setMaximumSize(QSize(850, 600))
        self.merge_pages.setLineWidth(0)
        self.merge_open_dir_page = QWidget()
        self.merge_open_dir_page.setObjectName(u"merge_open_dir_page")
        sizePolicy.setHeightForWidth(self.merge_open_dir_page.sizePolicy().hasHeightForWidth())
        self.merge_open_dir_page.setSizePolicy(sizePolicy)
        self.merge_open_dir_page.setMinimumSize(QSize(760, 500))
        self.merge_open_dir_page.setMaximumSize(QSize(850, 600))
        self.merge_open_dir_button = QPushButton(self.merge_open_dir_page)
        self.merge_open_dir_button.setObjectName(u"merge_open_dir_button")
        self.merge_open_dir_button.setGeometry(QRect(0, 0, 800, 550))
        sizePolicy.setHeightForWidth(self.merge_open_dir_button.sizePolicy().hasHeightForWidth())
        self.merge_open_dir_button.setSizePolicy(sizePolicy)
        self.merge_open_dir_button.setMinimumSize(QSize(760, 500))
        self.merge_open_dir_button.setMaximumSize(QSize(850, 600))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setPointSize(20)
        self.merge_open_dir_button.setFont(font)
        self.merge_open_dir_button.setIconSize(QSize(16, 16))
        self.merge_pages.addWidget(self.merge_open_dir_page)
        self.merge_para_page = QWidget()
        self.merge_para_page.setObjectName(u"merge_para_page")
        sizePolicy.setHeightForWidth(self.merge_para_page.sizePolicy().hasHeightForWidth())
        self.merge_para_page.setSizePolicy(sizePolicy)
        self.merge_para_page.setMinimumSize(QSize(760, 500))
        self.merge_para_page.setMaximumSize(QSize(850, 600))
        self.merge_output_path_button = QPushButton(self.merge_para_page)
        self.merge_output_path_button.setObjectName(u"merge_output_path_button")
        self.merge_output_path_button.setGeometry(QRect(0, 320, 800, 50))
        self.merge_output_path_button.setFont(font)
        self.merge_row_heads_label = QLabel(self.merge_para_page)
        self.merge_row_heads_label.setObjectName(u"merge_row_heads_label")
        self.merge_row_heads_label.setGeometry(QRect(410, 250, 281, 50))
        self.merge_row_heads_label.setFont(font)
        self.merge_row_heads_entry = QLineEdit(self.merge_para_page)
        self.merge_row_heads_entry.setObjectName(u"merge_row_heads_entry")
        self.merge_row_heads_entry.setGeometry(QRect(700, 250, 90, 50))
        self.merge_row_heads_entry.setFont(font)
        self.merge_column_entry = QLineEdit(self.merge_para_page)
        self.merge_column_entry.setObjectName(u"merge_column_entry")
        self.merge_column_entry.setGeometry(QRect(300, 250, 90, 50))
        self.merge_column_entry.setFont(font)
        self.merge_column_label = QLabel(self.merge_para_page)
        self.merge_column_label.setObjectName(u"merge_column_label")
        self.merge_column_label.setGeometry(QRect(10, 250, 291, 50))
        self.merge_column_label.setFont(font)
        self.merge_import_label = QLabel(self.merge_para_page)
        self.merge_import_label.setObjectName(u"merge_import_label")
        self.merge_import_label.setGeometry(QRect(0, 0, 800, 50))
        self.merge_import_label.setFont(font)
        self.merge_process_button = QPushButton(self.merge_para_page)
        self.merge_process_button.setObjectName(u"merge_process_button")
        self.merge_process_button.setGeometry(QRect(0, 420, 800, 50))
        self.merge_process_button.setFont(font)
        self.merge_output_path_label = QLabel(self.merge_para_page)
        self.merge_output_path_label.setObjectName(u"merge_output_path_label")
        self.merge_output_path_label.setGeometry(QRect(0, 370, 800, 50))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(10)
        self.merge_output_path_label.setFont(font1)
        self.merge_output_path_label.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.merge_output_path_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse)
        self.merge_import_list_view = QListView(self.merge_para_page)
        self.merge_import_list_view.setObjectName(u"merge_import_list_view")
        self.merge_import_list_view.setGeometry(QRect(0, 50, 800, 180))
        sizePolicy.setHeightForWidth(self.merge_import_list_view.sizePolicy().hasHeightForWidth())
        self.merge_import_list_view.setSizePolicy(sizePolicy)
        self.merge_import_list_view.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.merge_import_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.merge_pages.addWidget(self.merge_para_page)

        self.retranslateUi(merge)

        self.merge_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(merge)
    # setupUi

    def retranslateUi(self, merge):
        merge.setWindowTitle(QCoreApplication.translate("merge", u"merge", None))
        self.merge_open_dir_button.setText(QCoreApplication.translate("merge", u"\u5bfc\u5165\u6587\u4ef6\u5939", None))
        self.merge_output_path_button.setText(QCoreApplication.translate("merge", u"\u8bf7\u9009\u62e9\u8f93\u51fa\u6587\u4ef6", None))
        self.merge_row_heads_label.setText(QCoreApplication.translate("merge", u"\u5408\u5e76\u8868\u683c\u5934\u884c\u6570(1-99):", None))
        self.merge_column_label.setText(QCoreApplication.translate("merge", u"\u5408\u5e76\u6307\u5f15\u5217(\u4f8b\u5982:1\u6216A): ", None))
        self.merge_import_label.setText(QCoreApplication.translate("merge", u"\u5df2\u5bfc\u5165\u6587\u4ef6:", None))
        self.merge_process_button.setText(QCoreApplication.translate("merge", u"\u5f00\u59cb\u5904\u7406", None))
        self.merge_output_path_label.setText("")
    # retranslateUi

