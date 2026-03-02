from schemas import *
import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from crewai.tools import tool
from tavily import TavilyClient
from scrapegraph_py import Client

load_dotenv()

basic_llm = LLM(
    model="openrouter/arcee-ai/trinity-large-preview:free",  # or any model on openrouter
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"), 
    temperature=0
    )


search_queries_recommendation_agent = Agent(
    role="Search Queries Recommendation Agent",
    goal="\n".join([
                "To provide a list of suggested search queries to be passed to the search engine.",
                "The queries must be varied and looking for specific items."
            ]),
    backstory="The agent is designed to help in looking for products by providing a list of suggested search queries to be passed to the search engine based on the context provided.",
    llm=basic_llm,
    verbose=True,
)


search_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search_engine_tool(query: str):
    """Useful for search-based queries. Use this to find current information about any query related pages using a search engine"""
    return search_client.search(query)

search_engine_agent = Agent(
    role="Search Engine Agent",
    goal="To search for products based on the suggested search query",
    backstory="The agent is designed to help in looking for products by searching for products based on the suggested search queries.",
    llm=basic_llm,
    verbose=True,
    tools=[search_engine_tool]
)


scrape_client = Client(api_key=os.getenv("SCRAPER_API_KEY"))

@tool
def web_scraping_tool(page_url: str):
    """
    An AI Tool to help an agent to scrape a web page

    Example:
    web_scraping_tool(
        page_url="https://www.noon.com/egypt-en/15-bar-fully-automatic-espresso-machine-1-8-l-1500"
    )
    """
    details = scrape_client.smartscraper(
        website_url=page_url,
        user_prompt="Extract ```json\n" + SingleExtractedProduct.schema_json() + "```\n From the web page"
    )

    return {
        "page_url": page_url,
        "details": details
    }

scraping_agent = Agent(
    role="Web scraping agent",
    goal="To extract details from any website",
    backstory="The agent is designed to help in looking for required values from any website url. These details will be used to decide which best product to buy.",
    llm=basic_llm,
    tools=[web_scraping_tool],
    verbose=True,
)



procurement_report_author_agent = Agent(
    role="Procurement Report Author Agent",
    goal="To generate a professional HTML page for the procurement report",
    backstory="The agent is designed to assist in generating a professional HTML page for the procurement report after looking into a list of products.",
    llm=basic_llm,
    verbose=True,
)


