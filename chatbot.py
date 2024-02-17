import streamlit as st
import google.generativeai as genai
 
genai.configure(api_key='AIzaSyBLD5xONBnM-wmjnNKgZXhGQsmIIswG7Zo')
 
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title='Gemini-Pro', page_icon='🤖')

st.title("Gemini-Pro ChatBot 🔬📊🤖 ")
st.sidebar.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', use_column_width='always')
st.sidebar.markdown('''
### About this project
This **Streamlit App** is a chatbot powered by Gemini-Pro made by Luiza Carneiro on 02/16/24.
                    
The source code can be found at https://github.com/luiza218
''')
st.sidebar.markdown('''                  
### About the programmer
Luiza is a 2nd year Computer Science student at Universidade Fumec, Brazil.
She is envolved currently in the data engineering field, providing solutions, collecting data and providing them to the company's needs and expectations.
She has an advanced domain in Python and loves creating bots and data-science apps in Streamlit. She is also fluent in the English language.
''')

user_input = st.text_area("Hey you, ask me anything!", key='input', height=100)
 
if st.button("Send"):
    if user_input:
        st.write("Chatbot:")
        with st.spinner("Generating response..."):
            chat = model.start_chat()
            response = chat.send_message(user_input)
            st.info(response.text)