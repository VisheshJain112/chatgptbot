from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from gpt_index import SimpleDirectoryReader,GPTListIndex,GPTSimpleVectorIndex,LLMPredictor,PromptHelper
from langchain import OpenAI
import sys
import os
import gradio as gr


agent = create_csv_agent(OpenAI(temperature=0), "doc_dump/program_details - program_details.csv.csv", verbose=True)


agent.run("NUMBER OF GMO partners in Canada")