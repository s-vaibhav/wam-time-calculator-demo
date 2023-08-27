# 23 Feb 2023

import streamlit as st

st.title("WAM Time Calculator")
st.code('''Estimate the number of hours for all your units combined per week required to 
achieve your desired WAM this trimester. These number of hours includes all 
study time, including time for attending class, making notes, doing assignments 
and preparing for quizes and exams. This number would also help you understand 
how fast or slow you need to work.''', language=None)

st.markdown('''---''')
col1, col2 = st.columns(2)


st.markdown("#### 1. WAM Time equation (as recommended by the university)")
st.code("50 WAM = 10 hours per unit per week")

st.markdown("#### 2. Select desired WAM for this trimester to estimate the hours required per unit per week")
slide1 = st.slider("Desired WAM", 50, 100, step=5)
slide2 = st.slider("Hours per unit per week required", 10, 20, value=slide1//5, disabled=True)


st.markdown("#### 3. Select number of units taken for this trimester to add to the calculation")
slide3 = st.slider("Number of units", 1, 6, step=1)

st.markdown("#### 4. Result")
st.title(f"Total of {slide2 * slide3} hours")
f"of study time per week for {slide3} unit/s to obtain a {slide1} WAM. {slide2 * slide3} hours is {round(((slide2*slide3)/(5*24))*100, 1)}% of the workweek (Mon-Fri)."

st.markdown("---")
st.markdown("#### Leave your feedback")
radio = st.radio("Was this app helful to you?", ["Yes :)", "No :("])
st.text_area("Comments (optional)")
feedbacksubmit_button = st.button("Submit", key=2)

if feedbacksubmit_button:
    if radio == "Yes :)":
        st.success("This is a demo app, feedback doesn't actually get submitted.")
    else:
        st.success("This is a demo app, feedback doesn't actually get submitted.")
