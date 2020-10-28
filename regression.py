"""

file: regression.py
author: Shantanav Saurav << ss9415@g.rit.edu >>
purpose: perform linear regression analysis on a random set of data

"""
import random, sys, quick_sort, matplotlib.pyplot as plt


def regression(x, y):
    """
    Display regression analysis of x,y ordered pairs
    :param x: X values
    :param y: Y values
    """
    Xm, Ym = sum(x) / len(x), sum(y) / len(y)
    m = sum([((x[i] - Xm) * (y[i] - Ym)) for i in range(0, len(x))]) / sum([(i - Xm) ** 2 for i in x])
    b = Ym - m * Xm
    regression_line = [(m * xval) + b for xval in x]
    print("Equation: " + str(m) + "x + " + str(b))
    
    predict_x = [i + len(x) - 1 for i in range(0, len(x) // 2)]
    predict_y = [(m * predict_x[i]) + b for i in range(0, len(predict_x))]
    plt.scatter(x, y, s = 3, color="#000000", label="Original Data Set")
    plt.plot(x, regression_line, label="Best Fit Line")
    plt.plot(predict_x, predict_y, label="Prediction based on best fit")
    plt.legend()
    plt.show()


def main(size: int) -> None:
    """
    Perform linear regression analysis in Python
    :return: None
    """
    y = quick_sort.quick_sort([random.randint(10000, 1000000) for i in range(0, int(size))]) 
    x = [i for i in range(0, len(y))]
    regression(x, y)


if __name__ == "__main__":
    main(sys.argv[1])
