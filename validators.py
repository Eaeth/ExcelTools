# -*- coding: utf-8 -*-

from PySide6.QtGui import QValidator
from openpyxl.utils.cell import column_index_from_string

class RowValidator(QValidator):
    def __init__(self, max_value=1000000):
        super().__init__()
        self.max_value = max_value

    def validate(self, value, pos):
        if value.isdigit() and 1 <= int(value) <= self.max_value:
            return (QValidator.Acceptable, value, pos)
        elif value == "":
            return (QValidator.Acceptable, value, pos)
        else:
            return (QValidator.Invalid, value, pos)


class ColumnValidator(QValidator):
    def validate(self, value, pos):
        try:
            if value.isdigit():
                if 1 <= int(value) <= 10000:
                    return (QValidator.Acceptable, value, pos)
                else:
                    return (QValidator.Invalid, value, pos)
            elif value.isalpha():
                try:
                    column_index_from_string(value)
                    return (QValidator.Acceptable, value, pos)
                except:
                    return (QValidator.Invalid, value, pos)
            elif value == "":
                return (QValidator.Acceptable, value, pos)
            else:
                return (QValidator.Invalid, value, pos)
        except:
            return (QValidator.Invalid, value, pos)