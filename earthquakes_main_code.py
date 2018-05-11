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
        self.side2_label = QLabel("Intensity (0-10)")
        self.grid.addWidget(self.side2_label, 3, 1, 1, 1)
        self.side2_value = QSlider(Qt.Horizontal)
        self.side2_value.setMinimum(0)
        self.side2_value.setMaximum(10)
        self.side2_value.setValue(0)
        self.side2_value.setTickPosition(QSlider.TicksBelow)
        self.side2_value.setTickInterval(5)
        self.grid.addWidget(self.side2_value, 3, 2, 1, 1)
        self.separation_value = QLineEdit()
        self.grid.addWidget(self.separation_value, 4, 2, 1, 1)
        self.separation_label = QLabel("Separation (m): ")
        self.grid.addWidget(self.separation_label, 4, 1, 1, 1)
        self.calc_button = QPushButton("Calculate")
        self.grid.addWidget(self.calc_button, 5, 1, 1, 2)

        '''
        Stylistic modifications:
        - White background
        '''

        # Signals and slots
        self.calc_button.clicked.connect(self.calc_force)

        self.show()

    def calc_force(self):

        try:
            mass1 = float(self.time_value.text())
            mass2 = float(self.side2_value.text())
            r = float(self.separation_value.text())
            force = G*mass1*mass2/r/r
            self.answer_value.setText(str('{:.4e}'.format(force)) + " Newtons")
        except ZeroDivisionError:
            self.answer_value.setText("Separation of 0 not allowed")
        except ValueError:
            self.answer_value.setText("Enter numbers")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = App()
    sys.exit(app.exec())

# TODO - Make a slider with magnitude.
# TODO - Scrape past 30 days on start.