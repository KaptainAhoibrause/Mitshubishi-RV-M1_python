import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout
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


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window title
        self.setWindowTitle('PowerSupplyUI')

        # button toggled function
        def toggled(checked):
            print(checked)

        # channel label
        chnl1Label = Widgets.Label("chnl1Label", "CH 1")
        chnl2Label = Widgets.Label("chnl2Label", "CH 2")
        chnl3Label = Widgets.Label("chnl3Label", "CH 3")
        chnl4Label = Widgets.Label("chnl4Label", "CH 4")
        outputLabel = Widgets.Label("outputLabel", "OUT")

        # channel buttons
        chnl1Button = Widgets.ToggleButton("chnl1Button", "on/off")
        chnl2Button = Widgets.ToggleButton("chnl2Button", "on/off")
        chnl3Button = Widgets.ToggleButton("chnl3Button", "on/off")
        chnl4Button = Widgets.ToggleButton("chnl4Button", "on/off")
        outputButton = Widgets.ToggleButton("outputButton", "on/off")

        # place widgets
        layout = QGridLayout()
        layout.addWidget(chnl1Label, 0, 0)
        layout.addWidget(chnl2Label, 0, 1)
        layout.addWidget(chnl3Label, 0, 2)
        layout.addWidget(chnl4Label, 0, 3)
        layout.addWidget(outputLabel, 0, 4)

        layout.addWidget(chnl1Button, 1, 0)
        layout.addWidget(chnl2Button, 1, 1)
        layout.addWidget(chnl3Button, 1, 2)
        layout.addWidget(chnl4Button, 1, 3)
        layout.addWidget(outputButton, 1, 4)
        self.setLayout(layout)

        # show the window
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())
