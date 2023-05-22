# This code is to find similarity between input text and all the pre-processed
# product details and display list of top 10 similar items with title, links, price and rating

import json
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the data from data.json
with open('data.json', 'r') as file:
    data = json.load(file)

# Preprocess the titles
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Remove special characters and numbers
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    # Tokenize the text
    tokens = word_tokenize(text)
    # Convert to lowercase and remove stop words
    tokens = [token.lower() for token in tokens if token.lower() not in stop_words]
    # Lemmatize the tokens
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    # Join the tokens back into a string
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text

preprocessed_titles = [preprocess_text(item['title']) for item in data]

# Calculate similarity
def calculate_similarity(input_text, preprocessed_titles):
    # Preprocess the input text
    preprocessed_input = preprocess_text(input_text)

    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit the vectorizer on the preprocessed titles
    vectorizer.fit(preprocessed_titles)

    # Transform the input text and preprocessed titles into TF-IDF vectors
    input_vector = vectorizer.transform([preprocessed_input])
    titles_vectors = vectorizer.transform(preprocessed_titles)

    # Compute the cosine similarity between the input vector and the titles vectors
    similarities = cosine_similarity(input_vector, titles_vectors)

    return similarities.flatten()

# Function to find similarities and return ranked list
def find_similar_items(payload):
    # Parse the JSON payload to extract the input text
    input_text = payload['text']

    # Calculate the similarity scores
    similarities = calculate_similarity(input_text, preprocessed_titles)

    # Create a ranked list of similar items with their links
    ranked_items = [(data[i]['title'], data[i]['link'], data[i]['rating'], data[i]['price'], similarities[i]) for i in range(len(data))]
    ranked_items.sort(key=lambda x: x[4], reverse=True)

    # Create the JSON response
    response = []
    for item in ranked_items[:10]:
        response.append({
            'title': item[0],
            'link': item[1],
            'rating': item[2],
            'price': item[3],
            'similarity': item[4]
        })

    return response

# input query
input_payload = {
    'text': 'v neck men t-shirt with cotton printed' 
}

result = find_similar_items(input_payload)
json_reply = json.dumps(result, indent=4)

print(json.dumps(result, indent=4))

# Writing to result.json
with open("result.json", "w") as outfile:
    outfile.write(json_reply)
