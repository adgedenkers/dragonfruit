import sys
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import nltk

nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Create a plaintext parser
    parser = PlaintextParser.from_string(content, Tokenizer('english'))
    
    # Summarize the content using LSA Summarizer
    summarizer = Summarizer()
    summary = ' '.join([str(sentence) for sentence in summarizer(parser.document, 5)]) # Summarize to 5 sentences

    return summary

def extract_keywords(content):
    # Tokenize and remove stop words
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(content)
    filtered_words = [word for word in words if word not in stop_words and word.isalnum()]

    # Calculate frequency distribution
    freq_dist = FreqDist(filtered_words)
    keywords = freq_dist.most_common(10)  # Get top 10 keywords

    return keywords

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    # Summarize the text
    summary = summarize_text(file_path)
    print("Summary:\n", summary)

    # Extract keywords
    keywords = extract_keywords(summary)
    print("\nKeywords and Scores:")
    for keyword, score in keywords:
        print(f"{keyword}: {score}")

if __name__ == "__main__":
    main()