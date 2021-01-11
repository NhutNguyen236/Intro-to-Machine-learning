#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
# sklearn tutorial 
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()
print('ok') 


# In[2]:


import pandas as pd
iris_data = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
print(iris_data.head(5))
print(iris_data.columns)


# In[3]:


from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
iris_data['species'] = LE.fit_transform(iris_data['species'])
X = np.array(iris_data) 
print(X[:5]) 


# In[4]:


# iris.data chứa dữ liệu X 
print(iris.data.shape) # shape của X 
print(iris.target.shape) # shape của labels 
print(iris.data[:10])
print(iris.feature_names)
print(iris.target) # có 3 labels: 0, 1, 2
print(iris.target_names)


# In[5]:


from sklearn.model_selection import train_test_split 
X = iris.data
y = iris.target 
X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=4)
print(X_train.shape,y_train.shape)
print(X_test.shape,y_test.shape)


# In[6]:


# phân loại với KKN
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics 

k = 5
knn = KNeighborsClassifier(n_neighbors=k,metric='euclidean')
knn.fit(X_train,y_train) 
y_pred = knn.predict(X_test)
print('y_pred:\n',y_pred) 
print('y_true:\n',y_test) 

# tính accuracy 
acc_score = metrics.accuracy_score(y_pred,y_test) 
print('accuracy:\n',acc_score) 


# In[7]:


# ví dụ về sử dụng SVM 
from sklearn import svm 
svm_classifier = svm.SVC(kernel='linear',gamma=0.01, C=100.)
svm_classifier.fit(X_train,y_train)


# In[8]:


# predict
y_pred_svm = svm_classifier.predict(X_test)
print('predict:\n',y_pred_svm)
print('y_true:\n',y_test) 

# tính accuracy 
acc_score_svm = metrics.accuracy_score(y_pred_svm,y_test) 
print('accuracy:\n',acc_score_svm) 


# In[ ]:




