# -*- coding: utf-8 -*-

import os
import win32com.client
import pywintypes


class ExcelEncryption:
    def __init__(self, input_path, output_path, password):
        self.input_path = input_path
        self.output_path = output_path
        self.password = password

    def encryption_excels(self):

        excel = win32com.client.gencache.EnsureDispatch('Excel.Application')
        excel.Visible = False
        files = []
        exist_file_encrypted = False

        try:
            for filename in os.listdir(self.input_path):
                if filename.endswith(('.xls', '.xlsx')):
                    filepath = os.path.join(self.input_path, filename)

                    try:
                        workbook = excel.Workbooks.Open(
                            filepath, Password=self.password)
                    except pywintypes.com_error as e:
                        workbook.Close()
                        if "密码不正确" in str(e):
                            exist_file_encrypted = True
                            file_encrypted = filepath
                            break
                        else:
                            return str(e)

                    output_filepath = os.path.join(self.output_path, filename)
                    if output_filepath.endswith('.xls'):
                        output_filepath = output_filepath.replace(
                            '.xls', '.xlsx')
                    if os.path.exists(output_filepath):
                        workbook.Close()
                        return f"冲突文件: {os.path.normpath(output_filepath)} \n文件已经存在,请删除该文件或更改输出路径。"

                    files.append(filename)
                    workbook.Close()

            if exist_file_encrypted:
                return f"{os.path.normpath(file_encrypted)} 已加密，无需再次加密，请先去除已加密文件"

            for filename in files:
                filepath = os.path.join(self.input_path, filename)
                workbook = excel.Workbooks.Open(filepath)
                workbook.Password = self.password
                if filename.endswith('.xls'):
                    filename = filename.replace('.xls', '.xlsx')
                save_path = os.path.join(self.output_path, filename)
                save_path = os.path.normpath(save_path)
                workbook.SaveAs(save_path, FileFormat=51)
                workbook.Close()

        finally:
            excel.Quit()
