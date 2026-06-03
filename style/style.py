import os


def get_style(dockwidget):
    abs_path = os.path.dirname(os.path.abspath(__file__))

    assets_path = os.path.join(os.path.dirname(abs_path), "assets").replace("\\", "/")

    file_path = os.path.join(abs_path, "style.qss")

    with open(file_path) as qss_file_content:
        qss = qss_file_content.read()

    qss = qss.replace("ASSETS_PATH", assets_path)
    dockwidget.setStyleSheet(qss)
