import numpy as np
import sklearn
from sklearn import linear_model, preprocessing
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import matplotlib.pyplot as pyplot
from matplotlib import style
from math import sqrt
import pickle

def getData():

    data = pd.read_csv("Train.csv")

    #print(data.head())

    predict = "followers"
    labels = ["time", "verified", "comments", "retweets", "likes"]

    #X = np.array(data.drop([predict], 1))
    X = np.array(data[labels])
    scaler = preprocessing.RobustScaler(quantile_range=(20, 80)).fit(X)
    X_scaled = scaler.transform(X)

    y = np.array(data[predict])

    return X_scaled, y

def Train(X, y):

    best = 0

    for i in range(100):
        X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
            X, y, test_size = 0.1)

        linear = linear_model.Ridge()

        linear.fit(X_train, y_train)

        predictions = linear.predict(X_test)

        for x in range(len(predictions)):
            predictions[x] = int(predictions[x])
            #print(predictions[x], "-", y_test[x])

        '''print("Mean squared error: \n",
              mean_squared_error(y_test, predictions))
        print("Root Mean squared error: \n",
              sqrt(mean_squared_error(y_test, predictions)))'''

        score = r2_score(y_test, predictions)
        print("Variance score: \n", score)
        if score > best:
            best = score
            filename = 'model_' + str(round(score, 2)) + '.sav'
            pickle.dump(linear, open(filename, 'wb'))


X, y = getData()
Train(X, y)
