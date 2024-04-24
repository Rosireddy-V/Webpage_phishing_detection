import streamlit as st
import numpy as np
import pickle
import functions

model = pickle.load(open('model_13.pkl','rb'))
# Use the loaded model for predictions or further training


st.header('Webpage Phishing Detection')



q1 = st.text_input('Enter the url')
q2 = st.number_input('Enter the number of redirections in the url')
spchar=functions.extract_url_features(q1)
inputs=functions.r_inputs(spchar,q2)

if st.button('Check'):
    predictions = (model.predict(inputs)>0.5).astype(int)
    if predictions[0][0]==1:
        st.header("Phishing")
    else:
        st.header("Not Phishing")
#print(predictions[0][0])