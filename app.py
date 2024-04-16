from openai import OpenAI
import streamlit as st

f = open("key/.openai_api_key.txt")
key = f.read()
client = OpenAI(api_key=key)

st.snow()

st.title("😊AI code Reviewer")
st.subheader("Soon to be Billion Dollar App Idea💲💲💲")

#  mcq_creator(prompt):
prompt = st.text_input("Enter your python code here")

if st.button("Generate") == True:
    # st.balloons()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": """You are an AI code reviewer, User will enter the code and you will review the code and 
                         tells how many and what bugs are there and also print the corrected code"""},
            {"role": "user", "content": prompt}
        ]
    )
    st.write(response.choices[0].message.content)

st.text("\n")
st.write("©️© Ayush Raj")
