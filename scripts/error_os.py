from PySide6.QtWidgets import QApplication, QMessageBox

import sys

class Error(QMessageBox):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Unsupported Operating System!")
        self.setText("Program dont have build in path for this operating system.")
        self.setInformativeText("Please import path to Trash Can the settings.")
        
        self.setIcon(QMessageBox.Icon.Warning)

        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.addButton("Open Settings", QMessageBox.YesRole)
        


app = QApplication(sys.argv)
wi = Error()
sys.exit(wi.exec())