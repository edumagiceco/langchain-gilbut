#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install langchain==0.0.350


# In[2]:


#!pip install streamlit==1.29.0


# In[3]:


#!pip install openai==0.28.1


# In[4]:


import streamlit as st
from langchain.llms import OpenAI
st.set_page_config(page_title="🦜🔗 뭐든지 질문하세요~ ")
st.title('🦜🔗 뭐든지 질문하세요~ ')

import os
os.environ["OPENAI_API_KEY"] = "sk-"  #openai 키 입력

def generate_response(input_text):  #llm이 답변 생성
    llm = OpenAI(model_name='gpt-4-0314', temperature=0)
    st.info(llm(input_text))

with st.form('Question'):
    text = st.text_area('질문 입력:', 'What types of text models does OpenAI provide?') #첫 페이지가 실행될 때 보여줄 질문
    submitted = st.form_submit_button('보내기')
    generate_response(text)


# In[ ]:




