import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score,classification_report
from sklearn.preprocessing import OneHotEncoder
import os
import pandas as pd

file_path = r'd:\pythonenv\risk_assessment\risk_assessment\credit_risk\credit_risk_data.csv'

try:
    df = pd.read_csv(file_path)
    print("Data loaded:", df.shape)
except FileNotFoundError:
    print(" File not found at:", file_path)
except Exception as e:
    print(" Other error:", e)


def preprocess_data(data):
    #remove missing values 
    ser = data.isnull().sum()
    ser = ser.to_dict()
    nan_cols=[]
    for key,value in ser.items():
        if value != 0:
            nan_cols.append(key)
    for col in nan_cols:
        data.dropna(subset=[col],inplace=True)
    
    #encode categorical values
    batch_data = data.sample(n=5000)
    #dependent and independent
    X = batch_data[['loan_grade','cb_person_default_on_file']].values
    Y = batch_data['loan_status'].values
    #split train test data
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.20,random_state=0,shuffle=True)
    ohe = OneHotEncoder()
    X_train_new = ohe.fit_transform(X_train[:,0:2]).toarray()
    X_test_new = ohe.fit_transform(X_test[:,0:2]).toarray()
    return X_train_new,X_test_new,Y_train

def train_model(X_train_new,Y_train):
    clf = DecisionTreeClassifier()
    clf.fit(X_train_new,Y_train)
    return clf

def predict(clf,grade,defaulter):
    X_new = np.zeros((1,9))
    if(grade == "A"):
        X_new[0,0] = 1.
    elif(grade == "B"):
        X_new[0,1] = 1.
    elif(grade == "C"):
        X_new[0,2] = 1.
    elif(grade == "D"):
        X_new[0,3] = 1.
    elif(grade == "E"):
        X_new[0,4] = 1.
    elif(grade == "F"):
        X_new[0,5] = 1.
    else:    
        X_new[0,6] = 1.

    if(defaulter == "Y"):
       X_new[0,7]  = 1.
    else:
       X_new[0,8] = 1.
    print(X_new)
    y_pred = clf.predict(X_new)
    return y_pred


#X_new = [[0., 0., 0., 0., 1., 0., 0., 1., 0.]]
#pred = predict(clf,X_new)
#pred = predict('C','N')
#print(pred)

