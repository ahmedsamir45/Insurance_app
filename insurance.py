#!/usr/bin/env python
# coding: utf-8

# ai\Scripts\activate
# python insurance.py
import pandas as pd
import numpy as np


from flask import render_template ,url_for,flash ,redirect,request
from flask import Flask
data = pd.read_csv('insurance.csv')

columns= list(data.columns)
print(columns)

data2 = data.drop(data.select_dtypes(include='object'),axis=1)


columns_desc = [" age of primary beneficiary",
                
                " insurance contractor gender, female, male",

                " Body mass index, providing an understanding of body, weights that are relatively high or low relative to height objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9",\
                    " Number of children covered by health insurance / Number of dependents",\
                        "Smoking"," the beneficiary's residential area in the US, northeast, southeast, southwest, northwest.",
                        "Individual medical costs billed by health insurance"]


from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer



categorical_feature = ['sex','smoker','region']
one_hot = OneHotEncoder()

transformer=ColumnTransformer([("one_hot",one_hot,categorical_feature)],remainder="passthrough")
transform_insurance=transformer.fit_transform(data)







pd.DataFrame(transform_insurance)



dummies = pd.get_dummies(data,columns=categorical_feature)





x = dummies.drop('charges',axis=1)
y = dummies['charges']


from sklearn.model_selection import train_test_split
x_train,x_test,y_train ,y_test = train_test_split(x,y,test_size=0.2)



from sklearn.ensemble import RandomForestRegressor
model1 = RandomForestRegressor()






model1.fit(x_train,y_train)




print(len(columns))
print(len(columns_desc))




app = Flask(__name__)


@app.route("/")
def Home():

    return render_template('home.html',message='hello from home page',custom='home')



@app.route('/charge',methods=['GET',"POST"])
def Charges():
    sex_unique = list(data['sex'].unique())
    region_unique = list(data['region'].unique())
    smoker_unique = list(data['smoker'].unique())


    return render_template('charge.html',sex_unique=sex_unique,region_unique=region_unique,smoker_unique=smoker_unique,custom="charge")


@app.route('/predict',methods=['GET',"POST"])
def predict():
    age = request.form.get('age')
    bmi = request.form.get('bmi')
    sex = request.form.get('gens')
    children = request.form.get('ch')
    smoker = request.form.get('smoker')
    region1 = request.form.get('regions')
    
    region_northwest=[]
    region_northeast=[]
    region_southeast=[]
    region_southwest=[]

    if sex=='male':
        sex_male=1
        sex_female=0
    else:
        sex_male=0
        sex_female=1

    if region1=='southwest':

    
        region_northwest.append(0)
        region_northeast.append(0)
        region_southwest.append(1)
        region_southeast.append(0)


    elif region1=='southeast':
        
        region_northwest.append(0)
        region_northeast.append(0)
        region_southwest.append(0)
        region_southeast.append(1)

    elif region1=='northwest':

        region_northwest.append(1)
        region_northeast.append(0)
        region_southwest.append(0)
        region_southeast.append(0)

    elif region1=='northeast':
        region_northwest.append(0)
        region_northeast.append(1)
        region_southwest.append(0)
        region_southeast.append(0)


    if smoker=='yes':
        smoker_yes=1
        smoker_no = 0
    else:
        smoker_yes=0
        smoker_no=1

    x_T = pd.DataFrame({'age':[age],'bmi':[bmi],'children':[children],'sex_female':[sex_female],'sex_male':[sex_male],'smoker_no':[smoker_no],'smoker_yes':[smoker_yes],\
                        'region_northeast':region_northeast,'region_northwest':region_northwest,'region_southeast':region_southeast,'region_southwest':region_southwest})

        
    y_predict = model1.predict(x_T)

    charge = y_predict[0]

    return render_template('predict.html',charge=charge,custom='predict',age=age,bmi=bmi,region1=region1,smoker=smoker,sex=sex)

@app.route("/visualization")
def Visualization():
    return render_template('visualization.html',message='hello from data visualization',custom='visualization')

@app.route("/About")
def About():

   
    shape = data.shape
    std = data2.std()
    max = data.max()
    min = data.min()
    nunique = data.nunique()

    score=f'{model1.score(x_test,y_test)*100:0.2f} %'



    

    return render_template('about.html',custom="about"
                        ,packed=zip(columns,columns_desc),
                           columns=columns,columns_desc=columns_desc,score=score
                          ,shape=shape,std=std,max=max,min=min,nunique=nunique)


if __name__ == '__main__':
    app.run(debug=True,port=9000)

