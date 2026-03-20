# 🛒 AI Procurement Agent

An autonomous multi-agent system that automates the product research and procurement reporting process using **CrewAI**, **LLMs**, **web search**, and **AI-powered scraping**.

---

## 📌 Overview

The AI Procurement Agent eliminates manual product research by orchestrating a pipeline of specialized AI agents that:

1. Generate smart search queries for a target product
2. Search the web across e-commerce platforms
3. Scrape and extract structured product details
4. Produce a professional HTML procurement report

---

## 🏗️ Architecture

```
User Input (product, websites, country)
        │
        ▼
┌─────────────────────────────────────────────┐
│              CrewAI Orchestrator             │
│          (Sequential Agent Pipeline)         │
└─────────────────────────────────────────────┘
        │
        ├──► 1. Search Queries Recommendation Agent
        │         └─ Generates targeted search queries
        │
        ├──► 2. Search Engine Agent  [Tavily API]
        │         └─ Searches across e-commerce sites
        │
        ├──► 3. Web Scraping Agent  [ScrapeGraph AI]
        │         └─ Extracts structured product data
        │
        └──► 4. Procurement Report Author Agent
                  └─ Generates Bootstrap HTML report
```

---

## 🤖 Agents

| Agent | Role | Tool |
|---|---|---|
| **Search Queries Recommendation Agent** | Generates brand/type-specific search queries | LLM reasoning |
| **Search Engine Agent** | Searches e-commerce sites for products | Tavily Search API |
| **Web Scraping Agent** | Extracts product specs, prices, discounts | ScrapeGraph AI |
| **Procurement Report Author Agent** | Writes structured HTML procurement report | LLM + Bootstrap |

---

## 📂 Project Structure

```
├── main.py            # Crew setup and kickoff
├── agents.py          # Agent definitions and tools
├── tasks.py           # Task definitions and output schemas
├── schemas.py         # Pydantic models for structured output
├── requirements.txt   # Python dependencies
├── Dockerfile         # Container setup
├── deploy.yml         # GitHub Actions CI/CD pipeline
└── ai-agent-output/   # Generated output files (auto-created)
    ├── step_1_suggested_search_queries.json
    ├── step_2_search_results.json
    ├── step_3_search_results.json
    └── step_4_procurement_report.html
```

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.10+
- API keys for: OpenRouter, Tavily, ScrapeGraph AI, AgentOps

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-procurement-agent.git
cd ai-procurement-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the root directory:

```env
OPENROUTER_API_KEY=your_openrouter_key
TAVILY_API_KEY=your_tavily_key
SCRAPER_API_KEY=your_scrapegraph_key
AGENTOPS_API_KEY=your_agentops_key
```

### 4. Run the agent

```bash
python main.py
```

---

## 🐳 Docker

### Build & Run

```bash
docker build -t ai-procurement-agent .
docker run --env-file .env ai-procurement-agent
```

---

## 🚀 CI/CD

The project includes a GitHub Actions workflow (`deploy.yml`) that automatically builds the Docker image on every push to `master`.

---

## 🔧 Configuration

Customize the agent run by editing the `inputs` in `main.py`:

```python
rankyx_crew.kickoff(
    inputs={
        "product_name": "coffee machine for the office",
        "websites_list": ["www.amazon.eg", "www.jumia.com.eg", "www.noon.com/egypt-en"],
        "country_name": "Egypt",
        "no_keywords": 10,
        "language": "English",
        "score_th": 0.10,
        "top_recommendations_no": 10
    }
)
```

| Parameter | Description |
|---|---|
| `product_name` | Product to search for |
| `websites_list` | Target e-commerce sites |
| `country_name` | Target market |
| `no_keywords` | Max search queries to generate |
| `language` | Language for search queries |
| `score_th` | Minimum relevance score (0–1) for search results |
| `top_recommendations_no` | Max products to scrape and compare |

---

## 📊 Output

The agent produces a **professional Bootstrap HTML report** (`step_4_procurement_report.html`) including:

- Executive Summary
- Price comparison tables
- Product specs and discount analysis
- Ranked recommendations
- Conclusion and appendices

---

## 🧰 Tech Stack

| Category | Technology |
|---|---|
| Agent Framework | [CrewAI](https://crewai.com) |
| LLM Provider | [OpenRouter](https://openrouter.ai) (Arcee Trinity / any model) |
| Web Search | [Tavily API](https://tavily.com) |
| Web Scraping | [ScrapeGraph AI](https://scrapegraph.ai) |
| Data Validation | [Pydantic v2](https://docs.pydantic.dev) |
| Observability | [AgentOps](https://agentops.ai) |
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` |
| Containerization | Docker |
| CI/CD | GitHub Actions |

---

## 📝 License

MIT License — feel free to use, modify, and distribute.
