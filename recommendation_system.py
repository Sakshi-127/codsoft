from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset (can be movies, books, or products)
items = [
    {"title": "The Matrix", "desc": "A hacker discovers the reality is a simulation."},
    {"title": "Inception", "desc": "A thief steals information by entering dreams."},
    {"title": "Interstellar", "desc": "A team travels through a wormhole to save Earth."},
    {"title": "The Social Network", "desc": "Story of the creation of Facebook."},
    {"title": "The Imitation Game", "desc": "A mathematician cracks the Nazi code during WWII."}
]

# Extract descriptions
descriptions = [item["desc"] for item in items]

# Vectorize text using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(descriptions)

# Compute cosine similarity between items
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend(title, top_n=3):
    # Find item index
    idx = next((i for i, item in enumerate(items) if item["title"].lower() == title.lower()), None)
    if idx is None:
        return f"Item '{title}' not found in the database."

    # Get similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    # Print recommendations
    print(f"\n🧠 Because you liked *{items[idx]['title']}*, you might also like:")
    for i, score in sim_scores:
        print(f"- {items[i]['title']} (Score: {round(score, 2)})")

# Example use
if __name__ == "__main__":
    print("🎬 Available titles:")
    for item in items:
        print("-", item["title"])
    
    choice = input("\nEnter a title to get recommendations: ")
    recommend(choice)
