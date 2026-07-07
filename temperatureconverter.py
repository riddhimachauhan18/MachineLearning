import streamlit as st
st.title("Temperature Converter")
c = st.number_input("Temperature in Celsius")
if st.button("Convert"):
    f = (9*c/5)+32
    st.write("Temperature in Fahrenheit =",f)
