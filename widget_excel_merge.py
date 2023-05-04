# -*- coding: utf-8 -*-

import os
from PySide6.QtWidgets import QMessageBox, QWidget, QFileDialog
from PySide6.QtCore import QStringListModel
from merge_ui import Ui_merge
from worker_thread import WorkerThread
from excel_merger import ExcelMerger
from widget_wait import WidgetWait
from validators import ColumnValidator, RowValidator
from openpyxl.utils.cell import column_index_from_string


class WidgetExcelMerge(QWidget, Ui_merge):
    def __init__(self, parent=None):
        super(WidgetExcelMerge, self).__init__(parent)

        self.setupUi(self)

        self.model = QStringListModel()

        self.worker_thread = WorkerThread()
        self.worker_thread.finished_signal().finished.connect(self.task_finished)
        self.worker_thread.started.connect(self.start_wait)

        self.merge_open_dir_button.clicked.connect(self.get_file_list)
        self.merge_output_path_button.clicked.connect(self.choose_output_path)
        self.merge_column_entry.setValidator(ColumnValidator())
        self.merge_column_entry.textChanged.connect(
            self.on_merge_column_entry_changed)
        self.merge_row_heads_entry.setValidator(RowValidator(max_value=99))
        self.merge_row_heads_entry.textChanged.connect(
            self.on_row_heads_entry_changed)
        self.merge_process_button.clicked.connect(self.run_worker)
        self.merge_pages.currentChanged.connect(self.on_current_widget_changed)
        self.merge_pages.setCurrentWidget(self.merge_open_dir_page)

    def task_finished(self, success, result):
        # 处理任务完成信号，显示结果或者错误信息
        self.merge_process_button.setEnabled(True)
        self.wait.hide()
        if success:
            QMessageBox.information(self, "成功", "处理完成，请核验结果!")
        else:
            QMessageBox.critical(self, "错误", str(result))

        self.merge_pages.setCurrentWidget(self.merge_open_dir_page)
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
            self.merge_pages.setCurrentWidget(self.merge_para_page)

            # 添加列表数据
            self.model.setStringList(file_list)
            self.merge_import_list_view.setModel(self.model)

    def choose_output_path(self):
        output_path, _ = QFileDialog.getSaveFileName(self, "保存文件", "", "Excel Files (*.xlsx)")
        if output_path:
            # check if the file extension is '.xlsx'
            _, ext = os.path.splitext(output_path)
            if ext != '.xlsx':
                # add the '.xlsx' extension if it's missing
                output_path += '.xlsx'
            self.output_path = output_path
            self.merge_output_path_button.setText("保存文件到以下路径")
            self.merge_output_path_label.setText(self.output_path)

    def on_merge_column_entry_changed(self, text):
        try:
            self.merge_col = int(text)
        except ValueError:
            try:
                self.merge_col = column_index_from_string(text)
            except ValueError:
                self.merge_col = None

    def on_row_heads_entry_changed(self, text):
        if text:
            self.head_rows = int(text)
        else:
            self.head_rows = None

    def run_worker(self):
        if not all([self.input_path, self.head_rows, self.merge_col, self.output_path]):
            QMessageBox.critical(self, "处理异常", "请填写完整参数！")
            return

        # 设置任务并启动线程
        self.worker_thread.set_task(func=self.do_task)
        self.worker_thread.start()
        self.merge_process_button.setEnabled(False)

    def do_task(self, *args, **kwargs):
        result = ExcelMerger(self.input_path, self.head_rows, self.merge_col,
                                self.output_path).merge_excels()
        return result

    def on_current_widget_changed(self):
        if self.merge_pages.currentWidget() is self.merge_para_page:
            self.output_path = None
            self.merge_output_path_button.setText("请选择输出文件")
            self.merge_output_path_label.setText("")
            self.merge_row_heads_entry.setText("1")
            self.merge_column_entry.setText("A")
            self.model.setStringList([])
            self.merge_import_list_view.setModel(self.model)

        else:
            self.file_path = None

    def closeEvent(self, event):
        # 窗口关闭时结束线程
        if self.worker_thread.isRunning():
            self.worker_thread.quit()
            self.worker_thread.wait()
        event.accept()
