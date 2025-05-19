from langchain_community.utilities import SerpAPIWrapper
from dotenv import load_dotenv

load_dotenv()

search = SerpAPIWrapper()

def search_web(query: str) -> str:
    return search.run(query)