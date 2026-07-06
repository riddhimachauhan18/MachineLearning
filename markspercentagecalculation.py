import streamlit as st
st.title("Percentage Calculator")
m1 = st.number_input("English")
m2 = st.number_input("Math")
m3 = st.number_input("Science")
total = m1+m2+m3
percentage = total/3
if st.button("Calculate"):
    st.write("Percentage =",percentage,"%")
if percentage>=33:
    st.success("Pass")
else:
    st.error("Fail")
