import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QLabel
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
        self.ui.errorLabel = QLabel("")
        self.ui.plotLayout.addWidget(self.ui.errorLabel)

    def plot(self):
        func_str = self.ui.functionInput.text().strip()
        min_str = self.ui.minInput.text().strip()
        max_str = self.ui.maxInput.text().strip()

        # Validate function input
        if not func_str:
            self.ui.errorLabel.setText("Function input cannot be empty.")
            return

        # Validate numerical inputs
        try:
            x_min = float(min_str)
            x_max = float(max_str)
        except ValueError:
            self.ui.errorLabel.setText("Min and Max values must be numeric.")
            return

        if x_min >= x_max:
            self.ui.errorLabel.setText("Min value must be less than Max value.")
            return

        # Validate function format
        if not validate_function(func_str):
            self.ui.errorLabel.setText("Invalid function format.")
            return

        # Clear error message and plot
        self.ui.errorLabel.setText("")
        self.canvas.axes.clear()
        try:
            plot_function(func_str, x_min, x_max, self.canvas.axes)
            self.canvas.draw()
        except Exception as e:
            self.ui.errorLabel.setText(f"Error plotting function: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
