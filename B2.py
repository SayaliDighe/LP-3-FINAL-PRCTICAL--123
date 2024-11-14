#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('emails.csv')


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


# input data
x = df.drop(['Email No.','Prediction'], axis = 1)

#output data
y = df['Prediction']


# In[6]:


x.shape


# In[7]:


set(x.dtypes)


# In[8]:


import seaborn as sns
sns.countplot(x = y);


# In[9]:


y.value_counts()


# In[12]:


#Feature Scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)


# In[13]:


x_scaled


# In[15]:


#Cross-validation
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, random_state=0, test_size=0.25)


# In[16]:


x_scaled.shape


# In[17]:


x_train.shape


# In[18]:


x_test.shape


# In[19]:


#import the class
from sklearn.neighbors import KNeighborsClassifier


# In[20]:


#create the object
knn = KNeighborsClassifier(n_neighbors=5)


# In[21]:


#train the algorithm
knn.fit(x_train, y_train)


# In[22]:


#predict on test data
y_pred = knn.predict(x_test)


# In[23]:


# Import the evaluation metrics
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score
from sklearn.metrics import classification_report


# In[24]:


ConfusionMatrixDisplay.from_predictions(y_test, y_pred)


# In[25]:


y_test.value_counts()


# In[26]:


accuracy_score(y_test, y_pred)


# In[27]:


print(classification_report(y_test, y_pred))


# In[28]:


import numpy as np
import matplotlib.pyplot as plt


# In[29]:


error = []
for k in range(1,14):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    pred = knn.predict(x_test)
    error.append(np.mean(pred != y_test))


# In[30]:


error


# In[31]:


knn = KNeighborsClassifier(n_neighbors=1)


# In[32]:


knn.fit(x_train, y_train)


# In[33]:


y_pred = knn.predict(x_test)


# In[34]:


accuracy_score(y_test, y_pred)


# In[36]:


from sklearn.svm import SVC


# In[37]:


svm = SVC(kernel = 'linear')


# In[38]:


svm.fit(x_train, y_train)


# In[39]:


y_pred = svm.predict(x_test)


# In[40]:


accuracy_score(y_test, y_pred)


# In[ ]:


# Linear: 0.9767981438515081
# RBF: 0.9450889404485692
# polynomial: 0.7548337200309359

