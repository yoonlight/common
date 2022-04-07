import matplotlib.pyplot as plt
import datetime
from .utils import checkdir


def plot(x_len, y_loss, y_val_loss, y_test_loss):
    date = datetime.datetime.now()
    unix_time = datetime.datetime.timestamp(date)*1000
    checkdir()
    plt.plot(x_len, y_val_loss, marker='.',
             c='red', label="Validation-set Loss")
    plt.plot(x_len, y_loss, marker='.', c='blue', label="Train-set Loss")
    plt.plot(x_len, y_test_loss, marker='.', c='green', label="Test-set Loss")

    plt.legend(loc='upper right')
    plt.grid()
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.savefig(fname=f"image/result-{unix_time}.png")
    plt.show()
