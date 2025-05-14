import requests

def search_hugging_face_models(task):
    url = "https://huggingface.co/api/models"
    params = {
        "search": task,
        "sort": "downloads",
        "direction": -1
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        models = response.json()
        return models
    else:
        raise Exception("Failed to fetch models from Hugging Face Hub")

def suggest_base_model(task):
    try:
        models = search_hugging_face_models(task)
        if models:
            # Return the top 5 models as suggestions
            return models[:5]
        else:
            return "No models found for the specified task."
    except Exception as e:
        return str(e)