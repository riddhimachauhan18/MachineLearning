import streamlit as st
st.title("Student Result")
name=st.text_input("Student Name")
m1=st.number_input("python")
m2=st.number_input("java")
m3=st.number_input("DBMS")
percentage=(m1+m2+m3)/3
if st.button("Show Result"):
    st.write("Student:",name)
    st.write("Percentage:",round(percentage,2))
    if percentage>=60:
        st.success("First Devision")
    elif percentage>=45:
        st.success("Second Devision")
    elif percentage>=33:
        st.warning("Third Division")
    else:
        st.error("Fail")
