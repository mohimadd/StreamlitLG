import streamlit as st
import pickle
import pandas as pd
import numpy as np


PD_Columns = ['gender','age','height','weight','family_history_with_overweight','favc','fcvc','ncp','caec','smoke','ch2o','scc','faf','tue','calc','mtrans']




# Load model 
LG_model = pickle.load(open('Model Logistic Regression.sav','rb'))

# Create Title
st.title('Screening Obesity Prediction')

# seperate into 2 columns

left,right = st.columns(2)

with left:
    gender = st.number_input('Gender')
    st.caption('0 : Female, 1 : Male')

with right :
    age = st.number_input('Age')
    st.caption('Age in Years')

with left:
    height = st.number_input('Height')
    st.caption('Height in Meters, ex : 1.78')

with right :
    weight = st.number_input('Weight')
    st.caption('Weight in Kilograms')

with left :
    Familiy_History_OW = st.number_input('Family History Over Weight')
    st.caption('0 : No, 1 : Yes')

with right :
    FAVC = st.number_input('High Calories Food Consume')
    st.caption('Frequently Consume High Calories Food, 0 : No, 1 : Yes')

with left :
    FCVC = st.slider('Vegetable Consume in a Day',1,3)
    st.caption('Rate Your Frequent Consume Vegetables, 1 : rarely - 3 : Always')

with right :
    NCP = st.number_input('Main Meals')
    st.caption('How Many Main Meals Consume a Day')

with left :
    CAEC = st.number_input('Snack After Meals')
    st.caption('Have You Consume Snack After Eat Meals, 0 : No, 1 : Yes')

with right :
    SMOKE = st.number_input('Smoking Behavior')
    st.caption('0 : No, 1 : Yes')

with left :
    C2HO = st.number_input('Water Drink Daily')
    st.caption('How Much Water Drink Daily in Liters, ex : 1.8')

with right :
    SCC = st.number_input('Calories Monitor Behavior')
    st.caption('0 : No, 1 : Yes')

with left :
    FAF = st.slider('Physical Activity',1,3)
    st.caption('Rate Your Physical Activity, 1 : Sedentary - 3 : Active')

with right :
    TUE = st.slider('Technological Behavior',0,2)
    st.caption('Rate Time For Used Technological Device (Smartphone, laptop, etc), 0 : Rarely - 2 : Active')

with left :
    CALC = st.number_input('Alcohol Behavior')
    st.caption('0 : Rarely, 1 : Frequently')

with right :
    MTRANS = st.number_input('Transportation Behavior')
    st.caption('0 : Public Transportation, 1 : Private Transportation')

# Prediction code
prediction_result = ''

if st.button ('Check Classification Status') :
    columns_predict = PD_Columns

    input_user = [[gender,age,height,weight,Familiy_History_OW,FAVC,FCVC,NCP,CAEC,SMOKE,C2HO,SCC,FAF,TUE,CALC,MTRANS]]
    input_user = pd.DataFrame(input_user, columns=columns_predict)

    obese_prediction = LG_model.predict(input_user)

    if (obese_prediction[0] == 0):
        prediction_result = 'You Predicted Normal Status'
    if (obese_prediction[0] == 1) :
        prediction_result = 'Your Predicted Over Weight Status'
    if (obese_prediction[0] == 2) :
        prediction_result = 'You Predicted Obese'
    st.success(prediction_result)

