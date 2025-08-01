import io
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score,classification_report
from sklearn.preprocessing import OneHotEncoder
from django.core.files.base import ContentFile
# credit_risk_assessment.py

from .models import * # Replace 'visualizer' with your actual app name

def load_data():
    df = pd.read_csv('/home/shoun1/risk_assessment/risk_assessment/credit_risk_dataset.csv')
    return df
    

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
    
    buf = io.BytesIO()
    fig, ax = plt.subplots(figsize=(12, 8))
    plot_tree(clf,feature_names=['A','B','C','D','E','F','G','Y','N'],class_names=['0','1'],filled=True)
    fig.savefig(buf, format='png')
    buf.seek(0)

    # Create and save the model instance
    tree_image = Plots(name='my_tree_plot')
    #tree_image.save('tree_plot.png', ContentFile(buf.read()))
    tree_image.save()
    buf.close()
    plt.close(fig)         
    return clf,tree_image

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

