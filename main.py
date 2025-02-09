import streamlit as st
import form 
from Loan import Loan

st.image("images/pop_logo.png", width=200)

def go_to_page(page_name):
    st.session_state.page = page_name

    with open('designs.html') as file:
        html_content = file.read()
        st.markdown(html_content, unsafe_allow_html=True)
    
if 'page' not in st.session_state:
    st.session_state.page = 'main'
    go_to_page("main")

if st.session_state.page == 'main':
    st.title("Pay Off Pal")
    studentCol, ratingCol = st.columns(2)

    with studentCol:
        st.image("images/one-in-four-students.png", width=200)
    

    if st.button("Let us help you out!"):
        go_to_page("form")

if st.session_state.page == 'form':
    loan_data = form.loan_info_form()

    if loan_data:
        st.write("Loan Data Collected:")
        st.write(loan_data)
        user_loan = Loan()
        user_loan.SetLoanData(loan_data)
        getData = user_loan.GetLoan()
        
        min_payment_amount = getData["montly_payment"] #amount
        payment_months = getData["term_length"] #months

        result_string = f"If you pay ${min_payment_amount:.2f} every month you'll be able to pay off your loan by {payment_months} months"
        st.write(result_string)
        st.write("Keep up the good work!")
        st.write("Click Let's Go to go back to the main page")


        st.session_state.page = 'main'

