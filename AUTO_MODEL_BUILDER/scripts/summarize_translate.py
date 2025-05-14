from transformers import pipeline

def summarize_and_translate(papers):
    """
    Summarize and translate a list of research papers.

    Args:
        papers (list): A list of dictionaries containing paper titles and links.

    Returns:
        list: A list of dictionaries containing the original title, link, summary, and translated summary.

    Raises:
        Exception: If summarization or translation fails.
    """
    try:
        # Initialize the summarization and translation pipelines
        summarizer = pipeline("summarization")
        translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ja")

        results = []
        for paper in papers:
            try:
                # Summarize the paper title (or content if available)
                summary = summarizer(paper['title'], max_length=130, min_length=30, do_sample=False)
                summary_text = summary[0]['summary_text']

                # Translate the summary to Japanese
                translated_summary = translator(summary_text)
                translated_text = translated_summary[0]['translation_text']

                # Append the result
                results.append({
                    "title": paper['title'],
                    "link": paper['link'],
                    "summary": summary_text,
                    "translated_summary": translated_text
                })
            except Exception as e:
                # Handle errors for individual papers
                results.append({
                    "title": paper['title'],
                    "link": paper['link'],
                    "summary": "Error summarizing this paper.",
                    "translated_summary": f"Error translating this paper: {str(e)}"
                })

        return results
    except Exception as e:
        raise Exception(f"An error occurred during summarization and translation: {str(e)}")