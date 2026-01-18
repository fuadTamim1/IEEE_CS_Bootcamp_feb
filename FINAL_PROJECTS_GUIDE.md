# Final Projects Guide
## Smart File Organizer & Rule-Based Chatbot

---

## 📋 Overview

This guide provides complete specifications, examples, evaluation criteria, and starter code for both final project options.

**Submission Deadline**: End of Workshop Week  
**Required Deliverables**: Python file, output/demo, README documentation

---

## 🎯 Project Objectives

Both projects aim to:
- Apply Python fundamentals learned in Day 1
- Implement file handling and data structures from Day 2
- Demonstrate problem-solving and engineering thinking
- Create a functional, user-friendly program
- Write clean, documented code

---

# Option 1: Smart File Organizer

## 📖 Project Description

Create an automated file organization system that sorts files in a directory based on their extensions and other criteria.

**Real-World Application**: 
- Organize cluttered Downloads folder
- Maintain project directory structure
- Automate file management workflows
- System administration tasks

---

## ✅ Base Requirements

### Minimum Viable Product (MVP)

Your file organizer MUST include:

1. **File Extension Detection**
   - Identify file types by extension (.jpg, .pdf, .txt, etc.)

2. **Category-Based Organization**
   - At least 3 categories (e.g., Images, Documents, Media)
   - Each category has multiple extensions

3. **Dynamic Folder Creation**
   - Create category folders if they don't exist
   - Handle folder naming properly

4. **Safe File Moving**
   - Move files to appropriate folders
   - Don't overwrite existing files
   - Handle errors gracefully

5. **User Interface**
   - Clear prompts and feedback
   - Show what files are being moved
   - Display summary at the end

---

## 🌟 Extension Options (Choose 2+)

### 1. Time-Based Sorting
**Difficulty**: ⭐⭐

Sort files by creation or modification date into year/month folders.

**Example Structure**:
```
Documents/
├── 2025/
│   ├── January/
│   └── February/
└── 2026/
    ├── January/
    └── February/
```

**Implementation Hints**:
```python
import os
from datetime import datetime

modified_time = os.path.getmtime(filepath)
date = datetime.fromtimestamp(modified_time)
year = date.strftime("%Y")
month = date.strftime("%B")
```

---

### 2. Auto-Renaming
**Difficulty**: ⭐⭐⭐

Rename files to a standard format automatically.

**Example Formats**:
- `doc_001.txt`, `doc_002.txt`, `doc_003.txt`
- `image_2026_01_18.jpg`
- `file_prefix_timestamp.ext`

**Implementation Hints**:
```python
import os
from datetime import datetime

def rename_file(original_path, category):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    name, ext = os.path.splitext(original_path)
    new_name = f"{category}_{timestamp}{ext}"
    return new_name
```

---

### 3. Duplicate Detection
**Difficulty**: ⭐⭐⭐⭐

Detect and handle duplicate files (same name or content).

**Features**:
- Check if file already exists in destination
- Option to skip, rename, or replace duplicates
- Compare file contents (advanced)

**Implementation Hints**:
```python
import os
import hashlib

def get_file_hash(filepath):
    """Get MD5 hash of file content"""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def handle_duplicate(source, destination):
    if os.path.exists(destination):
        # Option 1: Rename with number
        base, ext = os.path.splitext(destination)
        counter = 1
        while os.path.exists(f"{base}_{counter}{ext}"):
            counter += 1
        return f"{base}_{counter}{ext}"
    return destination
```

---

### 4. System File Filtering
**Difficulty**: ⭐⭐

Ignore system and hidden files during organization.

**Files to Ignore**:
- `.DS_Store` (macOS)
- `Thumbs.db` (Windows)
- `.git/` folders
- Hidden files (starting with `.`)

**Implementation Hints**:
```python
def should_ignore(filename):
    """Check if file should be ignored"""
    ignored_files = ['.DS_Store', 'Thumbs.db', 'desktop.ini']
    
    if filename.startswith('.'):
        return True
    
    if filename in ignored_files:
        return True
    
    return False
```

---

### 5. Execution Report
**Difficulty**: ⭐⭐

Generate a detailed report of the organization process.

**Report Should Include**:
- Total files processed
- Files moved per category
- Errors encountered
- Timestamp
- Duration

**Implementation Hints**:
```python
import time
from datetime import datetime

def generate_report(stats):
    report = f"""
{'=' * 50}
FILE ORGANIZATION REPORT
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
{'=' * 50}

Total Files Processed: {stats['total']}
Files Moved: {stats['moved']}
Files Skipped: {stats['skipped']}
Errors: {stats['errors']}

Breakdown by Category:
"""
    for category, count in stats['categories'].items():
        report += f"  {category}: {count} files\n"
    
    report += f"\nExecution Time: {stats['duration']:.2f} seconds\n"
    report += "=" * 50
    
    # Save to file
    with open("organization_report.txt", "w") as f:
        f.write(report)
    
    return report
```

---

### 6. Performance Metrics
**Difficulty**: ⭐⭐

Measure and display execution time and efficiency.

**Metrics to Track**:
- Total execution time
- Files processed per second
- Memory usage (advanced)
- Comparison: manual vs automated time saved

**Implementation Hints**:
```python
import time

start_time = time.time()

# ... your organization code ...

end_time = time.time()
duration = end_time - start_time

files_per_second = total_files / duration if duration > 0 else 0

print(f"Performance Metrics:")
print(f"  Duration: {duration:.2f} seconds")
print(f"  Speed: {files_per_second:.1f} files/second")
print(f"  Estimated manual time: {total_files * 5} seconds")
print(f"  Time saved: {(total_files * 5) - duration:.2f} seconds")
```

---

## 📝 Starter Code

**File**: `file_organizer_starter.py`

```python
"""
Smart File Organizer
Automatically organizes files in a directory by extension

Author: [Your Name]
Date: [Date]
"""

import os
import shutil
from pathlib import Path

# Configuration
CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.pptx'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp']
}

def get_category(file_extension):
    """
    Returns the category for a given file extension.
    
    Args:
        file_extension (str): File extension (e.g., '.jpg')
    
    Returns:
        str: Category name or 'Other' if not found
    """
    for category, extensions in CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return 'Other'

def create_folders(base_path):
    """
    Creates category folders if they don't exist.
    
    Args:
        base_path (str): Base directory path
    """
    for category in CATEGORIES.keys():
        folder_path = os.path.join(base_path, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {category}/")
    
    # Create 'Other' folder
    other_path = os.path.join(base_path, 'Other')
    if not os.path.exists(other_path):
        os.makedirs(other_path)
        print(f"Created folder: Other/")

def organize_files(source_directory):
    """
    Main function to organize files in the specified directory.
    
    Args:
        source_directory (str): Path to directory to organize
    """
    print("=" * 60)
    print("FILE ORGANIZER - Starting...")
    print("=" * 60)
    
    # Check if directory exists
    if not os.path.exists(source_directory):
        print(f"Error: Directory '{source_directory}' not found!")
        return
    
    # Create category folders
    create_folders(source_directory)
    
    # Statistics
    stats = {
        'total': 0,
        'moved': 0,
        'skipped': 0,
        'errors': 0,
        'categories': {}
    }
    
    # Get all files in directory
    files = [f for f in os.listdir(source_directory) 
             if os.path.isfile(os.path.join(source_directory, f))]
    
    print(f"\nFound {len(files)} files to organize.\n")
    
    # Process each file
    for filename in files:
        try:
            # Get file extension
            _, extension = os.path.splitext(filename)
            
            # Skip files without extension
            if not extension:
                stats['skipped'] += 1
                continue
            
            # Get category
            category = get_category(extension)
            
            # Build source and destination paths
            source_path = os.path.join(source_directory, filename)
            dest_folder = os.path.join(source_directory, category)
            dest_path = os.path.join(dest_folder, filename)
            
            # Check if file already exists in destination
            if os.path.exists(dest_path):
                print(f"⚠️  Skipped (already exists): {filename}")
                stats['skipped'] += 1
                continue
            
            # Move file
            shutil.move(source_path, dest_path)
            print(f"✓ Moved to {category}/: {filename}")
            
            # Update statistics
            stats['moved'] += 1
            stats['categories'][category] = stats['categories'].get(category, 0) + 1
        
        except Exception as e:
            print(f"✗ Error processing {filename}: {e}")
            stats['errors'] += 1
        
        stats['total'] += 1
    
    # Display summary
    print("\n" + "=" * 60)
    print("ORGANIZATION COMPLETE")
    print("=" * 60)
    print(f"Total files: {stats['total']}")
    print(f"Moved: {stats['moved']}")
    print(f"Skipped: {stats['skipped']}")
    print(f"Errors: {stats['errors']}")
    
    if stats['categories']:
        print("\nFiles per category:")
        for category, count in sorted(stats['categories'].items()):
            print(f"  {category}: {count}")

def main():
    """Main program entry point"""
    print("Welcome to Smart File Organizer!")
    print("-" * 60)
    
    # Get directory from user
    directory = input("Enter directory path to organize (or '.' for current): ").strip()
    
    if directory == '.':
        directory = os.getcwd()
    
    # Confirm
    print(f"\nWill organize files in: {directory}")
    confirm = input("Continue? (yes/no): ").strip().lower()
    
    if confirm == 'yes':
        organize_files(directory)
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()
```

---

## 🧪 Testing Your File Organizer

### Create Test Files

```python
# test_file_creator.py
# Run this to create test files for your organizer

import os

def create_test_files():
    """Creates sample files for testing"""
    
    # Create test directory
    test_dir = "test_files_to_organize"
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    
    # Sample files to create
    test_files = [
        "vacation_photo.jpg",
        "meeting_notes.txt",
        "presentation.pptx",
        "song.mp3",
        "movie.mp4",
        "report.pdf",
        "data.csv",
        "photo2.png",
        "budget.xlsx",
        "script.py",
        "archive.zip",
        "document.docx",
        "image.gif",
        "video.avi"
    ]
    
    for filename in test_files:
        filepath = os.path.join(test_dir, filename)
        with open(filepath, 'w') as f:
            f.write(f"This is a test file: {filename}\n")
    
    print(f"✓ Created {len(test_files)} test files in '{test_dir}/'")
    print(f"Run your file organizer on this directory!")

if __name__ == "__main__":
    create_test_files()
```

---

## 📊 Evaluation Rubric

| Criteria | Points | Description |
|----------|--------|-------------|
| **Functionality** | 40 | |
| Base requirements work | 25 | All MVP features functional |
| Extensions implemented | 15 | 2+ extensions working correctly |
| **Code Quality** | 30 | |
| Code organization | 10 | Functions, clear structure |
| Comments & documentation | 10 | Docstrings, inline comments |
| Error handling | 10 | Try/except, user-friendly errors |
| **Creativity** | 20 | |
| Unique features | 10 | Original additions beyond requirements |
| User experience | 10 | Easy to use, clear feedback |
| **Documentation** | 10 | |
| README quality | 10 | Clear explanation, usage instructions |
| **Total** | **100** | |

---

# Option 2: Rule-Based Chatbot

## 📖 Project Description

Create an interactive chatbot that responds to user inputs based on predefined keywords and rules.

**Real-World Application**:
- Customer support automation
- FAQ systems
- Interactive tutorials
- Basic virtual assistants

---

## ✅ Base Requirements

### Minimum Viable Product (MVP)

Your chatbot MUST include:

1. **Keyword Recognition**
   - Detect keywords in user input
   - Match keywords to responses

2. **Multiple Conversation Paths**
   - At least 10 different keywords/phrases
   - Each with appropriate responses

3. **User-Friendly Interface**
   - Clear welcome message
   - Help command
   - Exit command
   - Good conversation flow

4. **Input Processing**
   - Handle different input formats
   - Basic text normalization

5. **Basic Logic**
   - if/elif/else structure
   - Sensible default responses

---

## 🌟 Extension Options (Choose 2+)

### 1. Response Variety
**Difficulty**: ⭐

Provide multiple possible responses for each keyword.

**Example**:
```
User: "hello"
Bot: (randomly picks)
  - "Hi there! How can I help you?"
  - "Hello! What can I do for you today?"
  - "Hey! Good to see you!"
```

**Implementation Hints**:
```python
import random

RESPONSES = {
    'greeting': [
        "Hi there! How can I help you?",
        "Hello! What can I do for you today?",
        "Hey! Good to see you!",
        "Greetings! How may I assist you?"
    ],
    'thanks': [
        "You're welcome!",
        "Happy to help!",
        "Anytime!",
        "Glad I could assist!"
    ]
}

def get_response(category):
    return random.choice(RESPONSES[category])
```

---

### 2. Fallback Logic
**Difficulty**: ⭐

Handle unknown inputs gracefully with helpful fallback responses.

**Implementation Hints**:
```python
FALLBACK_RESPONSES = [
    "I'm not sure I understand. Can you rephrase that?",
    "Hmm, I don't know about that. Try asking something else!",
    "Sorry, I didn't get that. Type 'help' to see what I can do.",
    "I'm still learning! Can you ask that differently?"
]

def get_fallback():
    return random.choice(FALLBACK_RESPONSES)

# In main loop
matched = False
for keyword, response in responses.items():
    if keyword in user_input:
        print(response)
        matched = True
        break

if not matched:
    print(get_fallback())
```

---

### 3. External Configuration
**Difficulty**: ⭐⭐⭐

Load keywords and responses from a JSON file.

**Benefits**:
- Easy to update responses without changing code
- Non-programmers can edit responses
- Better organization

**Example JSON** (`chatbot_config.json`):
```json
{
  "greetings": {
    "keywords": ["hello", "hi", "hey", "greetings"],
    "responses": [
      "Hi there! How can I help you?",
      "Hello! What can I do for you today?",
      "Hey! Good to see you!"
    ]
  },
  "farewell": {
    "keywords": ["bye", "goodbye", "see you", "exit"],
    "responses": [
      "Goodbye! Have a great day!",
      "See you later!",
      "Take care!"
    ]
  },
  "help": {
    "keywords": ["help", "what can you do", "commands"],
    "responses": [
      "I can chat about various topics! Try asking about weather, jokes, or say hello!"
    ]
  }
}
```

**Implementation Hints**:
```python
import json

def load_config(filename='chatbot_config.json'):
    """Load chatbot configuration from JSON file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file '{filename}' not found!")
        return {}

config = load_config()

def find_response(user_input, config):
    """Find matching response based on keywords"""
    user_input = user_input.lower()
    
    for intent, data in config.items():
        for keyword in data['keywords']:
            if keyword in user_input:
                return random.choice(data['responses'])
    
    return "I'm not sure how to respond to that."
```

---

### 4. Conversation Logging
**Difficulty**: ⭐⭐

Save conversation history to a file.

**Features**:
- Timestamp each message
- Save both user and bot messages
- Option to review history

**Implementation Hints**:
```python
from datetime import datetime

def log_conversation(user_input, bot_response, log_file='conversation_log.txt'):
    """Log conversation to file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] User: {user_input}\n")
        f.write(f"[{timestamp}] Bot: {bot_response}\n")
        f.write("-" * 50 + "\n")

# In main loop
while True:
    user_input = input("You: ")
    bot_response = get_response(user_input)
    print(f"Bot: {bot_response}")
    
    log_conversation(user_input, bot_response)
```

---

### 5. Case-Insensitive Matching
**Difficulty**: ⭐

Handle inputs regardless of capitalization.

**Implementation Hints**:
```python
def normalize_input(text):
    """Normalize user input for matching"""
    # Convert to lowercase
    text = text.lower()
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    # Remove punctuation (optional)
    import string
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    return text

# Usage
user_input = input("You: ")
normalized = normalize_input(user_input)

# Now check keywords against normalized input
if "hello" in normalized:
    print("Hi there!")
```

---

### 6. Context Awareness
**Difficulty**: ⭐⭐⭐⭐

Remember previous messages to provide contextual responses.

**Example**:
```
User: "What's your name?"
Bot: "I'm ChatBot! What's yours?"
User: "I'm Alice"
Bot: "Nice to meet you, Alice!"
User: "What's my name?"
Bot: "Your name is Alice!"
```

**Implementation Hints**:
```python
class Chatbot:
    def __init__(self):
        self.context = {
            'user_name': None,
            'last_topic': None,
            'conversation_count': 0
        }
    
    def remember_name(self, name):
        """Store user's name"""
        self.context['user_name'] = name
    
    def get_response(self, user_input):
        """Generate contextual response"""
        user_input = user_input.lower()
        
        # Check for name introduction
        if "i'm " in user_input or "i am " in user_input:
            # Extract name (simple approach)
            words = user_input.split()
            if "i'm" in user_input:
                name_index = words.index("i'm") + 1
            else:
                name_index = words.index("am") + 1
            
            if name_index < len(words):
                name = words[name_index].strip('.,!?')
                self.remember_name(name.capitalize())
                return f"Nice to meet you, {name.capitalize()}!"
        
        # Use context in responses
        if "my name" in user_input and self.context['user_name']:
            return f"Your name is {self.context['user_name']}!"
        
        # ... other responses ...
        
        return "I'm not sure about that."

# Usage
bot = Chatbot()
while True:
    user_input = input("You: ")
    response = bot.get_response(user_input)
    print(f"Bot: {response}")
```

---

## 📝 Starter Code

**File**: `chatbot_starter.py`

```python
"""
Rule-Based Chatbot
Responds to user inputs based on keyword matching

Author: [Your Name]
Date: [Date]
"""

import random

# Chatbot responses database
RESPONSES = {
    # Greetings
    'greeting': {
        'keywords': ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good evening'],
        'responses': [
            "Hello! How can I help you today?",
            "Hi there! What can I do for you?",
            "Hey! Good to see you!"
        ]
    },
    
    # Farewell
    'farewell': {
        'keywords': ['bye', 'goodbye', 'see you', 'farewell', 'exit', 'quit'],
        'responses': [
            "Goodbye! Have a great day!",
            "See you later!",
            "Take care!"
        ]
    },
    
    # How are you
    'wellbeing': {
        'keywords': ['how are you', 'how do you do', 'hows it going'],
        'responses': [
            "I'm doing great, thanks for asking! How about you?",
            "I'm fine! How can I assist you?",
            "All good here! What brings you today?"
        ]
    },
    
    # Thanks
    'thanks': {
        'keywords': ['thank', 'thanks', 'appreciate'],
        'responses': [
            "You're welcome!",
            "Happy to help!",
            "Anytime!",
            "Glad I could assist!"
        ]
    },
    
    # Help
    'help': {
        'keywords': ['help', 'what can you do', 'commands', 'options'],
        'responses': [
            "I can chat about various topics! Try greeting me, asking about weather, or request a joke!"
        ]
    },
    
    # Weather
    'weather': {
        'keywords': ['weather', 'temperature', 'forecast', 'rain', 'sunny'],
        'responses': [
            "I don't have real-time weather data, but you can check weather.com!",
            "Sorry, I can't check the weather right now. Try a weather app!",
            "For accurate weather info, I recommend checking your local weather service!"
        ]
    },
    
    # Jokes
    'joke': {
        'keywords': ['joke', 'funny', 'make me laugh'],
        'responses': [
            "Why did the Python programmer quit their job? They didn't get arrays!",
            "What do you call a programmer from Finland? Nerdic!",
            "Why do programmers prefer dark mode? Because light attracts bugs!"
        ]
    },
    
    # About bot
    'about': {
        'keywords': ['who are you', 'what are you', 'your name'],
        'responses': [
            "I'm a simple chatbot built with Python!",
            "I'm a rule-based chatbot. I match keywords to responses!",
            "I'm here to chat and help where I can!"
        ]
    },
    
    # Time
    'time': {
        'keywords': ['time', 'what time', 'clock'],
        'responses': [
            "I don't have access to real-time information, sorry!",
            "Check your device clock for the current time!"
        ]
    },
    
    # Capabilities
    'capabilities': {
        'keywords': ['what can you do', 'your capabilities', 'features'],
        'responses': [
            "I can chat, tell jokes, and respond to various keywords!",
            "I'm designed for simple conversations. Try asking me questions!",
            "My capabilities include greeting, chatting, and providing basic responses!"
        ]
    }
}

# Fallback responses for unknown inputs
FALLBACK_RESPONSES = [
    "I'm not sure I understand. Can you rephrase that?",
    "Hmm, I don't know about that. Try asking something else!",
    "Sorry, I didn't get that. Type 'help' to see what I can do.",
    "I'm still learning! Can you ask that differently?",
    "That's interesting, but I don't have a good response for that yet."
]

def find_response(user_input):
    """
    Find appropriate response based on user input.
    
    Args:
        user_input (str): User's message
    
    Returns:
        str: Bot's response
    """
    # Normalize input
    user_input = user_input.lower().strip()
    
    # Check each category
    for category, data in RESPONSES.items():
        for keyword in data['keywords']:
            if keyword in user_input:
                return random.choice(data['responses'])
    
    # No match found - return fallback
    return random.choice(FALLBACK_RESPONSES)

def main():
    """Main chatbot loop"""
    print("=" * 60)
    print("WELCOME TO CHATBOT")
    print("=" * 60)
    print("Hi! I'm a simple chatbot. Type 'help' to see what I can do.")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("-" * 60)
    
    conversation_count = 0
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Check for empty input
        if not user_input:
            print("Bot: Please say something!")
            continue
        
        # Check for exit commands
        if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
            print("Bot: Goodbye! Thanks for chatting!")
            break
        
        # Get and display response
        response = find_response(user_input)
        print(f"Bot: {response}")
        
        conversation_count += 1
    
    # End statistics
    print("\n" + "=" * 60)
    print(f"Conversation ended. We exchanged {conversation_count} messages.")
    print("=" * 60)

if __name__ == "__main__":
    main()
```

---

## 🧪 Testing Your Chatbot

### Test Scenarios

```python
# Test cases to verify your chatbot

test_inputs = [
    "hello",                    # Should greet
    "HELLO",                    # Test case insensitivity
    "how are you?",             # Wellbeing check
    "tell me a joke",           # Joke request
    "what's the weather like?", # Weather query
    "who are you?",             # About bot
    "thank you",                # Thanks
    "help",                     # Help command
    "asdfghjkl",                # Unknown input (fallback)
    "bye"                       # Exit
]

print("=== AUTOMATED CHATBOT TESTING ===\n")
for test_input in test_inputs:
    response = find_response(test_input)
    print(f"Input: {test_input}")
    print(f"Response: {response}\n")
```

---

## 📊 Evaluation Rubric

| Criteria | Points | Description |
|----------|--------|-------------|
| **Functionality** | 40 | |
| Base requirements work | 25 | 10+ keywords, proper matching |
| Extensions implemented | 15 | 2+ extensions working correctly |
| **Code Quality** | 30 | |
| Code organization | 10 | Clean structure, readable |
| Comments & documentation | 10 | Clear explanations |
| User experience | 10 | Good conversation flow |
| **Creativity** | 20 | |
| Response variety | 10 | Interesting, engaging responses |
| Unique features | 10 | Original additions |
| **Documentation** | 10 | |
| README quality | 10 | Clear usage instructions |
| **Total** | **100** | |

---

## 📄 README Template

Both projects should include a README file:

```markdown
# [Project Name]

## Description
[Brief description of what your project does]

## Features
- [List key features]
- [Include any extensions you implemented]

## Requirements
- Python 3.x
- [Any additional libraries]

## Installation
```bash
# Clone or download project
# Install dependencies (if any)
pip install -r requirements.txt
```

## Usage
```bash
python file_organizer.py
# or
python chatbot.py
```

## How It Works
[Explain your approach]

## Extensions Implemented
1. **[Extension Name]**: [Brief description]
2. **[Extension Name]**: [Brief description]

## Example Output
```
[Paste example of your program running]
```

## Challenges & Solutions
[Optional: What was difficult and how you solved it]

## Future Improvements
[Optional: What you would add with more time]

## Author
[Your Name]
```

---

## 💡 Tips for Success

### For Both Projects

1. **Start with MVP**
   - Get basic functionality working first
   - Then add extensions one at a time

2. **Test Frequently**
   - Test after each feature
   - Don't wait until the end

3. **Handle Errors**
   - Use try/except blocks
   - Provide helpful error messages

4. **Document as You Go**
   - Add comments while coding
   - Write README incrementally

5. **Keep It Simple**
   - Don't overcomplicate
   - Working code > complex code

### Common Pitfalls to Avoid

❌ **Don't**:
- Wait until last minute
- Skip error handling
- Forget to comment code
- Ignore edge cases
- Make it too complex

✅ **Do**:
- Start early
- Test incrementally
- Document clearly
- Handle errors gracefully
- Ask for help when stuck

---

## 🏆 Going Above and Beyond

Want to make your project stand out?

### File Organizer
- GUI interface (tkinter)
- Undo functionality
- Watch folder for new files
- Email report of changes
- Configuration file for categories

### Chatbot
- Sentiment analysis
- Spell checking
- Multiple languages
- Voice input/output
- GUI interface

---

## 📞 Getting Help

**If you're stuck:**
1. Review Day 1 and Day 2 materials
2. Check Python documentation
3. Search Stack Overflow
4. Ask in workshop channel/email
5. Debug with print statements

**Good luck with your project! 🚀**

---

## 📤 Submission Checklist

Before submitting, ensure you have:

- [ ] Python file (.py) with your code
- [ ] README.md with documentation
- [ ] Screenshots or video demo
- [ ] All requirements implemented
- [ ] At least 2 extensions completed
- [ ] Code is commented
- [ ] Tested and working
- [ ] No syntax errors
- [ ] Professional presentation

**Submit by**: [Workshop End Date]  
**Submit to**: [Email/Platform]

---

**Remember**: The goal isn't perfection - it's learning and building! Focus on making something functional and be proud of what you create! 🎉
