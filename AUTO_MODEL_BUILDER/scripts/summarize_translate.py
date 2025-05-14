from transformers import pipeline

def summarize_and_translate(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ja")
    translated_summary = translator(summary[0]['summary_text'])
    return translated_summary[0]['translation_text']