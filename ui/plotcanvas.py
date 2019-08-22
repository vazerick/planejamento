from PyQt5.QtWidgets import QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt



class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=1, height=1, dpi=75):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self, x, y):
        ax = self.fig.add_subplot(111)
        ax.clear()

        ax.set_yticks([25,50,75,100], minor=False)
        ax.yaxis.grid(True, which='major', linewidth=2)
        ax.xaxis.grid(True, linestyle="--", linewidth=0.5)
        ax.bar(x, y)
        print("\n\n\tDEBUG")
        for tick in ax.get_xticklabels():
            tick.set_rotation(45)
        self.draw()
        print(len(x), len(y))