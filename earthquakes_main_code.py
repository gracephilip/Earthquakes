import sys
import math
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from web_scrape import get_data
from eq_gmplot import plotting_function
from eq_gmplot import plates
import qdarkstyle


class App(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the app layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(100, 100, 400, 200)

        # Make widgets
        self.title = QLabel("Worldwide Earthquakes")
        with open('main.css', 'r') as f:
            self.title.setStyleSheet(f.read())
        self.grid.addWidget(self.title, 1, 1, 1 ,1)
        # Time interval
        self.time_label = QLabel("Interval: ")
        self.grid.addWidget(self.time_label, 2, 1, 1, 1)
        self.time_value = QComboBox()
        dropdownItems = ['Past 30 Days', 'Past 7 Days', 'Past Day', 'Past Hour']
        for i in dropdownItems:
            self.time_value.addItem(i)
        self.grid.addWidget(self.time_value, 2, 2, 1, 1)
        # Intensity
        self.intensity_label = QLabel("Minimum Intensity (0):")
        self.grid.addWidget(self.intensity_label, 3, 1, 1, 1)
        self.intensity_value = QSlider(Qt.Horizontal)
        self.intensity_value.setMinimum(0)
        self.intensity_value.setMaximum(10)
        self.intensity_value.setValue(0)
        self.intensity_value.setTickPosition(QSlider.TicksBelow)
        self.intensity_value.setTickInterval(1)
        self.grid.addWidget(self.intensity_value, 3, 2, 1, 1)
        # Search button
        self.search_button = QPushButton("Search")
        self.grid.addWidget(self.search_button, 5, 1, 1, 2)
        # Boundaries
        self.boundary_label = QLabel("Show Boundaries:")
        self.will_show_boundaries = True
        self.grid.addWidget(self.boundary_label, 4, 1, 1, 1)
        self.boundary_value = QCheckBox()
        self.boundary_value.setChecked(True)
        self.grid.addWidget(self.boundary_value, 4, 2, 1, 2)

        '''
        Stylistic modifications:
        - (None so far...)
        '''
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        # Signals and slots
        self.search_button.clicked.connect(self.get_earthquake)
        self.intensity_value.sliderMoved.connect(lambda: self.intensity_label.setText('Minimum Intensity (' + str(self.intensity_value.sliderPosition()) + '):'))
        self.intensity_value.sliderPressed.connect(lambda: self.intensity_label.setText('Minimum Intensity (' + str(self.intensity_value.sliderPosition()) + '):'))

        self.show()

    def get_earthquake(self):
        self.search_button.setText("Loading...")
        QtWidgets.qApp.processEvents()
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
        self.will_show_boundaries = bool(int(int(self.boundary_value.checkState())/2))

        longitudes, latitudes, magnitudes = get_data(intensity, interval)

        plotting_function(latitudes, longitudes, magnitudes)
        self.search_button.setText("Search")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = App()
    sys.exit(app.exec())

# TODO - Plot boundaries.
# TODO - Improve the style and interface geometry.
# TODO - Add a QWebView.