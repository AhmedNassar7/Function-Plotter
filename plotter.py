import re
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QMessageBox

def validate_function(func_str):
    # Validate function string using regular expressions
    pattern = r'^[0-9x\+\-\*/\^\(\)log10sqrt\s\.]+$'
    if not re.match(pattern, func_str):
        return False
    return True

def evaluate_function(func_str, x):
    # Evaluate the function safely
    func_str = func_str.replace('^', '**')
    func_str = func_str.replace('log10', 'np.log10')
    func_str = func_str.replace('sqrt', 'np.sqrt')
    try:
        y = eval(func_str)
    except Exception as e:
        raise ValueError(f"Error evaluating function: {e}")
    return y

def plot_function(func_str, x_min, x_max, axes):
    x = np.linspace(x_min, x_max, 400)
    y = evaluate_function(func_str, x)
    axes.plot(x, y)
    axes.set_xlabel('x')
    axes.set_ylabel('f(x)')
    axes.set_title(f'Plot of {func_str}')
    axes.grid(True)
