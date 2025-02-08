import streamlit as st

with st.form("my_form"):
    st.write("Paying off Student Debt Easier") # need to rework the description of the form
    principalAmount = st.text_input("Enter Loan Amount: $", placeholder="0.0")
    interestRatePrecentage = st.text_input("Enter Interest Rate (APR) (%):", placeholder="0.0")
    termLength =  st.text_input("Enter Term Length:", placeholder="0")
    isMinimumPayment = st.checkbox("Do you have a minimum payment per month?")
    st.write("Have you paid off any amount yet?")


    yesCol, noCol = st.columns(2)
    with yesCol:
           yesButton =  st.form_submit_button("Yes")
    with noCol:
          noButton = st.form_submit_button("No")
          
    if yesButton:
           paidAmount =  st.text_input("How much have you paid towards your account?", placeholder="0")


    st.write("I am ready to see when I'll be able to pay off my loan")
    submitted = st.form_submit_button("Let's Go")