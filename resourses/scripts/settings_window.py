from PySide6.QtWidgets import QApplication, QDialog

from screens.settingswindow_ui import Ui_Dialog

import sys

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Settings")
        self.setFixedSize(300, 120) #i forgot to lock size in designer



app = QApplication(sys.argv)
wi = SettingsWindow()
wi.show()
sys.exit(app.exec())