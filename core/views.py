from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.
import joblib

AdaBoostRegressor = joblib.load('./models/Ada Boost Regressor.pkl')
ARDRegression = joblib.load('./models/ARDRegression.pkl')
BaggingRegressor = joblib.load('./models/Bagging Regressor.pkl')
BayesianRidge = joblib.load('./models/Bayesian Ridge.pkl')
DecisionTreeRegressor = joblib.load('./models/Decision Tree Regressor.pkl')
ExtraTreeRegressor = joblib.load('./models/Extra Tree Regressor.pkl')
GammaRegressor = joblib.load('./models/Gamma Regressor.pkl')
GradientBoostingRegressor = joblib.load('./models/Gradient Boosting Regressor.pkl')
HistGradientBoostingRegressor = joblib.load('./models/Hist Gradient Boosting Regressor.pkl')
HuberRegressor = joblib.load('./models/Huber Regressor.pkl')
Lasso = joblib.load('./models/Lasso.pkl')
LinealRegression = joblib.load('./models/Lineal Regression.pkl')
PassiveAggressiveRegressor = joblib.load('./models/Passive Aggressive Regressor.pkl')
PoissonRegressor = joblib.load('./models/Poisson Regressor.pkl')
RandomForestRegressor = joblib.load('./models/Random Forest Regressor.pkl')
TweedieRegressor = joblib.load('./models/Tweedie Regressor.pkl')


def index(request):
    context = {'a': 'HelloWorld!'}
    return render(request, 'index.html', context)
    #return HttpResponse({'a':1})

def predict(request):
    print(request)
    if request.method == 'POST':

        temp= []
        temp.append(float(request.POST.get('temp9Val')))
        temp.append(float(request.POST.get('presion3Val')))
        temp.append(float(request.POST.get('humedad3Val')))
        temp.append(float(request.POST.get('presion9Val')))
        algoritmoNombre = (request.POST.get('algoritmo'))
        algoritmo = eval(request.POST.get('algoritmo'))
    print(algoritmo)
    scoreval = algoritmo.predict([temp])
    context={'scoreval':round(scoreval[0],1), 'algoritmo':algoritmoNombre}
    return render(request, 'index.html',context)