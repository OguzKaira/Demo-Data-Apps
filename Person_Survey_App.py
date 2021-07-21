import streamlit as st

st.title("Person Survey")
st.markdown("### This survey, which contains your personal information, has been created to serve you better")

user = st.text_input("Enter Name:")
age = st.number_input("Enter Age:")

like = st.radio("What Do You Like More:", ("Play Games" , "Reading Book" , "Watching Movie"))

country = st.text_input("Enter Your Country")
time = st.slider("How many years have you been using a phone?", 0,80)

name = st.checkbox("Don't show my name")
send = st.button("Send Answers")

if(send and name):
    st.success(f"""Thanks For Answer, Your Answers:
    \nName: {"Private"}
    \nAge: {age}
    \nYour Like: {like.title()}
    \nCountry: {country}
    \nYou Have Been Use Phone: {time}
    """)

elif(send and not name):
    st.success(f"""Thanks For Answer, Your Answers:
    \nName: {user}
    \nAge: {age}
    \nYour Like: {like.title()}
    \nCountry: {country}
    \nYou Have Been Use Phone: {time}
    """)
