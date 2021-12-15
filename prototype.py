# Protoype for business idea
# Janine Simons
# December 15, 2021

import streamlit as st

st.set_page_config(page_title="Prototype for inspiration app", initial_sidebar_state="auto")
trend_title = """
             <h1 style = "color: 332E34; text-align: center" > Prototype for inspiration app</h1>
             <h5 style = "color: #2F2523; text-align: center" > Stories to inspire you</h5>
             """
st.sidebar.subheader("Profile")
st.sidebar.radio("Your gender ", ["Male", "Female", "Unknown"])
st.sidebar.multiselect('Situation', ["Single","Married","Divorced"])
st.sidebar.number_input('Age')
st.sidebar.text_input("Profession")

check_button = st.sidebar.button("Inspire")

if check_button:
   st.markdown(trend_title, unsafe_allow_html=True)
   st.image("book_melindagates.jpg", width=200)
   st.image("audio_women.jpg", width=200)
   st.image("picture.jpg", width=200)
   st.balloons()







