import pickle
import streamlit as st
model = pickle.load(open('lrmodel.pkl','rb'))

st.title('Insurance Claims Charges Predictor')
st.header('Input insurance holder information:')

def user_input(): 
    age = float(st.number_input('Age:'))
    sex = int(convert_sex(st.radio('Sex:', options = ['M', 'F'])))
    bmi = float(st.number_input('BMI:'))
    children = float(st.number_input('Num. of Children:'))
    smoker = int(convert_smoker(st.radio('Smoker:', options = ['Y', 'N'])))

def convert_sex(input): 
    return 1 if input=='M' else 0 

def convert_smoker(input): 
    return 1 if input=='Y' else 0 

with st.form(key='input'): 
    df = user_input() 
    st.form_submit_button('Submit')