from PySide6.QtWidgets import QApplication, QWidget, QLabel, QProgressBar, QMenu
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt

from send2trash import send2trash

from resourses.scripts._setjson import set_json


import sys, json, os, subprocess

class TrashWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAcceptDrops(True)

        self.p0sition = None

        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(7, 19, 67, 52)
        self.progressbar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressbar.setOrientation(Qt.Vertical)

        self.pixmap1 = QPixmap("resourses/images/Trash(1).png")
        self.pixmap1.scaled(0, 0, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.pixmap2 = QPixmap("resourses/images/Trash(2).png")
        self.pixmap2.scaled(0, 0, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setPixmap(self.pixmap1.scaled(80, 90))

        self.set_update()
        


    #apply
    def set_update(self):

        print("set_update")

        set_json()

        with open('resourses/data.json', 'r') as file:

            data = json.load(file)

            self.progressbar.setMaximum(data['settings']['limit'])
            self.progressbar.setValue(data['size'])

            if data['size'] >= data['settings']['limit']:
                self.progressbar.setValue(data['settings']['limit'])



    #move
    def mousePressEvent(self, event):

        if event.button() == Qt.MouseButton.LeftButton:
            self.p0sition = event.globalPosition().toPoint() - self.pos()

    def mouseMoveEvent(self, event):
            
        if self.p0sition is not None:
            self.move(event.globalPosition().toPoint() - self.p0sition)

    def mouseReleaseEvent(self, event):
        
        self.p0sition = None



    
    #upload file
    def dragEnterEvent(self, event):

        self.label.setPixmap(self.pixmap2.scaled(80, 90))
        
        event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        
        self.label.setPixmap(self.pixmap1.scaled(80, 90))

    def dropEvent(self, event):

        mime_data = event.mimeData()

        for url in mime_data.urls():
            send2trash(os.path.abspath(url.toLocalFile()))

        self.label.setPixmap(self.pixmap1.scaled(80, 90))
        self.set_update()



    #menu
    def contextMenuEvent(self, event):
        menu = QMenu()

        self.act_update = menu.addAction(QIcon("resourses/images/ico-update.png"), "Update")
        self.act_settings = menu.addAction(QIcon("resourses/images/ico-settings.png"), "Settings")
        self.act_exit = menu.addAction(QIcon("resourses/images/ico-exit.png"), "Exit")

        act = menu.exec(event.globalPos())

        match act:
            case self.act_update:
                self.set_update()
            case self.act_settings:
                subprocess.Popen([sys.executable, 'resourses/scripts/settings_window.py'])
            case self.act_exit:
                sys.exit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    wi = TrashWidget()
    wi.resize(170, 200)
    wi.show()
    sys.exit(app.exec())