from PySide6.QtWidgets import QApplication, QMessageBox

import sys

class Error(QMessageBox):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.setWindowTitle("Hmm")
        self.setText("if you see this message that means something wrong")
        self.setInformativeText("you dont suppost to see this message i didnt code it yet")
        
        self.setIcon(QMessageBox.Icon.Warning)

        self.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.addButton("popopepeaaaaaaaaaaa", QMessageBox.YesRole)
        


app = QApplication(sys.argv)
wi = Error()
sys.exit(wi.exec())