import os
from langsmith import traceable
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

# Initialize LLM 
llm = ChatOllama(
    model=os.getenv("OLLAMA_GEN_MODEL"),
    temperature=0.0
)

# Format Prompt
@traceable
def format_prompt(subject: str):
    return [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=f"Explain {subject} in simple terms.")
    ]


# Invoke LLM
@traceable(run_type="llm")
def invoke_llm(messages):
    response = llm.invoke(messages)
    return response


# Parse Output
@traceable
def parse_output(response):
    return response.content


# Full Pipeline
@traceable
def run_pipeline():
    messages = format_prompt("DevOps")
    response = invoke_llm(messages)
    return parse_output(response)


# ▶ Run
if __name__ == "__main__":
    output = run_pipeline()
    print(output)
