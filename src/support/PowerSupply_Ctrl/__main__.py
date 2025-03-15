import sys
from GUI import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(
        Path('src/support/PowerSupply_Ctrl/gui_assets/style.qss').read_text())

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())