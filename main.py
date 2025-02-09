import streamlit as st
import form 
from Loan import Loan

if 'page' not in st.session_state:
    st.session_state.page = 'main'

def go_to_page(page_name):
    st.session_state.page = page_name

if st.session_state.page == 'main':
    st.title("Pay Off Pal")

    if st.button("Let us help you out"):
        go_to_page("form")

if st.session_state.page == 'form':
    loan_data = form.loan_info_form()

    if loan_data:
        st.write("Loan Data Collected:")
        st.write(loan_data)
        user_loan = Loan()
        user_loan.SetLoanData(loan_data)
        st.session_state.page = 'main'

