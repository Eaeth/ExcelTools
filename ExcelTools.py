# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from main_ui import Ui_main
from widget_excel_split import WidgetExcelSplit
from widget_excel_merge import WidgetExcelMerge


class ExcelToolsWindows(QWidget, Ui_main):
    m_widget_split = None
    m_widget_merge = None

    def __init__(self, parent=None):
        super(ExcelToolsWindows, self).__init__(parent)
        self.setupUi(self)

        self.initialize()

    def initialize(self):
        self.m_widget_split = WidgetExcelSplit(self)
        self.m_widget_merge = WidgetExcelMerge(self)

        merge_layout = QVBoxLayout()
        merge_layout.setContentsMargins(0, 0, 0, 0)  # 设置边距为0
        merge_layout.addWidget(self.m_widget_merge)
        self.merge.setLayout(merge_layout)

        split_layout = QVBoxLayout()
        split_layout.setContentsMargins(0, 0, 0, 0)  # 设置边距为0
        split_layout.addWidget(self.m_widget_split)
        self.split.setLayout(split_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ExcelToolsWindows()
    widget.show()
    sys.exit(app.exec())
