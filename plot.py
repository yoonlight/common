import matplotlib.pyplot as plt


def plot(x_len, y_loss, y_val_loss, y_test_loss):
    plt.plot(x_len, y_val_loss, marker='.',
             c='red', label="Validation-set Loss")
    plt.plot(x_len, y_loss, marker='.', c='blue', label="Train-set Loss")
    plt.plot(x_len, y_test_loss, marker='.', c='green', label="Test-set Loss")

    plt.legend(loc='upper right')
    plt.grid()
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.savefig(fname="result")
    plt.show()
