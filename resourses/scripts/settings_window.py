from PySide6.QtWidgets import QApplication, QDialog, QDialogButtonBox
from PySide6.QtCore import Qt

from screens.settingswindow_ui import Ui_Dialog

from _getdata import GetTrash

import sys, json

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Settings")
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)

        with open('resourses/data.json', 'r') as file:
            self.data = json.load(file)

        self.ui.lineEditPath.setText(self.data['settings']['path'])
        self.ui.lineEditLimit.setText(str(self.data['settings']['limit']))

        self.ui.buttonBox.accepted.connect(self.applySettings)
        self.ui.buttonBox.clicked.connect(self.showDeafults)

    
    def applySettings(self):
        self.data['settings']['path'] = str(self.ui.lineEditPath.text())
        self.data['settings']['limit'] = int(self.ui.lineEditLimit.text())

        with open('resourses/data.json', "w") as file:
            json.dump(self.data, file, indent=4)


    def showDeafults(self, button): 
        if self.ui.buttonBox.standardButton(button) == QDialogButtonBox.StandardButton.RestoreDefaults:
            self.ui.lineEditPath.setText(GetTrash.deafult_path())
            self.ui.lineEditLimit.setText(str(GetTrash.deafult_limit()))

    

app = QApplication(sys.argv)
wi = SettingsWindow()
wi.show()
sys.exit(app.exec())