from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource
import agentops
from agents import *
from tasks import *
import os
import json
from dotenv import load_dotenv
load_dotenv()

agentops.init(
    api_key=os.getenv("AGENTOPS_API_KEY")
)


about_company = "Rankyx is a company that provides AI solutions to help websites refine their search and recommendation systems."

company_context = StringKnowledgeSource(
    content=about_company
)

rankyx_crew = Crew(
    agents=[search_queries_recommendation_agent, search_engine_agent, scraping_agent, procurement_report_author_agent],
    tasks=[search_queries_recommendation_task, search_engine_task, scraping_task, procurement_report_author_task],
    process=Process.sequential,
    knowledge_sources=[company_context],
    embedder={
        "provider": "huggingface",
        "config": {
            "model": "sentence-transformers/all-MiniLM-L6-v2"
        }
    }
)

rankyx_crew.kickoff(
    inputs = {
         "product_name": "coffee machine for the office",
        "websites_list": ["www.amazon.eg", "www.jumia.com.eg", "www.noon.com/egypt-en"],
        "country_name": "Egypt",
        "no_keywords": 10,
        "language": "English",
         "score_th": 0.10,
         "top_recommendations_no": 10
    }
)

agentops.end_session("Success")
