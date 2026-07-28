from PySide6.QtWidgets import QApplication, QDialog, QDialogButtonBox
from PySide6.QtCore import Qt

# from screens.settingswindow_ui import Ui_Dialog
from scripts.screens.settingswindow_ui import Ui_Dialog

# from _getdata import GetTrash
from scripts._getdata import GetTrash

import configparser

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Settings")
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)

        self.config = configparser.ConfigParser()
        self.config.read('assets/configdontouch.ini')

        self.ui.lineEditPath.setText(self.config.get('settings', 'path'))
        self.ui.lineEditLimit.setText(self.config.get('settings', 'limit'))

        self.ui.buttonBox.accepted.connect(self.applySettings)
        self.ui.buttonBox.clicked.connect(self.showDeafults)

    
    def applySettings(self):

        self.config.set('settings', 'path', self.ui.lineEditPath.text())
        self.config.set('settings', 'limit', self.ui.lineEditLimit.text())

        with open('assets/configdontouch.ini', 'w') as configfile:
            self.config.write(configfile)
                

    def showDeafults(self, button): 
        if self.ui.buttonBox.standardButton(button) == QDialogButtonBox.StandardButton.RestoreDefaults:
            self.ui.lineEditPath.setText(GetTrash.deafult_path())
            self.ui.lineEditLimit.setText(str(GetTrash.deafult_limit()))