from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier #Multi Learn Perseption
from sklearn.model_selection import train_test_split

irisd=load_iris()

print(irisd.data[0:10])

X_train, X_test, y_train, y_test = train_test_split(irisd.data, irisd.target, random_state=10)

mlp=MLPClassifier(solver='sgd',hidden_layer_sizes=(3,), random_state=0)

mlp.fit(X_train, y_train)

print("Accuracy:{}".format(mlp.score(X_test,y_test)))

print("weights between input and 1st layer")
print(mlp.coefs_[0])

print("weights between 1st and 2nd layer")
print(mlp.coefs_[1])

y_pred=mlp.predict(X_test)
print("Predicted values: \n", y_pred)

from sklearn import metrics
print("Accuracy: \n", metrics.confusion_matrix(y_test, y_pred))

print("Accuracy:\n",metrics.accuracy_score(y_test,y_pred))

