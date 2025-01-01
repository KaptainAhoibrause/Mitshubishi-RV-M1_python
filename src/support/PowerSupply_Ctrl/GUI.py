import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout, QStatusBar, QWidget, QMainWindow
from PyQt6.QtGui import QIcon
# from PyQt6.QtCore import Qt


class Widgets:
    class ToggleButton(QPushButton):
        def __init__(self, name, label):
            super().__init__(label)
            self.name = name
            self.setCheckable(True)  # Make the button toggleable
            self.clicked.connect(self.toggled)

        def toggled(self):
            # Display the current state (checked or unchecked)
            print(f"Toggled {self.name} to {self.isChecked()}")

    class Label(QLabel):
        def __init__(self, name, content):
            super().__init__()
            self.setText(content)


class WindowObjects:
    class StatusBar(QStatusBar):
        def __init__(self, name):
            super().__init__()
            self.id = name
            self.showMessage("GUI Ready")


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window title
        self.setWindowTitle('PowerSupplyUI')
        self.setWindowIcon(QIcon('./gui_assets/lightning-34774_640.png'))

        self.setGeometry(100, 100, 300, 200)

        # button toggled function
        def toggled(checked):
            print(checked)

        # channel label
        chnl1Label = Widgets.Label("chnl1Label", "CH 1")
        chnl2Label = Widgets.Label("chnl2Label", "CH 2")
        chnl3Label = Widgets.Label("chnl3Label", "CH 3")
        chnl4Label = Widgets.Label("chnl4Label", "CH 4")

        # channel voltage and amp
        chnl1Volt = Widgets.Label("chnl1Volt", "n.a.")
        chnl2Volt = Widgets.Label("chnl2Volt", "n.a.")
        chnl3Volt = Widgets.Label("chnl3Volt", "n.a.")
        chnl4Volt = Widgets.Label("chnl4Volt", "n.a.")

        chnl1Amp = Widgets.Label("chnl1Amp", "n.a.")
        chnl2Amp = Widgets.Label("chnl2Amp", "n.a.")
        chnl3Amp = Widgets.Label("chnl3Amp", "n.a.")
        chnl4Amp = Widgets.Label("chnl4Amp", "n.a.")

        # channel buttons
        chnl1Button = Widgets.ToggleButton("chnl1Button", "on/off")
        chnl2Button = Widgets.ToggleButton("chnl2Button", "on/off")
        chnl3Button = Widgets.ToggleButton("chnl3Button", "on/off")
        chnl4Button = Widgets.ToggleButton("chnl4Button", "on/off")
        outputButton = Widgets.ToggleButton("outputButton", "OUT")

        statusBar1 = WindowObjects.StatusBar(1)
        self.setStatusBar(statusBar1)

        # place widgets
        layout = QGridLayout()
        layout.addWidget(chnl1Label, 0, 0)
        layout.addWidget(chnl2Label, 1, 0)
        layout.addWidget(chnl3Label, 2, 0)
        layout.addWidget(chnl4Label, 3, 0)

        layout.addWidget(chnl1Volt, 0, 1)
        layout.addWidget(chnl2Volt, 1, 1)
        layout.addWidget(chnl3Volt, 2, 1)
        layout.addWidget(chnl4Volt, 3, 1)

        layout.addWidget(chnl1Amp, 0, 2)
        layout.addWidget(chnl2Amp, 1, 2)
        layout.addWidget(chnl3Amp, 2, 2)
        layout.addWidget(chnl4Amp, 3, 2)

        layout.addWidget(chnl1Button, 0, 3)
        layout.addWidget(chnl2Button, 1, 3)
        layout.addWidget(chnl3Button, 2, 3)
        layout.addWidget(chnl4Button, 3, 3)

        layout.addWidget(outputButton, 4, 0, 1, 4)

        # Create a central widget to hold the layout
        centralWidget = QWidget()
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('src/support/PowerSupply_Ctrl/gui_assets/style.qss').read_text())

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())
