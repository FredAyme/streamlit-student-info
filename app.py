import streamlit as st

# Title of the app
st.title("Student Information")

# input name
# st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible", icon=None, width="stretch", bind=None)
student_name = st.text_input("enter the name of the student")

# select age
student_age = st.slider("enter the age")

# Button to display text & age
if st.button("Display Info"):
    st.write("Student's name: ", student_name)
    st.write("Student's age: ", student_age)
