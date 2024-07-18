import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ui_main import Ui_MainWindow
from plotter import validate_function, plot_function

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.plotButton.clicked.connect(self.plot)
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.ui.plotLayout.addWidget(self.canvas)

    def plot(self):
        func_str = self.ui.functionInput.text()
        try:
            x_min = float(self.ui.minInput.text())
            x_max = float(self.ui.maxInput.text())
        except ValueError:
            self.ui.errorLabel.setText("Min and Max values must be numeric.")
            return

        if not validate_function(func_str):
            self.ui.errorLabel.setText("Invalid function format.")
            return

        self.ui.errorLabel.setText("")
        self.canvas.axes.clear()
        plot_function(func_str, x_min, x_max, self.canvas.axes)
        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
