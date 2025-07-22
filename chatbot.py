# Pattern Matching Chatbot using Regular Expressions
import re
import random
import time

# Pattern-response pairs
patterns = {
    
    r"\bhi\b|\bhello\b|\bhey\b": ["Hey there!", "Hello!", "Hi, how can I help you today?"],
    r"how are you": ["I'm doing well, thanks for asking!", "Running smooth as code! What about you?"],
    r"what(')?s your name|who are you": ["I'm CodeBot, your friendly assistant!"],
    r"help": ["Sure! Ask me anything or type 'joke' for a laugh."],
    r"joke": [
        "Why don't robots get tired? Because they recharge!",
        "Debugging: Being the detective in a crime movie where you're also the murderer.",
        "Why did the AI break up with the human? It found them too unpredictable."
    ],
    r"thank you|thanks": ["You're welcome!", "Glad I could help!"],
    r"language|languages|speak|do you know .* language": [
        "I understand English and a bit of Python 😄",
        "Right now, I speak only English. But I’d love to learn more!",
        "I was coded in Python, so that’s my favorite language!",
        "I can help you learn programming languages like Python or Java."
    ],
    r"\bbye\b|\bexit\b|\bquit\b": ["Goodbye!", "See you later!", "Have a great day!"]
}


# Function to match input with patterns
def match_response(user_input):
    for pattern, responses in patterns.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses)
    return "Sorry, I didn't quite get that. Try asking something else!"

# Chat function
def chat():
    print("CodeBot 🤖: Hello! I’m your chatbot. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if re.search(r"\b(exit|quit|bye)\b", user_input, re.IGNORECASE):
            print("CodeBot 🤖:", match_response(user_input))
            break
        response = match_response(user_input)
        time.sleep(0.5)
        print("CodeBot 🤖:", response)

# Run chatbot
if __name__ == "__main__":
    chat()
Add initial chatbot code
