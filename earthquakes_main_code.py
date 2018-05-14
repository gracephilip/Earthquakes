import sys
import math
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

G = 6.67408e-11

class App(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the app layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(100, 100, 400, 200)

        # Make widgets
        self.title = QLabel("Worldwide Earthquakes")
        self.grid.addWidget(self.title, 1, 1, 1 ,1)
        self.time_label = QLabel("Interval: ")
        self.grid.addWidget(self.time_label, 2, 1, 1, 1)
        self.time_value = QComboBox()
        dropdownItems = ['Past 30 Days', 'Past 7 Days', 'Past Day', 'Past Hour']
        for i in dropdownItems:
            self.time_value.addItem(i)
        self.grid.addWidget(self.time_value, 2, 2, 1, 1)
        self.intensity_label = QLabel("Intensity (0-10)")
        self.grid.addWidget(self.intensity_label, 3, 1, 1, 1)
        self.intensity_value = QSlider(Qt.Horizontal)
        self.intensity_value.setMinimum(0)
        self.intensity_value.setMaximum(10)
        self.intensity_value.setValue(0)
        self.intensity_value.setTickPosition(QSlider.TicksBelow)
        self.intensity_value.setTickInterval(1)
        self.grid.addWidget(self.intensity_value, 3, 2, 1, 1)
        self.calc_button = QPushButton("Calculate")
        self.grid.addWidget(self.calc_button, 5, 1, 1, 2)
        self.boundary_label = QLabel("Show Boundaries")
        self.grid.addWidget(self.boundary_label, 4, 1, 1, 1)
        self.boundary_value = QCheckBox()
        self.grid.addWidget(self.boundary_value, 4, 2, 1, 2)

        '''
        Stylistic modifications:
        - White background
        '''

        # Signals and slots
        self.calc_button.clicked.connect(self.get_earthquake)

        self.show()

    def get_earthquake(self):
        print("earthquake")
        intensity = self.intensity_value.sliderPosition()
        interval = self.time_value.currentText()
        if self.time_value.currentText() == 'Past 30 Days':
            interval = 30
        elif self.time_value.currentText() == 'Past 7 Days':
            interval = 7
        elif self.time_value.currentText() == 'Past Day':
            interval = 1
        elif self.time_value.currentText() == 'Past Hour':
            interval = 1/24
        will_show_boundaries = bool(int(int(self.boundary_value.checkState())/2))
        print(intensity, interval, will_show_boundaries)
        # show boundary
        # try
        # self.answer_value.setText("Enter numbers")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = App()
    sys.exit(app.exec())

# TODO - Make a slider with magnitude.
# TODO - Scrape past 30 days on start.