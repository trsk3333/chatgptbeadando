from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from rag import retrieve_from_vectorstore
from web_search import search_web
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")

tools = [
    Tool.from_function(func=retrieve_from_vectorstore, name="RAG Tool", description="Use it when the question is about the making of electric guitars, or the evolution of guitars in general."),
    Tool.from_function(func=search_web, name="Web Search Tool", description="Use it when you need current information, weather updates, or to answer general questions.")
]

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", memory=memory, handle_parsing_errors=True, verbose=True)

def run_agent(question: str) -> str:
    return agent.run(question)