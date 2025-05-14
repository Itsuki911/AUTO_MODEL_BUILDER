import requests
from requests.auth import HTTPBasicAuth

def fetch_github_code(query, max_results=5):
    url = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc"
    response = requests.get(url)
    
    if response.status_code == 200:
        repositories = response.json().get('items', [])
        results = []
        
        for repo in repositories[:max_results]:
            repo_info = {
                'name': repo['name'],
                'url': repo['html_url'],
                'description': repo['description'],
                'stars': repo['stargazers_count'],
                'language': repo['language'],
            }
            results.append(repo_info)
        
        return results
    else:
        print(f"Error fetching data from GitHub: {response.status_code}")
        return None

def main():
    query = input("Enter the search query for GitHub repositories: ")
    results = fetch_github_code(query)
    
    if results:
        for idx, repo in enumerate(results):
            print(f"{idx + 1}. {repo['name']} - {repo['description']} (Stars: {repo['stars']})")
            print(f"   URL: {repo['url']}")
            print(f"   Language: {repo['language']}\n")

if __name__ == "__main__":
    main()