import pandas as pd
import matplotlib.pyplot as pyplot
from matplotlib import style
import numpy as np
import sklearn
from sklearn import linear_model, preprocessing
from sklearn.metrics import mean_squared_error, r2_score
import pickle
from math import sqrt


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

    return X_scaled, y, X

def Test(X_test, y_test, acc):

    name = "model_" + str(acc) + ".sav"
    loaded_model = pickle.load(open(name, 'rb'))
    predictions = loaded_model.predict(X_test)
    score1 = loaded_model.score(X_test, y_test)
    score2 = sqrt(mean_squared_error(y_test, predictions))
    print("Acc:", score1, "Mean error:", score2)
    return predictions

def ManualTest(acc):

    name = "model_" + str(acc) + ".sav"
    loaded_model = pickle.load(open(name, 'rb'))

    time = int(input("Time in minutes: "))
    verified = int(input("verified, 0 or 1: "))
    comments = int(input("number of comments: "))
    retweets = int(input("number of retweets: "))
    likes = int(input("number of likes: "))
    X_test = [[time, verified, comments, retweets, likes]]
    
    predictions = loaded_model.predict(X_test)

def Plot(y_label, y_data, x_label, x_data):

    x_df = pd.DataFrame({x_label:x_data})
    y_df = pd.DataFrame({y_label:y_data})

    style.use("ggplot")
    pyplot.scatter(x_df[x_label], y_df[y_label])
    pyplot.xlabel(x_label)
    pyplot.ylabel(y_label)
    pyplot.show()

modelacc = float(input("Model acc: "))
X, y, X_unscaled = getData()
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y, test_size = 0.99)
predictions = Test(X_test, y_test, modelacc)
Plot("y", y_test, "predictions", predictions)
Plot("likes", X_unscaled[:,4], "followers", y)
#Plot("time", X_unscaled[:,0], "followers", y)
Plot("comments", X_unscaled[:,2], "followers", y)
Plot("retweets", X_unscaled[:,3], "followers", y)
