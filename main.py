import extractive
import abstractive

def main():
    print("Welcome to AI-Powered Notes Summarizer!\n")
    text = input("Enter your text to summarize: ")
    
    print("\nChoose summarization type:")
    print("1. Extractive Summarization (NLTK)")
    print("2. Abstractive Summarization (Transformer)")
    
    choice = input("Enter choice (1/2): ")
    
    if choice == '1':
        summary = extractive.extractive_summary(text, num_sentences=3)
        print("\nExtractive Summary:\n", summary)
    elif choice == '2':
        summary = abstractive.abstractive_summary(text)
        print("\nAbstractive Summary:\n", summary)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
