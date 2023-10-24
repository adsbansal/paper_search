import os 
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

def get_answer(topic, key):
    # Setting the replicate API token
    os.environ["OPENAI_API_KEY"] = key 

    # LLM - # _ = llm(prompt)
    llm = OpenAI(
        # streaming=True,
        # callbacks=[StreamingStdOutCallbackHandler()],
        model_name="gpt-3.5-turbo",
    )

    # Template Setting -
    template = """
    User: You are a research assistant:
    Do the following tasks according to the sequence
    1. Use you own knowledge and explain the development of scientific research done on the topic {topic}. Answer in 50 words.
    2. Get the latest research papers by using a tool.
    3. Get the latest YouTube videos by using a tool.

    Assistant:
    """
    prompt_template = PromptTemplate(
        input_variables=["topic"],
        template=template
    )

    prompt = prompt_template.format(topic=topic)


    # Classes for the LLM Tools


    class paper_tool(BaseTool):
        name = "get_research_papers"
        description = "This tool allows you to get the latest research papers in the given specified topic"

        def _run(self, topic: str):
            return search_scholar(topic)

    class youtube_tool(BaseTool):
        name = "get_youtube_videos"
        description = "This tool allows you to get the latest YouTube videos for a specified topic"

        def _run(self, topic: str):
            return search_youtube(topic)


    # Instantiating the Classes and Setting Tool list
    paper_getter = paper_tool()
    youtube_getter = youtube_tool()

    tools = [paper_getter, youtube_getter]

    # Setting up the Agent and LLM
    conversational_agent = initialize_agent(
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        # agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        tools=tools, 
        llm=llm,
        verbose=True,
        max_iterations=2
    )

    return conversational_agent.run(prompt)