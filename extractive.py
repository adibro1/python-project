import nltk
import heapq
import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# Download NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

def extractive_summary(text, num_sentences=3):
    # Step 1: Clean the text
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    sentences = sent_tokenize(text)
    
    # Step 2: Word frequency analysis
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))
    
    word_frequencies = {}
    for word in words:
        if word not in stop_words and word.isalnum():
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    # Step 3: Score sentences based on word frequency
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

    # Step 4: Extract top sentences
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    summary = ' '.join(summary_sentences)
    
    return summary

# Test the function
if __name__ == "__main__":
    sample_text = """Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to human or animal intelligence.
    It is a branch of computer science that deals with the simulation of human intelligence. AI applications include natural language 
    processing, speech recognition, and machine vision."""
    
    print("Extractive Summary:\n", extractive_summary(sample_text, 2))
