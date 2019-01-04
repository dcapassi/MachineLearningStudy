# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 13:55:06 2019

@author: dmoreira
"""

#Simple Linear Regressionn
#Following the Udemy Machine Learning from A to Z Tutorial

#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the dataset
dataset = pd.read_csv('Salary_Data.csv')

#Creating the Array with the Independat variables
X = dataset.iloc[:, :-1].values

#Creating the Array with the Dependant variables
y = dataset.iloc[:,1].values

#Spliting the Dataset in the TrainningSet and the TestSet
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 1/3, random_state = 0)

#Fitting the Simple Linear Regression to the Trainning Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit (X_train, y_train)

y_pred = regressor.predict(X_test)


##Plotting the TrainningSet results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue' )
plt.title('Salary Vs Experience (TrainingSet)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()











