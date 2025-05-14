import requests

def fetch_research_papers(task):
    arxiv_url = "http://export.arxiv.org/api/query?"
    search_query = f"search_query=all:{task}&start=0&max_results=5"
    response = requests.get(arxiv_url + search_query)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception("Error fetching papers from arXiv")

def fetch_semantic_scholar_papers(task):
    semantic_scholar_url = "https://api.semanticscholar.org/v1/paper/search"
    params = {'query': task, 'limit': 5}
    response = requests.get(semantic_scholar_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching papers from Semantic Scholar")