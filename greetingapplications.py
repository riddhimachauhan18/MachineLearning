import streamlit as st
st.title("Welcome App")
name=st.text_input("Enter Your Name")
if st.button("Submit"):
    st.success("Welcome"+name)
