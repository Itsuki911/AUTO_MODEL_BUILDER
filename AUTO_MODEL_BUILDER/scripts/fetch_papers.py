import requests
import html

def generate_keywords(task):
    """
    Generate a list of keywords based on the task description.
    """
    # Example: Simple keyword generation logic
    keywords = task.split()
    return keywords

def fetch_research_papers(task, max_results=5):
    """
    Fetch research papers from arXiv based on the task and generated keywords.

    Args:
        task (str): The task description to generate keywords for.
        max_results (int): The maximum number of results to fetch.

    Returns:
        list: A list of dictionaries containing paper titles and links.

    Raises:
        Exception: If there is an error fetching papers from arXiv.
    """
    arxiv_url = "http://export.arxiv.org/api/query?"
    keywords = generate_keywords(task)
    search_query = "+OR+".join([f"all:{keyword}" for keyword in keywords])
    query = f"search_query={search_query}&start=0&max_results={max_results}"

    try:
        response = requests.get(arxiv_url + query, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching papers from arXiv: {e}")

    if response.status_code == 200:
        # Parse the response to extract paper titles and links
        papers = []
        entries = response.text.split("<entry>")
        for entry in entries[1:]:  # Skip the first split part (not an entry)
            # Extract the title
            title_start = entry.find("<title>") + len("<title>")
            title_end = entry.find("</title>")
            title = html.unescape(entry[title_start:title_end].strip())

            # Extract the link
            link_start = entry.find("<id>") + len("<id>")
            link_end = entry.find("</id>")
            link = html.unescape(entry[link_start:link_end].strip())

            papers.append({"title": title, "link": link})
        return papers
    else:
        raise Exception(f"Error fetching papers from arXiv: {response.status_code}, {response.text}")