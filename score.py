# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:37:48 2022

@author: jagar
"""
import streamlit as st
import pickle
from sklearn.linear_model import LinearRegression 
finalmodel = pickle.load(open('finalmodel.pkl','rb'))

gre_score = st.number_input("enter GRE score")
toefl_score = st.number_input("enter TOEFL score")
ur_score = st.number_input("enter University ranking")
sop_score = st.number_input("enter SOP score")
lor_score = st.number_input("enter LOR score")
cgpa=st.number_input("Enter Cgpa")
research = st.number_input("Research")

result = finalmodel.predict([[gre_score,toefl_score,ur_score,sop_score,lor_score,cgpa,research]])

st.header(result)