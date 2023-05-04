# -*- coding: utf-8 -*-

from PySide6.QtCore import Signal, QObject, QThread
import traceback


class FinishedSignal(QObject):
    """
    定义一个信号对象，用于工作线程与主线程之间的通信。
    """
    finished = Signal(bool, str)


class WorkerThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._args = None
        self._kwargs = None
        self._finished_signal = FinishedSignal()

    def set_task(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def run(self):
        try:
            # 执行任务
            result = self._kwargs['func'](*self._args)
            if result == None:
                self._finished_signal.finished.emit(True, str(result))
            else:
                self._finished_signal.finished.emit(False, str(result))
        except Exception as e:
            # 报告异常
            tb = traceback.format_exc()
            self._finished_signal.finished.emit(False, str(e) + "\n\n" + tb)

    def finished_signal(self):
        return self._finished_signal
