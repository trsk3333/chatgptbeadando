from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from rag import retrieve_from_vectorstore
from web_search import search_web
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")

tools = [
    Tool.from_function(func=retrieve_from_vectorstore, name="RAG Tool", description="Retrieves from vector DB"),
    Tool.from_function(func=search_web, name="Web Search Tool", description="Performs web search using SerpAPI")
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

def run_agent(question: str) -> str:
    return agent.run(question)