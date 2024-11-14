import pandas as pd
import numpy as np
df=pd.read_csv("Diabetes.csv")
df.head()
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
x=df.iloc[:,:-1]
y=df.iloc[:,-1]
X_train ,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
print(y_pred)
print("Confusion matrix:\n" ,metrics.confusion_matrix(y_test,y_pred))
print("Accuracy Score:\n" ,metrics.accuracy_score(y_test,y_pred))
print("Error rate:", 1-metrics.accuracy_score(y_test,y_pred))
print("Precison Score:\n" ,metrics.precision_score(y_test,y_pred))
print("Recall Score:\n" ,metrics.recall_score(y_test,y_pred))