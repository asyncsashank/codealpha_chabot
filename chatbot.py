
import streamlit as st

st.title("FAQ Chatbot")

faq = {
    "what is ai": "AI stands for Artificial Intelligence. It refers to computer systems designed to perform tasks that typically require human intellect, such as learning from data, recognizing speech, understanding language, and solving problems.",
    "what is python": ".",
    "what is machine learning": "Machine Learning allows systems to learn from data.",
    "who developed python": "Python was developed by Guido van Rossum."
}

question = st.text_input("Ask Question")

if st.button("Get Answer"):

    question = question.lower()

    if question in faq:
        st.success(faq[question])
    else:
        st.error("Question not found")
