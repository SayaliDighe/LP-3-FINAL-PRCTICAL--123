import pandas as pd
import numpy as np
df=pd.read_csv("emails.csv")
df.head()
x=df.iloc[:,1:3001]
y=df.iloc[:,3001]
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn import metrics
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.20)
knn=KNeighborsClassifier(n_neighbors=5)
svm=SVC(kernel="linear")
knn.fit(X_train,y_train)
svm.fit(X_train,y_train)
y_pred_knn=knn.predict(X_test)
y_pred_svm=svm.predict(X_test)
print("Accuracy Score of KNN :", metrics.accuracy_score(y_test,y_pred_knn))
print("Accuracy Score of SVM:", metrics.accuracy_score(y_test,y_pred_svm))
print("confusion matrix of KNN:\n" , 
metrics.confusion_matrix(y_test,y_pred_knn))
print("confusion matrix of SVM:\n", 
metrics.confusion_matrix(y_test,y_pred_svm))
print("Classification report of KNN:\n",metrics.classification_report(y_test,y_pred_knn))
print("Classification report of SVM:\n",metrics.classification_report(y_test,y_pred_svm))