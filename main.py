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
        user_loan.setLoanData(loan_data)
        st.session_state.page = 'main'

