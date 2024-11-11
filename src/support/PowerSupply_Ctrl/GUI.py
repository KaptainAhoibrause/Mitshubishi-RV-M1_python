import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout
# from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window title
        self.setWindowTitle('PowerSupplyUI')

        # channel label
        chnl1Label = QLabel()
        chnl1Label.setText("CH 1")

        chnl2Label = QLabel()
        chnl2Label.setText("CH 2")

        chnl3Label = QLabel()
        chnl3Label.setText("CH 3")

        chnl4Label = QLabel()
        chnl4Label.setText("CH 4")

        # channel buttons
        chnl1Button = QPushButton()
        chnl1Button.setCheckable(True)
        chnl1Button.setText("on/off")

        chnl2Button = QPushButton()
        chnl2Button.setCheckable(True)
        chnl2Button.setText("on/off")

        chnl3Button = QPushButton()
        chnl3Button.setCheckable(True)
        chnl3Button.setText("on/off")

        chnl4Button = QPushButton()
        chnl4Button.setCheckable(True)
        chnl4Button.setText("on/off")

        # place widgets
        layout = QGridLayout()
        layout.addWidget(chnl1Label, 0, 0)
        layout.addWidget(chnl2Label, 0, 1)
        layout.addWidget(chnl3Label, 0, 2)
        layout.addWidget(chnl4Label, 0, 3)

        layout.addWidget(chnl1Button, 1, 0)
        layout.addWidget(chnl2Button, 1, 1)
        layout.addWidget(chnl3Button, 1, 2)
        layout.addWidget(chnl4Button, 1, 3)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())
