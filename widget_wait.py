# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QDialog
from wait_ui import Ui_wait


class WidgetWait(QDialog, Ui_wait):
    def __init__(self, parent=None):
        super(WidgetWait, self).__init__(parent)
        self.setupUi(self)
