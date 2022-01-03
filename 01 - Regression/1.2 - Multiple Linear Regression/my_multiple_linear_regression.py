#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
My multiple linear regression

@author: deronsart
"""

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split



def gradient_descent(x, y, learning_rate, epochs):
    """ 
        Function which calculates the coefficient b and the weights for the multiple linear regression model
        The multiple linear regression formula is : y = b + w1*x1 + w2*x2 + ... + wn*xn
        The method used is the gradient descent, it calculates the loss and adapt the weights each time (epochs), to best fit the model
            Params : the arrays x and y
            Params : the learning_rate and the number of epochs (integers)
            Return : the array w (the weights), and the coefficient b
    """
    w = np.zeros(x.shape[1])
    b = 0 
    for i in range(epochs):
        z = b + x.dot(w)
        loss = z - y
        
        weight_gradient = x.T.dot(loss) / len(y)
        bias_gradient = np.sum(loss) /len(y)
        
        w = w - learning_rate * weight_gradient
        b = b - learning_rate * bias_gradient
        
    return w, b


def predict_mlr(x, w, b):
    """ 
        Function which predict the results for the values of an array x according to a multiple linear regression model
            Params : the array x containing the new values, and w containing the weights
            Param : the integer coefficient b
            Return : the prediction
    """
    return b + x.dot(w)


def r2_score(y, y_pred):
    """ 
        Function which calculates the regression score 
            Param : the array y and y_pred
            Return : the score
    """
    return 1 - (np.sum((y_pred - y)**2) / np.sum((y - y.mean())**2))
    
    


if __name__ == '__main__':
    # Data preprocessing
    dataset = pd.read_csv('data.csv')
    x = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values
    
    ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
    x = np.array(ct.fit_transform(x))
    
    sc = StandardScaler()
    x = sc.fit_transform(x)
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
    
    # Multiple Linear Regression
    w, b = gradient_descent(x_train, y_train, learning_rate=0.002, epochs = 25000)
    
    # Predictions
    y_pred = predict_mlr(x_test, w, b)
    for i in range(len(y_test)):
        print(y_test[i], "/", y_pred[i])
        
    # Regression score
    score = r2_score(y_test, y_pred)
    print("\nScore : " + str(score))    


