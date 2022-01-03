#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
My simple linear regression

@author: deronsart
"""

import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt



def simple_linear_regression(x, y):
    """
        Function which calculates the coefficients b0 and b1 for the simple linear regression model
        The linear regression formula is : y = b0 + b1 * x
        with b1 = sum((x[i] - mean(x)) * (y[i] - mean(y))) / sum((x[i] - mean(x))^2)
        and b0 = mean(y) - B1 * mean(x)
            Params : the arrays x and y
            Return : the coefficients b0 and b1
    """
    x_mean = x.mean()
    y_mean = y.mean()
    
    b1 = ((x - x_mean)*(y - y_mean)).sum() / ((x - x_mean)**2).sum()
    
    b0 = y_mean - b1 * x_mean
    
    return b0, b1


def predict_slr(b0, b1, x):
    """ 
        Function which predict the result for a value x according to a simple linear regression model
            Params : the coefficients b0 and b1, and the new value x
            Return : the prediction
    """
    return b0 + b1 * x



if __name__ == '__main__':
    # Data preprocessing
    dataset = pd.read_csv('data.csv')
    x = dataset.iloc[:, 0].values
    y = dataset.iloc[:, -1].values
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

    # Simple Linear Regression
    b0, b1 = simple_linear_regression(x_train, y_train)

    # Predictions
    y_pred = []
    for i in range(len(x)):
        y_pred.append(predict_slr(b0, b1, x[i]))
    
    # Visualising the results
    plt.scatter(x_train, y_train, color='orange', label = "training set")
    plt.scatter(x_test, y_test, color='red', label = "test set")
    plt.plot(x, y_pred, color='blue')
    
    plt.title('Salary depending on Experience')
    plt.xlabel('Experience')
    plt.ylabel('Salary')
    plt.legend(loc = "upper left")
    plt.show()


