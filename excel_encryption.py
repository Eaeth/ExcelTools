# -*- coding: utf-8 -*-

import os
import win32com.client
import pywintypes


class ExcelEncryption:
    def __init__(self, input_path, output_path, password, is_encryption):
        self.input_path = input_path
        self.output_path = output_path
        self.password = password
        self.is_encryption = is_encryption

    def encryption(self):
        try:
            excel = win32com.client.gencache.EnsureDispatch(
                'Excel.Application')
        except pywintypes.com_error:
            try:
                excel = win32com.client.gencache.EnsureDispatch(
                    'KWPS.Application')
                excel.Quit()
                return "请打开 WPS Office 兼容选项\n位置: 设置->组件管理->文件格式关联...->兼容第三方系统和软件"
            except pywintypes.com_error:
                return "未找到 Microsoft Excel 或 WPS Office,请先安装！"
        excel.Visible = False
        excel.DisplayAlerts = False
        files = []
        exist_file_encrypted = False

        try:
            for filename in os.listdir(self.input_path):
                if filename.endswith(('.xls', '.xlsx')):
                    filepath = os.path.join(self.input_path, filename)

                    try:
                        # 用一个不会用到的密码去打开文件，如果文件本身存在密码，则会报错，走下面密码不正确的流程；如果文件没有密码，依然可以正常打开
                        workbook = excel.Workbooks.Open(
                            filepath, Password=self.password)
                    except pywintypes.com_error as e:
                        if ("密码不正确" in str(e)) or ("发生意外" in str(e)):
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
                workbook = excel.Workbooks.Open(
                    filepath, Password=self.password)
                workbook.Password = self.password
                if filename.endswith('.xls'):
                    filename = filename.replace('.xls', '.xlsx')
                save_path = os.path.join(self.output_path, filename)
                save_path = os.path.normpath(save_path)
                workbook.SaveAs(save_path, FileFormat=51)
                workbook.Close()

        finally:
            excel.Quit()

    def decrypt(self):
        try:
            excel = win32com.client.gencache.EnsureDispatch(
                'Excel.Application')
        except pywintypes.com_error:
            try:
                excel = win32com.client.gencache.EnsureDispatch(
                    'KWPS.Application')
                excel.Quit()
                return "请打开 WPS Office 兼容选项\n位置: 设置->组件管理->文件格式关联...->兼容第三方系统和软件"
            except pywintypes.com_error:
                return "未找到 Microsoft Excel 或 WPS Office,请先安装！"

        excel.Visible = False
        excel.DisplayAlerts = False

        try:
            for filename in os.listdir(self.input_path):
                if filename.endswith(('.xls', '.xlsx')):
                    filepath = os.path.join(self.input_path, filename)

                    try:
                        # 用一个不会用到的密码去打开文件，如果文件本身存在密码，则会报错，走下面密码不正确的流程；如果文件没有密码，依然可以正常打开
                        workbook = excel.Workbooks.Open(
                            filepath, Password=self.password)
                    except pywintypes.com_error as e:
                        if ("密码不正确" in str(e)) or ("发生意外" in str(e)):
                            return f"{os.path.normpath(filepath)} 密码错误，请核对文件！"
                        else:
                            return str(e)

                    output_filepath = os.path.join(self.output_path, filename)
                    if output_filepath.endswith('.xls'):
                        output_filepath = output_filepath.replace(
                            '.xls', '.xlsx')
                    if os.path.exists(output_filepath):
                        workbook.Close()
                        return f"冲突文件: {os.path.normpath(output_filepath)} \n文件已经存在,请删除该文件或更改输出路径。"

                    if filename.endswith('.xls'):
                        filename = filename.replace('.xls', '.xlsx')
                    workbook.Password = ''
                    save_path = os.path.join(self.output_path, filename)
                    save_path = os.path.normpath(save_path)
                    workbook.SaveAs(save_path, FileFormat=51)
                    workbook.Close()

        finally:
            excel.Quit()

    def encryption_excels(self):
        if self.is_encryption:
            return self.encryption()
        else:
            return self.decrypt()
