# AI-Data-science-Tutor

import streamlit as st
import google.generativeai as genai
import os



st.title(":rainbow[AI Data Science Tutor] ")

#read the key


f=open("C:\OpenAI\Gemini_app\keys\gemini_api_key.txt.txt")
key=f.read()


genai.configure(api_key=key)

#Init gemini model

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              

                              system_instruction=""" You are a helpful and friendly AI assistant.
                              For a given  Data Science topic help the user to undersatand the topic with very good explanation 
                              with very good easy understandable example.
                              If a question is related to data science.""")

# if there is no chat_history in session, init one
if "messages" not in st.session_state.keys():
    st.session_state.messages=[
        {'role':"assistant",'content':"Hello, this is Chitti. How can I help you? "}
    ]

#init the chat object


for messages in st.session_state.messages:
    with st.chat_message(messages['role']):
        st.write(messages['content'])



user_input= st.chat_input()

if user_input is not None:
    st.session_state.messages.append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.write(user_input)

if st.session_state.messages[-1]['role'] !='assistant':
    with st.chat_message('assistant'):

        with st.spinner("Loading..."):

            ai_response=model.generate_content(user_input)
            st.write(ai_response.text)
        new_ai_message ={'role':'assistant','content':ai_response.text}
        st.session_state.messages.append(new_ai_message)

   
