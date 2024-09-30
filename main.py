import  streamlit as st
name = st.text_input("Enter Your Name :   ")
fname = st.text_input("Enter Fathers Name :   ")
addr = st.text_input("Enter Your Address :   ")
gender = st.text_input("Enter Your Gender :   ")
button = st.button("Done")
if button:
    st.markdown(f"""
    Name : {name}
    Fathers : {fname}
    Address : {addr}
    Gender : {gender}""")