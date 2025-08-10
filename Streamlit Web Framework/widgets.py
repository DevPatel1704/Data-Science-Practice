import streamlit as st
import pandas as pd

st.title("Stream text input")

name = st.text_input("Enter your name : ")
if name : 
    st.write(f"hello, {name}")

age = st.slider("Select your age : ",0,100,25)
st.write(f"Your age is {age}")

options = ["A","B","C","D"]
choice = st.selectbox("Choose your favourite Language : ",options)
st.write(f"You selected {choice}.")


data = {
    "Name" : ["A","B","C","D"],
    "Age" : [10,20,30,20],
    "City" : ["AA","BB","CC","DD"]
}

df=pd.DataFrame(data)
df.to_csv("sample_data.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)