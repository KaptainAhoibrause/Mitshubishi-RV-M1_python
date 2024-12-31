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

        # button toggled function
        def toggled(checked):
            print(checked)

        # channel label
        chnl1Label = Widgets.Label("chnl1Label", "CH 1")
        chnl2Label = Widgets.Label("chnl2Label", "CH 2")
        chnl3Label = Widgets.Label("chnl3Label", "CH 3")
        chnl4Label = Widgets.Label("chnl4Label", "CH 4")

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
        layout.addWidget(chnl2Label, 0, 1)
        layout.addWidget(chnl3Label, 0, 2)
        layout.addWidget(chnl4Label, 0, 3)

        layout.addWidget(chnl1Button, 1, 0)
        layout.addWidget(chnl2Button, 1, 1)
        layout.addWidget(chnl3Button, 1, 2)
        layout.addWidget(chnl4Button, 1, 3)
        layout.addWidget(outputButton, 2, 0, 4, 4)

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
