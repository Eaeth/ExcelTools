pyside6-uic.exe main.ui -o main_ui.py
pyside6-uic.exe wait.ui -o wait_ui.py
pyside6-uic.exe merge.ui -o merge_ui.py
pyside6-uic.exe split.ui -o split_ui.py
pyside6-rcc.exe images.qrc -o images_rc.py