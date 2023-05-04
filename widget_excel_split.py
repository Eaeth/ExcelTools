# -*- coding: utf-8 -*-

from PySide6.QtWidgets import QMessageBox, QWidget, QFileDialog
from split_ui import Ui_split

from worker_thread import WorkerThread
from excel_splitter import ExcelSplitter
from widget_wait import WidgetWait
from validators import ColumnValidator, RowValidator
from openpyxl.utils.cell import column_index_from_string


class WidgetExcelSplit(QWidget, Ui_split):
    def __init__(self, parent=None):
        super(WidgetExcelSplit, self).__init__(parent)

        self.setupUi(self)
        self.worker_thread = WorkerThread()

        self.split_open_file_button.clicked.connect(self.get_file_name)
        self.split_process_button.clicked.connect(self.run_worker)
        self.worker_thread.finished_signal().finished.connect(self.task_finished)
        self.worker_thread.started.connect(self.start_wait)
        self.split_column_entry.setValidator(ColumnValidator())
        self.split_column_entry.textChanged.connect(
            self.on_split_column_entry_changed)
        self.split_start_row_entry.setValidator(RowValidator(max_value=1000))
        self.split_start_row_entry.textChanged.connect(
            self.on_start_row_entry_changed)
        self.split_end_row_entry.setValidator(RowValidator(max_value=1000))
        self.split_end_row_entry.textChanged.connect(
            self.on_end_row_entry_changed)
        self.split_output_path_button.clicked.connect(self.choose_output_path)
        self.split_pages.currentChanged.connect(self.on_current_widget_changed)
        self.split_pages.setCurrentWidget(self.split_openfile_page)

    def get_file_name(self):
        self.file_path, _ = QFileDialog.getOpenFileName(
            self, "选择文件", "", "Excel files (*.xlsx;*.xls)")
        if self.file_path:
            self.split_pages.setCurrentWidget(self.split_para_page)
            self.split_select_file_path.setText(self.file_path)

    def start_wait(self):
        self.wait = WidgetWait()
        self.wait.exec()

    def run_worker(self):
        if not all([self.file_path, self.start_rows, self.end_rows, self.split_col, self.output_path]):
            QMessageBox.critical(self, "处理异常", "请填写完整参数！")
            return
        if self.start_rows >= self.end_rows:
            QMessageBox.warning(self, "提醒", "起始行号大于或等于起始行号")
            return
        # 设置任务并启动线程
        self.worker_thread.set_task(func=self.do_task)
        self.worker_thread.start()
        self.split_process_button.setEnabled(False)

    def do_task(self, *args, **kwargs):
        result = ExcelSplitter(self.file_path, self.start_rows, self.end_rows,
                               self.split_col, self.output_path).split_excel_by_column()
        return result

    def on_start_row_entry_changed(self, text):
        if text:
            self.start_rows = int(text)
        else:
            self.start_rows = None

    def on_end_row_entry_changed(self, text):
        if text:
            self.end_rows = int(text)
        else:
            self.end_rows = None

    def on_split_column_entry_changed(self, text):
        try:
            self.split_col = int(text)
        except ValueError:
            try:
                self.split_col = column_index_from_string(text)
            except ValueError:
                self.split_col = None

    def choose_output_path(self):
        output_path = QFileDialog.getExistingDirectory(self)
        if output_path:
            self.output_path = output_path
            self.split_output_path_button.setText("已选择文件夹")
            self.split_output_path_label.setText(self.output_path)

    def on_current_widget_changed(self):
        if self.split_pages.currentWidget() is self.split_para_page:
            self.output_path = None
            self.split_output_path_button.setText("选择输出文件夹")
            self.split_output_path_label.setText("")
            self.split_start_row_entry.setText("2")
            self.split_end_row_entry.setText("50")
            self.split_column_entry.setText("A")
        else:
            self.file_path = None

    def task_finished(self, success, result):
        # 处理任务完成信号，显示结果或者错误信息
        self.split_process_button.setEnabled(True)
        self.wait.hide()
        if success:
            QMessageBox.information(self, "成功", "处理完成，请核验结果!")
        else:
            QMessageBox.critical(self, "错误", str(result))

        self.split_pages.setCurrentWidget(self.split_openfile_page)
        self.worker_thread.quit()
        self.worker_thread.wait()

    def closeEvent(self, event):
        # 窗口关闭时结束线程
        if self.worker_thread.isRunning():
            self.worker_thread.quit()
            self.worker_thread.wait()
        event.accept()
