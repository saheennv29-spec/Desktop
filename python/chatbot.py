import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi! Welcome to our customer service.",
    "order": "Please provide your order ID for tracking.",
    "refund": "Refunds are usually processed within 5-7 business days.",
    "delivery": "Your order will typically arrive within 3-5 business days.",
    "payment": "We accept UPI, Debit Card, Credit Card, and Net Banking.",
    "contact": "You can contact us at support@example.com.",
    "bye": "Thank you for contacting us. Have a great day!"
}
print("=== Customer Service Chatbot ===")
print("Type 'bye' to exit.\n")
while True:
    user_input = input("You: ").lower()
    tokens = word_tokenize(user_input)
    found = False
    for word in tokens:
        if word in responses:
            print("Bot:", responses[word])
            found = True
            break

    if user_input == "bye":
        print("Bot:", responses["bye"])
        break

    if not found:
        print("Bot: Sorry, I couldn't understand your query.")