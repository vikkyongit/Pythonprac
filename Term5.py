from sklearn.datasets import load_iris

irisd=load_iris()

print("keys \n{}".format(irisd.keys()))

print(irisd['DESCR'])

print(irisd.data.shape)

print(irisd.data[0:5])

from sklearn.model_selection import train_test_split

X_train, X_test,y_train,y_test=train_test_split(irisd.data, irisd.target,random_state=0)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from sklearn.neighbors import KNeighborsClassifier 

knn=KNeighborsClassifier(n_neighbors = 8)
knn.fit(X_train, y_train)

import numpy as np
x_new = np.array([[5,2.9,1,0.2]])

prediction = knn.predict(x_new)

print("Prediction of test instance {}".format(prediction))

print("predicted_target_name: {}".format(irisd['target_names'][prediction]))

y_pred=knn.predict(X_test)

print("Accuracy of the model:{}".format(knn.score(X_test,y_test)))

confusion_matrix(y_test,y_pred)

print("Other performance measure: {}".format(classification_report(y_test,y_pred)))

