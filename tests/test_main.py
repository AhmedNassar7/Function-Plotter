import pytest
from PySide6.QtWidgets import QApplication
from main import MainWindow
from pytestqt.qtbot import QtBot

@pytest.fixture
def app(qtbot: QtBot):
    app = QApplication([])
    main_window = MainWindow()
    qtbot.addWidget(main_window)
    return main_window

def test_plot_button(app, qtbot: QtBot):
    app.ui.functionInput.setText("5*x^3 + 2*x")
    app.ui.minInput.setText("0")
    app.ui.maxInput.setText("10")
    qtbot.mouseClick(app.ui.plotButton, Qt.LeftButton)
    assert app.ui.errorLabel.text() == ""
