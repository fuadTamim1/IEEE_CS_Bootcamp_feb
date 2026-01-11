"""
WEEK 1 FINAL PROJECT - OPTION 2: Rule-Based Chatbot
====================================================

Base Functionality:
- Respond to predefined keywords

Extensions (choose at least 2):
✓ Multiple responses per keyword (random)
✓ Fallback response for unknown inputs
✓ Load responses from JSON file
✓ Save conversation history
✓ Case-insensitive matching
✓ Personality style

Starter Code - Build upon this!
"""

import json
import random

# Knowledge base - extend this!
RESPONSES = {
    "hello": [
        "Hi there! 👋 How can I help?",
        "Hey! What can I do for you?",
        "Greetings! 🎉"
    ],
    "how are you": [
        "I'm doing great! Thanks for asking!",
        "Excellent! Ready to help!"
    ],
    "help": [
        "I can help with:\n- Greetings (say 'hello')\n- Status (say 'how are you')\n- Exit (say 'bye')",
        "What do you need help with?"
    ],
    "bye": [
        "Goodbye! 👋",
        "See you later!",
        "Thanks for chatting!"
    ]
}

FALLBACK_RESPONSES = [
    "I'm not sure about that. Could you rephrase?",
    "Interesting! I'm still learning. Try: hello, how are you, help, bye",
    "Hmm, I didn't catch that. Try asking something else!"
]


def get_response(user_input):
    """
    Get a response based on user input.
    
    Args:
        user_input: String from user
    
    Returns:
        String response from chatbot
    """
    
    # Normalize input
    user_input = user_input.lower().strip()
    
    # Check for keyword match
    for keyword, responses in RESPONSES.items():
        if keyword in user_input:
            return random.choice(responses)
    
    # Return fallback
    return random.choice(FALLBACK_RESPONSES)


def chatbot():
    """Run the chatbot."""
    
    print("🤖 Welcome to the Chatbot!")
    print("Type 'help' for options or 'bye' to exit\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
        
        if user_input.lower() == "bye":
            response = get_response(user_input)
            print(f"Bot: {response}")
            break
        
        response = get_response(user_input)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    chatbot()


# NEXT STEPS TO EXTEND THIS PROJECT:
# 1. Load responses from a JSON config file
# 2. Add conversation history saving
# 3. Add more keywords and responses
# 4. Add personality traits
# 5. Improve keyword matching logic
# 6. Add user name tracking
# 7. Add sentiment analysis
