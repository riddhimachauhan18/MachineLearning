import streamlit as st
st.title("Age Calculator")
birth = st.number_input("Birth Year",1900,2026)
current = st.number_input("Current Year",2026)
if st.button("Calculate"):
age = current-birth
st.write("Age =",age)
