from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .credit_risk_assessment import load_data,train_model,predict,preprocess_data
#import credit_risk_assessment.py
data = load_data()
X_train_new,X_test_new,Y_train = preprocess_data(data)
clf,tree = train_model(X_train_new,Y_train)
# Create your views here.
def index(request):
    return render(request,'index.html')

def loan_status(request):
    loan_borrower = Borrower()
    loan_borrower.grade = request.POST['loan_grade']
    loan_borrower.defaulter = request.POST['default_on_file']
    #loan_borrower.grade = request.GET['loan_grade']
    #loan_borrower.defaulter = request.GET['default_on_file']
    #loan_borrower.grade = request.GET.get('loan_grade', '')
    #loan_borrower.defaulter = request.GET.get('default_on_file', '')
    print(type(loan_borrower.grade))
    print(f"Grade received: '{loan_borrower.grade}', Defaulter received: '{loan_borrower.defaulter}'")
    #evaluate risk
    risk = predict(clf,loan_borrower.grade,loan_borrower.defaulter)
    if(risk == 0):
        credit_risk = 'low_risk'
    else:
        credit_risk = 'high_risk'
    print(risk)
    return render(request,'index.html',{'credit_risk':credit_risk})

def show_tree(request):
    return render(request,'show.html')

def show_tree(request):
    return render(request,'show.html',{'tree':tree})
