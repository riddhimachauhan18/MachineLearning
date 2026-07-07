import streamlit as st
st.title("Even Odd Checker")
num = st.number_input("Enter Number",step=1)
if st.button("Check"):
if num%2==0:
st.success("Even Number")
else:
st.error("Odd Number")
