# summary3.py

import nltk
import heapq
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

class TextSummarizer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.text = self.load_text()
        self.sentences = sent_tokenize(self.text)
        self.word_frequencies = self.calculate_word_frequencies()
        self.tfidf_scores = self.calculate_tfidf()
        self.summary_length = 5  # Can be adjusted

    def load_text(self):
        with open(self.filepath, 'r') as file:
            return file.read()

    def preprocess(self, text):
        text = text.lower()
        tokens = nltk.word_tokenize(text)
        tokens = [word for word in tokens if word.isalpha()]
        tokens = [word for word in tokens if word not in stopwords.words('english')]
        return tokens

    def calculate_word_frequencies(self):
        tokens = self.preprocess(self.text)
        frequencies = defaultdict(int)
        for word in tokens:
            frequencies[word] += 1
        return frequencies

    def calculate_tfidf(self):
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(self.sentences)
        return np.array(tfidf_matrix.sum(axis=0)).flatten()

    def score_sentences(self, vectorizer):
        sentence_scores = defaultdict(float)
        for sentence in self.sentences:
            for word in nltk.word_tokenize(sentence):
                if word in self.word_frequencies:
                    word_index = vectorizer.vocabulary_.get(word.lower(), None)
                    if word_index is not None:
                        sentence_scores[sentence] += self.word_frequencies[word] * self.tfidf_scores[word_index]
        return sentence_scores

    def generate_summary(self):
        vectorizer = TfidfVectorizer(stop_words='english')
        vectorizer.fit_transform(self.sentences)
        sentence_scores = self.score_sentences(vectorizer)
        summary_sentences = heapq.nlargest(self.summary_length, sentence_scores, key=sentence_scores.get)
        return ' '.join(summary_sentences)

    def extract_named_entities(self):
        tokens = nltk.word_tokenize(self.text)
        tagged = pos_tag(tokens)
        named_entities = ne_chunk(tagged)
        return named_entities

# Usage
summarizer = TextSummarizer('pam.txt')
summary = summarizer.generate_summary()
named_entities = summarizer.extract_named_entities()

print("Summary:")
print(summary)
print("\nNamed Entities:")
for ne in named_entities:
    if hasattr(ne, 'label'):
        print(ne)
