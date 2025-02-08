from hmac import new
import streamlit as st
import Loan

def loan_info_form():
    
    if "principalAmount" not in st.session_state:
        st.session_state.principalAmount = ""
    if "interestRatePrecentage" not in st.session_state:
        st.session_state.interestRatePrecentage = ""
    if "termLength" not in st.session_state:
        st.session_state.termLength = ""
    if "minimumPayment" not in st.session_state:
        st.session_state.minimumPayment = ""
    if "paidAmount" not in st.session_state:
        st.session_state.paidAmount = ""
    if "yes_button_pressed" not in st.session_state:
        st.session_state.yes_button_pressed = False
    if "no_button_pressed" not in st.session_state:
        st.session_state.no_button_pressed = False


    with st.form("my_form"):
        st.write("Paying off Student Debt Easier")
        
        principalAmount = st.text_input("Enter Loan Amount: $", placeholder="0.0", value=st.session_state.principalAmount)
        interestRatePrecentage = st.text_input("Enter Interest Rate (APR) (%):", placeholder="0.0", value=st.session_state.interestRatePrecentage)
        termLength = st.text_input("Enter Term Length (months):", placeholder="0", value=st.session_state.termLength)
        minimumPayment = st.text_input("Minimum Monthly Payment:", placeholder="0.0", value=st.session_state.minimumPayment)
        
        st.write("Have you paid off any amount yet?")
        yesCol, noCol = st.columns(2)
        
        with yesCol:
            yesButton = st.form_submit_button("Yes, I have")
            if yesButton:
                st.session_state.yes_button_pressed = True
                st.session_state.no_button_pressed = False
        with noCol:
            noButton = st.form_submit_button("Not Yet")
            if noButton:
                st.session_state.no_button_pressed = True
                st.session_state.yes_button_pressed = False

        paidAmount = st.text_input("How much have you paid towards your account?", placeholder="0", value=st.session_state.paidAmount, disabled=not st.session_state.yes_button_pressed)

        st.write("I am ready to see when I'll be able to pay off my loan")
        submitted = st.form_submit_button("Let's Go")

    if submitted:
        st.session_state.principalAmount = principalAmount
        st.session_state.interestRatePrecentage = interestRatePrecentage
        st.session_state.termLength = termLength
        st.session_state.minimumPayment = minimumPayment
        st.session_state.paidAmount = paidAmount

        # Return collected form data
        return {
            "principalAmount": st.session_state.principalAmount,
            "interestRatePrecentage": st.session_state.interestRatePrecentage,
            "termLength": st.session_state.termLength,
            "minimumPayment": st.session_state.minimumPayment,
            "paidAmount": st.session_state.paidAmount
        }
    else:
        return None 



loan_data = loan_info_form()

if loan_data:
    st.write("Loan Data Collected:")
    st.write(loan_data)
    user_loan = Loan()
    user_loan.setLoanData(loan_data)

    