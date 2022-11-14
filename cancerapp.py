import streamlit as st
import pickle
import pandas as pd
st.title("Breast cancer detection")

radius_mean=st.number_input('radius_mean')
radius_worst=st.number_input('radius_worst')
texture_worst=st.number_input('texture_worst')
perimeter_worst=st.number_input('perimeter_worst')


if st.button('predict'):
    r = pickle.load(open('cancer.pkl','rb')) 
    
    
    
    
    #k=open('cancer.pkl','rb')
    #r=pickle.load(k)
    x = pd.DataFrame([[radius_mean,radius_worst,texture_worst,perimeter_worst]],
                  columns =['radius_mean','radius_worst','texture_worst','perimeter_worst'])
    prediction=r.predict(x)
    if prediction == 1:
        prediction='Malignant'
    elif prediction==0:
        prediction='Bengin'
        
        
    st.success(f'cancer type {prediction} ')