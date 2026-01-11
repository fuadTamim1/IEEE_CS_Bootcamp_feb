"""
FINAL PROJECT: Option 2 - Rule-Based Chatbot
============================================

Project Description:
Create an interactive chatbot that responds to user input based on predefined rules and keywords.

Base Functionality:
- Respond to specific keywords with predefined responses
- Use if/elif/else or dictionary lookup
- Keep chatbot running until user says goodbye
- Make it case-insensitive (treat \"Hello\" and \"hello\" the same)
- Provide a fallback response for unknown inputs

Skills Used:
- String manipulation and comparison
- Conditionals (if/elif/else)
- Loops (while loops)
- Functions for organization
- Dictionaries for data storage
- User input and output

Submission Requirements:
✓ Working Python file
✓ Chat transcript showing it works
✓ 100-200 word explanation of extensions implemented

==============================================

EXTENSIONS (Choose at least 2):

[ ] Variety (Multiple Responses per Keyword)
    Each keyword has multiple possible responses
    Use random.choice() to pick one
    Example: \"Hi\" -> \"Hello!\", \"Hey there!\", \"Greetings!\"

[ ] Fallback Logic
    Intelligent responses when input not recognized
    \"I don't understand that.\"
    \"Could you rephrase that?\"

[ ] External Configuration
    Load keywords/responses from external file (JSON or CSV)
    Makes it easy to update bot without changing code
    Example: keywords.json contains all Q&A pairs

[ ] Conversation Logging
    Save chat history to a file
    Each line: timestamp | user input | bot response
    Useful for analyzing chatbot performance

[ ] Case-Insensitive Matching
    Already in base - but make it more robust
    Handle variations in spacing

[ ] Sentiment Analysis
    Detect if user is happy/sad/neutral
    Respond differently based on sentiment
    \"You seem happy! What's making you smile?\"

[ ] Context Awareness
    Remember previous conversation context
    \"You mentioned Python earlier...\"
    Keep track of conversation history

[ ] Keyword Learning
    Let admin add new Q&A pairs during conversation
    \"admin add: What is Python? -> A programming language\"
    Save new Q&A pairs

[ ] Typo Tolerance
    Handle minor typos using fuzzy matching
    \"helo\" -> similar to \"hello\"
    Use difflib.get_close_matches()

==============================================
"""

import json
import datetime
import random
import os

# ============================================
# BASE DATA - KEYWORDS AND RESPONSES
# ============================================

# TODO: Add more keywords and responses to this dictionary
# Format: "keyword": "response"
KEYWORDS = {
    # Greetings
    "hello": "Hi there! Welcome to the chatbot. How can I help?",
    "hi": "Hello! Nice to see you.",
    "hey": "Hey! What's up?",
    "greetings": "Greetings! How are you today?",
    
    # Farewell
    "bye": "Goodbye! Have a great day!",
    "goodbye": "See you later!",
    "exit": "Thanks for chatting. Bye!",
    "quit": "Exiting chatbot. Goodbye!",
    
    # Help
    "help": "I'm here to help! You can say hello, ask me a question, or type 'help'.",
    "what can you do": "I can chat with you, answer questions, and help with information.",
    "?": "Please ask me a question!",
    
    # Personal questions
    "how are you": "I'm doing great, thanks for asking!",
    "who are you": "I'm a chatbot created for this Python workshop!",
    "what's your name": "I'm a Python Workshop Chatbot!",
    
    # About the workshop
    "python": "Python is a powerful programming language great for AI and automation!",
    "workshop": "You're in the Python Workshop! It's an amazing event learning Python fundamentals.",
    "ai": "AI (Artificial Intelligence) is a fascinating field. We're learning about it!",
    "automation": "Automation helps us save time by automating repetitive tasks.",
    
    # Math
    "what is 2+2": "2 + 2 = 4",
    "what is 5*5": "5 * 5 = 25",
    
    # More to add...
    # TODO: Add more keywords and responses
}

# Fallback responses for unknown inputs
FALLBACK_RESPONSES = [
    "I'm not sure how to respond to that. Can you ask something else?",
    "That's interesting, but I don't have a good answer for that.",
    "Could you rephrase that?",
    "I didn't understand that. Try asking something else!",
    "Sorry, I'm not trained to handle that question yet.",
]

# Goodbye keywords (to exit the chatbot)
GOODBYE_KEYWORDS = ["bye", "goodbye", "exit", "quit", "bye!", "goodbye!"]

# ============================================
# BASE FUNCTIONALITY - IMPLEMENT THESE FIRST
# ============================================

def normalize_input(user_input):
    """
    TODO: Clean up user input for processing.
    
    Steps:
    1. Convert to lowercase
    2. Remove extra spaces
    3. Remove punctuation from edges
    
    Examples:
    - \"  Hello  \" -> \"hello\"
    - \"Hi!\" -> \"hi\"
    - \"  PYTHON  ?  \" -> \"python\"
    
    Args:
        user_input (str): Raw user input
    
    Returns:
        str: Cleaned input
    """
    pass


def find_matching_keyword(user_input, keywords):
    """
    TODO: Find a matching keyword in the keywords dictionary.
    
    Methods to try:
    1. Exact match: \"hello\" in keywords
    2. Substring match: \"hello world\" contains \"hello\"
    3. Word match: Check if any keyword appears as a word
    
    Args:
        user_input (str): Cleaned user input
        keywords (dict): Keywords dictionary
    
    Returns:
        str: Matching keyword, or None if not found
    """
    pass


def get_response(user_input, keywords):
    """
    TODO: Get a response for the user input.
    
    Steps:
    1. Normalize the input
    2. Find matching keyword
    3. Return corresponding response
    4. If no match, return fallback response
    
    Args:
        user_input (str): User's message
        keywords (dict): Keywords dictionary
    
    Returns:
        str: Bot's response
    """
    pass


def is_goodbye(user_input):
    """
    TODO: Check if user is trying to exit the chat.
    
    Args:
        user_input (str): Cleaned user input
    
    Returns:
        bool: True if it's a goodbye message
    """
    pass


def run_chatbot():
    """
    TODO: Main chatbot loop.
    
    Steps:
    1. Display welcome message
    2. Loop until user says goodbye:
       a. Get user input
       b. Check if it's goodbye
       c. Get bot response
       d. Display response
    3. Display goodbye message
    
    """
    pass


# ============================================
# EXTENSION 1: MULTIPLE RESPONSES PER KEYWORD
# ============================================

# TODO (EXTENSION): Update KEYWORDS to have lists of responses
KEYWORDS_WITH_VARIETY = {
    "hello": [
        "Hi there! Welcome to the chatbot.",
        "Hello! Nice to see you.",
        "Greetings! How can I help?",
        "Hey! What's on your mind?"
    ],
    "how are you": [
        "I'm doing great, thanks for asking!",
        "Doing well! How about you?",
        "I'm fantastic! How are you?",
    ],
    # More keywords...
}

def get_response_with_variety(user_input):
    """
    TODO (EXTENSION): Get a random response for variety.
    
    Instead of always same response, pick randomly from list.
    
    Args:
        user_input (str): User's message
    
    Returns:
        str: Random response for this keyword
    """
    pass


# ============================================
# EXTENSION 2: EXTERNAL CONFIGURATION
# ============================================

def load_keywords_from_file(filename):
    """
    TODO (EXTENSION): Load keywords from JSON file.
    
    JSON format:
    {
        \"keywords\": {
            \"hello\": \"Hi there!\",
            \"bye\": \"Goodbye!\"
        },
        \"fallback\": [
            \"I don't understand\",
            \"Can you rephrase?\"
        ]
    }
    
    Args:
        filename (str): Path to JSON file
    
    Returns:
        dict: Keywords from file, or default if file not found
    """
    pass


def create_sample_keywords_file():
    """
    TODO (EXTENSION): Create a sample keywords.json file.
    
    Useful for testing external loading.
    """
    pass


# ============================================
# EXTENSION 3: CONVERSATION LOGGING
# ============================================

def log_conversation(user_input, bot_response):
    """
    TODO (EXTENSION): Log conversation to file.
    
    Format: [timestamp] User: input | Bot: response
    
    Args:
        user_input (str): What user said
        bot_response (str): What bot said
    """
    pass


def read_conversation_log(filename="chatbot_log.txt"):
    """
    TODO (EXTENSION): Read and display previous conversations.
    
    Args:
        filename (str): Path to log file
    
    Returns:
        str: Formatted conversation history
    """
    pass


# ============================================
# EXTENSION 4: SENTIMENT ANALYSIS
# ============================================

def analyze_sentiment(user_input):
    """
    TODO (EXTENSION): Determine sentiment of user input.
    
    Simple approach:
    - Happy keywords: good, great, awesome, excellent, love, happy, :), :D
    - Sad keywords: bad, terrible, hate, sad, :(, D:
    - Neutral: everything else
    
    Args:
        user_input (str): User's message
    
    Returns:
        str: 'positive', 'negative', or 'neutral'
    """
    pass


def respond_based_on_sentiment(sentiment):
    """
    TODO (EXTENSION): Choose response based on sentiment.
    
    Args:
        sentiment (str): Result from analyze_sentiment()
    
    Returns:
        str: Appropriate response
    """
    pass


# ============================================
# EXTENSION 5: FUZZY MATCHING (Typo Tolerance)
# ============================================

def find_similar_keyword(user_input, keywords, threshold=0.6):
    """
    TODO (EXTENSION): Find similar keywords using fuzzy matching.
    
    Use difflib.get_close_matches()
    
    Examples:
    - \"helo\" might match \"hello\"
    - \"pyton\" might match \"python\"
    
    Args:
        user_input (str): User's input with possible typo
        keywords (dict): Keywords dictionary
        threshold (float): Minimum similarity score (0-1)
    
    Returns:
        str: Best matching keyword, or None
    """
    pass


# ============================================
# TESTING
# ============================================

def test_chatbot():
    """
    Test the chatbot with predefined inputs.
    Useful for development without interactive mode.
    """
    
    test_inputs = [
        "hello",
        "Hi",
        "HELLO",
        "how are you",
        "python",
        "unknown phrase",
        "bye",
    ]
    
    print("Running chatbot tests...\n")
    
    for user_input in test_inputs:
        # TODO: Call your get_response function
        # response = get_response(user_input, KEYWORDS)
        response = f"[TODO: Implement get_response] - User said: {user_input}"
        print(f"User:  {user_input}")
        print(f"Bot:   {response}")
        print()


# ============================================
# MAIN PROGRAM
# ============================================

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════╗
║       RULE-BASED CHATBOT - STARTER CODE       ║
║                                                ║
║ Follow the TODO comments to implement the      ║
║ required functions. Then add your chosen       ║
║ extensions from the list above.                ║
║                                                ║
║ Steps:                                         ║
║ 1. Implement base functions (marked TODO)      ║
║ 2. Test with test_chatbot()                    ║
║ 3. Add more keywords to KEYWORDS dictionary    ║
║ 4. Add at least 2 extensions                   ║
║ 5. Run interactive mode                        ║
╚════════════════════════════════════════════════╝
    """)
    
    # Option 1: Test mode (faster for development)
    print("RUNNING IN TEST MODE\n")
    test_chatbot()
    
    # Option 2: Interactive mode (uncomment to use)
    # print("\\nRUNNING IN INTERACTIVE MODE\\n")
    # run_chatbot()
    
    print("\n📝 Next Steps:")
    print("1. Implement all TODO functions")
    print("2. Add more keywords to the KEYWORDS dictionary")
    print("3. Test with test_chatbot()")
    print("4. Switch to interactive mode (run_chatbot())")
    print("5. Add at least 2 extensions")
    print("\n💡 Tips:")
    print("- Start with simple keyword matching")
    print("- Test each function individually")
    print("- Use print() statements to debug")
    print("- Keep responses natural and helpful")
    print("- Add more keywords to make it useful")
