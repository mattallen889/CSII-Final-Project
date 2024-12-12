import sys
from PyQt6.QtWidgets import QApplication, QDialog
from PGui import Ui_Dialog
from ProjectLogic import Logic

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    logic = Logic(ui)
    Dialog.show()
    sys.exit(app.exec())
