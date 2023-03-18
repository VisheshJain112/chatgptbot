from gpt_index import SimpleDirectoryReader,GPTListIndex,GPTSimpleVectorIndex,LLMPredictor,PromptHelper
from langchain import OpenAI
import sys
import os
import gradio as gr
os.environ["OPENAI_API_KEY"] =  "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"

def create_index(path):
  max_input = 4096
  tokens = 200
  chunk_size = 600 #for LLM, we need to define chunk size
  max_chunk_overlap = 20

  promptHelper = PromptHelper(max_input,tokens,max_chunk_overlap,chunk_size_limit=chunk_size)  #define prompt

  llmPredictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-ada-001",max_tokens=tokens)) #define LLM
  docs = SimpleDirectoryReader(path).load_data() #load data

  vectorIndex = GPTSimpleVectorIndex(documents=docs,llm_predictor=llmPredictor,prompt_helper=promptHelper) #create vector index

  vectorIndex.save_to_disk(r"vectorIndex.json")
  return vectorIndex

def chatbot(query):
  vIndex = GPTSimpleVectorIndex.load_from_disk("vectorIndex.json")
  response = vIndex.query(query,response_mode="compact")
  return response.response




iface = gr.Interface(fn=chatbot,
                     inputs=gr.inputs.Textbox(lines=7, label="Enter your query"),
                     outputs="text",
                     title="MSM AI Chatbot")

vector_index = create_index("docs")
iface.launch(share=True)