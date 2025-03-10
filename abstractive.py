from transformers import pipeline

# Load the pre-trained summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def abstractive_summary(text, max_length=100, min_length=30):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

# Test the function
if __name__ == "__main__":
    sample_text = """Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to human or animal intelligence.
    It is a branch of computer science that deals with the simulation of human intelligence. AI applications include natural language 
    processing, speech recognition, and machine vision."""
    
    print("Abstractive Summary:\n", abstractive_summary(sample_text))
