import sys
import yfinance as yf
import datetime
from datetime import date, timedelta
import torch
import seaborn as sns
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# Get historical data for BTC-USD pair
def get_historical_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date, progress=False)
    return data

def visualize_data(data):
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='Date', y='Close', data=data, ax=ax)
    ax.set_title("Bitcoin Price Analysis")
    plt.show()

# GUI class for displaying the plot
class PlotWindow(QtWidgets.QMainWindow):
    def __init__(self, data):
        super().__init__()

        self.central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        self.canvas = MplCanvas(self.central_widget, width=5, height=4, dpi=100)
        self.layout.addWidget(self.canvas)

        self.plot_data(data)

    def plot_data(self, data):
        self.canvas.axes.plot(data['Date'], data['Close'])
        self.canvas.axes.set_title('Bitcoin Price Analysis')
        self.canvas.draw()



class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)



if __name__ == "__main__":
    
    today = date.today()
    end_date = today.strftime("%Y-%m-%d")
    start_date = (today - timedelta(days=365)).strftime("%Y-%m-%d")

  
    data = get_historical_data('BTC-USD', start_date, end_date)

   
    visualize_data(data)

    
    app = QtWidgets.QApplication(sys.argv)
    window = PlotWindow(data)
    window.show()
    sys.exit(app.exec_())
