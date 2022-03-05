import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline #for encoding

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label' ]
pima = pd.read_csv("diabetes.csv", header=0, names=col_names)

#exploratory data analysis
pima.head()
pima.info()
pima.shape
pima.isnull().any()
sns.pairplot(data=pima, hue='label')
sns.heatmap(pima.corr())
#exploratory data analysis


feature_cols = ['pregnant', 'insulin', 'bmi', 'age', 'glucose', 'bp', 'pedigree']
x=pima[feature_cols] #Features
y=pima.label #Target variable


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1) #70% training and 30% for testing


clf = DecisionTreeClassifier()
clf = clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)


print("Accuracy: ",accuracy_score(y_test, y_pred))
print("Classification report - \n", classification_report(y_test, y_pred))
print("Confusion matrix - \n", confusion_matrix(y_test, y_pred))

#!pip install graphviz
#!pip install pydotplus
#!pip install collections
import graphviz
import pydotplus
import collections
from sklearn import tree

import os
os.environ["PATH"] += os.pathsep + 'C:\ProgramData\Anaconda3\Lib\site-packages\graphviz'


dot_data = tree.export_graphviz(clf, out_file=None, feature_names=feature_cols, class_names=pima.columns[8], filled=True)
graph = graphviz.Source(dot_data, format="png")
graph

