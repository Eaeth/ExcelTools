# -*- coding: utf-8 -*-

import os
from PySide6.QtWidgets import QMessageBox, QWidget, QFileDialog
from PySide6.QtCore import QStringListModel
from encryption_ui import Ui_encryption
from worker_thread import WorkerThread
from excel_encryption import ExcelEncryption
from widget_wait import WidgetWait


class WidgetExcelEncryption(QWidget, Ui_encryption):
    def __init__(self, parent=None):
        super(WidgetExcelEncryption, self).__init__(parent)

        self.setupUi(self)

        self.model = QStringListModel()

        self.worker_thread = WorkerThread()
        self.worker_thread.finished_signal().finished.connect(self.task_finished)
        self.worker_thread.started.connect(self.start_wait)

        self.encryption_open_dir_button.clicked.connect(self.get_file_list)
        self.encryption_output_path_button.clicked.connect(
            self.choose_output_path)
        self.encryption_input_entry.textChanged.connect(
            self.on_password_entry_changed)
        self.encryption_process_button.clicked.connect(self.run_worker)
        self.encryption_pages.currentChanged.connect(
            self.on_current_widget_changed)
        self.encryption_pages.setCurrentWidget(self.encryption_open_dir_page)
        self.password = None

    def task_finished(self, success, result):
        # 处理任务完成信号，显示结果或者错误信息
        self.encryption_process_button.setEnabled(True)
        self.wait.hide()
        if success:
            QMessageBox.information(self, "成功", "处理完成，请核验结果!")
        else:
            QMessageBox.critical(self, "错误", str(result))

        self.encryption_pages.setCurrentWidget(self.encryption_open_dir_page)
        self.worker_thread.quit()
        self.worker_thread.wait()

    def start_wait(self):
        self.wait = WidgetWait()
        self.wait.exec()

    def get_file_list(self):
        file_list_path = QFileDialog.getExistingDirectory(self)
        if file_list_path:
            file_list = []  # 文件名列表
            for dir_path, dir_name, file_names in os.walk(file_list_path):
                for file_path in file_names:  # 遍历所有文件名
                    if file_path.endswith(('.xlsx', '.xls')):  # 仅添加 Excel 文件
                        file_name = os.path.basename(file_path)  # 提取文件名
                        file_list.append(file_name)
            if len(file_list) == 0:
                QMessageBox.warning(self, "提醒", "文件夹内不存在任何表格文件")
                return

            self.input_path = file_list_path
            self.encryption_pages.setCurrentWidget(self.encryption_para_page)

            # 添加列表数据
            self.model.setStringList(file_list)
            self.encryption_import_list_view.setModel(self.model)

    def choose_output_path(self):
        output_path = QFileDialog.getExistingDirectory(self)
        if output_path:
            self.output_path = output_path
            self.encryption_output_path_button.setText("已选择文件夹")
            self.encryption_output_path_label.setText(self.output_path)

    def on_password_entry_changed(self, text):
        if text:
            self.password = text
        else:
            self.password = None

    def run_worker(self):
        if not all([self.input_path, self.password, self.output_path]):
            QMessageBox.critical(self, "处理异常", "请填写完整参数！")
            return

        # 设置任务并启动线程
        self.worker_thread.set_task(func=self.do_task)
        self.worker_thread.start()
        self.encryption_process_button.setEnabled(False)

    def do_task(self, *args, **kwargs):
        result = ExcelEncryption(
            self.input_path, self.output_path, self.password).encryption_excels()
        return result

    def on_current_widget_changed(self):
        if self.encryption_pages.currentWidget() is self.encryption_para_page:
            self.output_path = None
            self.encryption_output_path_button.setText("选择输出文件夹")
            self.encryption_output_path_label.setText("")
            self.encryption_input_entry.setText("")
            self.model.setStringList([])
            self.encryption_import_list_view.setModel(self.model)

        else:
            self.file_path = None

    def closeEvent(self, event):
        # 窗口关闭时结束线程
        if self.worker_thread.isRunning():
            self.worker_thread.quit()
            self.worker_thread.wait()
        event.accept()
