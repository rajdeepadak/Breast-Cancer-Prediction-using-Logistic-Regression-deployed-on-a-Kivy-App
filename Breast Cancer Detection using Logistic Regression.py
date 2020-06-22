import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataset = pd.read_csv('breast_cancer.csv')
X = dataset.iloc[:, 1:10]
Y = dataset.iloc[:, -1]


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X, Y)


from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X, y = Y, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))


Y_pred = classifier.predict([[4, 4, 2, 3, 3, 4, 5, 4, 2]])
