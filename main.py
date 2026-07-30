from PySide6.QtWidgets import QApplication, QWidget, QLabel, QProgressBar, QMenu
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt

from send2trash import send2trash

from scripts._setini import sset_INI
from scripts._cleancan import clean_trash

from scripts.settings_window import SettingsWindow

import sys, configparser, os

class TrashWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAcceptDrops(True)

        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(7, 19, 67, 52)
        self.progressbar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressbar.setOrientation(Qt.Vertical)

        self.pixmap1 = QPixmap("assets/images/Trash(1).png")
        self.pixmap2 = QPixmap("assets/images/Trash(2).png")
        self.pixmap1.scaled(0, 0, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.pixmap2.scaled(0, 0, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setPixmap(self.pixmap1.scaled(80, 90))

        self.p0sition = None

        self.UIUpdate()


        # TODO: detect buttons: delete, cntr+z
        # TODO: deactivate/activate image on update
        # TODO: add "open trash folder"


    #update
    def UIUpdate(self):

        print("UIUpdate(self)")

        sset_INI()

        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)

        config = configparser.ConfigParser()
        config.read('assets/configdontouch.ini')

        self.progressbar.setMaximum(int(config.get('settings', 'limit')))

        if int(config.get('trash', 'trash')) >= int(config.get('settings', 'limit')):
            self.progressbar.setValue(int(config.get('settings', 'limit')))

        else:
            self.progressbar.setValue(int(config.get('trash', 'trash')))


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

        mimedata = event.mimeData()

        for url in mimedata.urls():
            send2trash(os.path.abspath(url.toLocalFile()))

        self.label.setPixmap(self.pixmap1.scaled(80, 90))
        self.UIUpdate()



    #menu
    def contextMenuEvent(self, event):
        menu = QMenu()

        # TODO: add "open trash folder"

        self.act_update = menu.addAction(QIcon("assets/images/ico-update.png"), "Update")
        self.act_cleantrash = menu.addAction(QIcon("assets/images/ico-clean.png"), "Clean")
        self.act_settings = menu.addAction(QIcon("assets/images/ico-settings.png"), "Settings")
        self.act_exit = menu.addAction(QIcon("assets/images/ico-exit.png"), "Exit")

        act = menu.exec(event.globalPos())

        match act:
            case self.act_update:
                self.UIUpdate()

            case self.act_cleantrash:
                clean_trash()
                self.UIUpdate()

            case self.act_settings:
                self.openSettings()

            case self.act_exit:
                sys.exit()


    #settings
    def openSettings(self):
        sett = SettingsWindow(self)
        sett.exec()
        self.UIUpdate()
 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wi = TrashWidget()
    wi.resize(170, 200)
    wi.show()
    sys.exit(app.exec())