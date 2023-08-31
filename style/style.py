import os


def get_style(dockwidget):
    abs_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(abs_path, 'style.qss')
    with  open(file_path) as qss_file_content:
        dockwidget.setStyleSheet(qss_file_content.read())
        