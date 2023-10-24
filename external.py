import streamlit as st
from langchain.llms import OpenAI
import os 
from internal import get_answer
import sys
sys.path.append("Tools")
from google_scholar import search_scholar
from youtube_search import search_youtube
from langchain.llms import OpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.agents import Tool
from langchain.tools import BaseTool
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.prompts.chat import SystemMessagePromptTemplate
from langchain.prompts import PromptTemplate

st.title("360 - Research Papers")
st.markdown("Please enter the topic you want to write a research paper on - This tool will give you a brief on the topic along with few recent high citation papers and started YouTube Links.")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


with st.form("my_form"):
    text = st.text_area("Enter text:", "Solving the Markovitz Problem in a Bayesian setting")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        get_answer(topic, openai_api_key)