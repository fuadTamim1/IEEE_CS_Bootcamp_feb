"""
DAY 3 - LESSON 10: Introduction to AI and Data Science Libraries
=============================================================

Learning Objectives:
- Understand NumPy and arrays
- Learn Pandas for data analysis
- Understand scikit-learn basics
- Learn about machine learning workflow
- Understand AI/ML roadmap and next steps

Key Concepts:
- NumPy: Numerical computing with arrays
- Pandas: Data analysis with DataFrames
- scikit-learn: Machine learning algorithms
- Features and Labels: Input and output for ML models
- Training and Testing: How to evaluate models
"""

# Note: This lesson assumes libraries are installed via requirements.txt
# Install with: pip install -r requirements.txt

print("=== INTRODUCTION TO AI AND DATA SCIENCE LIBRARIES ===\n")


# ===== SECTION 1: Understanding NumPy =====
print("=== NUMPY BASICS ===\n")

print("""
NumPy: Numerical Python
- Fast numerical computing
- Works with arrays and matrices
- Foundation for most data science libraries

Key concepts:
- Array: Collection of elements (like list but more efficient)
- ndarray: N-dimensional array
- Element-wise operations: Operations on all elements at once
""")

try:
    import numpy as np
    
    # Create arrays
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Array: {arr}")
    print(f"Shape: {arr.shape}")
    print(f"Data type: {arr.dtype}")
    
    # Array operations
    print(f"\nOperations:")
    print(f"  Sum: {np.sum(arr)}")
    print(f"  Mean: {np.mean(arr)}")
    print(f"  Max: {np.max(arr)}")
    print(f"  Min: {np.min(arr)}")
    
    # 2D array (matrix)
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"\nMatrix shape: {matrix.shape}")
    print(f"Matrix:\n{matrix}")
    
except ImportError:
    print("NumPy not installed. Install with: pip install numpy")


# ===== SECTION 2: Understanding Pandas =====
print("\n\n=== PANDAS BASICS ===\n")

print("""
Pandas: Data Analysis Library
- DataFrames: 2D labeled data (like spreadsheet)
- Series: 1D labeled data
- Easy data manipulation and analysis
- Great for working with CSV, JSON, Excel files
""")

try:
    import pandas as pd
    
    # Create DataFrame from dictionary
    data = {
        'Name': ['Ahmed', 'Sara', 'Ali', 'Fatima'],
        'Age': [25, 23, 24, 22],
        'Score': [95, 88, 92, 90],
        'City': ['Cairo', 'Alexandria', 'Giza', 'Aswan']
    }
    
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)
    
    print(f"\nDataFrame info:")
    print(f"  Shape: {df.shape}")
    print(f"  Columns: {list(df.columns)}")
    
    # Basic statistics
    print(f"\nStatistics:")
    print(f"  Average age: {df['Age'].mean()}")
    print(f"  Average score: {df['Score'].mean()}")
    print(f"  Highest score: {df['Score'].max()}")
    
    # Filtering
    print(f"\nFiltering (Score >= 90):")
    high_scorers = df[df['Score'] >= 90]
    print(high_scorers)
    
except ImportError:
    print("Pandas not installed. Install with: pip install pandas")


# ===== SECTION 3: Understanding scikit-learn =====
print("\n\n=== SCIKIT-LEARN BASICS ===\n")

print("""
scikit-learn: Machine Learning Library
- Simple and efficient tools for ML
- Supervised learning: Classification, Regression
- Unsupervised learning: Clustering, Dimensionality reduction
- Tools for model selection and evaluation
""")

try:
    from sklearn.datasets import load_iris
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    
    print("✓ scikit-learn is available")
    
    # Load sample dataset
    iris = load_iris()
    X = iris.data  # Features
    y = iris.target  # Labels
    
    print(f"\nIris Dataset:")
    print(f"  Features shape: {X.shape}")
    print(f"  Samples: {X.shape[0]}")
    print(f"  Features per sample: {X.shape[1]}")
    print(f"  Classes: {len(set(y))}")
    
    # Split data into training and testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    
    print(f"\nTrain-test split:")
    print(f"  Training samples: {len(X_train)}")
    print(f"  Testing samples: {len(X_test)}")
    
    # Train model
    print(f"\nTraining RandomForest classifier...")
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    print("  ✓ Model trained")
    
    # Make predictions
    predictions = model.predict(X_test)
    
    # Evaluate
    accuracy = accuracy_score(y_test, predictions)
    print(f"\nModel accuracy: {accuracy:.2%}")
    
except ImportError as e:
    print(f"scikit-learn or dependencies not available: {e}")
    print("Install with: pip install scikit-learn numpy scipy")


# ===== SECTION 4: Machine Learning Workflow =====
print("\n\n=== MACHINE LEARNING WORKFLOW ===\n")

print("""
Typical ML workflow:

1. DATA COLLECTION
   └─ Gather data from various sources
   
2. DATA PREPARATION
   ├─ Clean: Remove errors, handle missing values
   ├─ Transform: Convert to proper format
   └─ Feature Engineering: Create new features
   
3. EXPLORATORY DATA ANALYSIS
   ├─ Visualize data
   ├─ Find patterns
   └─ Check for correlations
   
4. MODEL SELECTION
   ├─ Choose algorithm (Linear, Tree, Neural Net, etc.)
   ├─ Set hyperparameters
   └─ Consider computational needs
   
5. MODEL TRAINING
   ├─ Split into train/test (70/30 or 80/20)
   ├─ Train on training data
   └─ Track training progress
   
6. MODEL EVALUATION
   ├─ Test on test data (NOT training data)
   ├─ Calculate metrics (accuracy, precision, recall)
   └─ Check for overfitting
   
7. HYPERPARAMETER TUNING
   ├─ Adjust parameters
   ├─ Try different algorithms
   └─ Compare results
   
8. DEPLOYMENT
   ├─ Save model
   ├─ Create API/service
   └─ Monitor performance

Key terms:
- Features: Input variables (X)
- Labels: Output variables (y)
- Training set: Data used to train model
- Test set: Data used to evaluate model
- Overfitting: Model memorizes training data
- Underfitting: Model is too simple
""")


# ===== SECTION 5: Types of Machine Learning =====
print("\n=== TYPES OF MACHINE LEARNING ===\n")

print("""
1. SUPERVISED LEARNING
   ├─ Classification
   │  ├─ Binary: Yes/No, Spam/Not Spam
   │  └─ Multi-class: Iris type, Hand-written digit
   │
   └─ Regression
      └─ Predict numerical values: House price, Temperature

2. UNSUPERVISED LEARNING
   ├─ Clustering: Group similar items
   │  ├─ K-Means
   │  └─ Hierarchical Clustering
   │
   └─ Dimensionality Reduction: Reduce features
      └─ PCA: Principal Component Analysis

3. REINFORCEMENT LEARNING
   └─ Agent learns through rewards/penalties
      ├─ Game AI
      ├─ Robot control
      └─ Autonomous driving

4. DEEP LEARNING
   └─ Neural networks with multiple layers
      ├─ Image recognition
      ├─ Natural language processing
      └─ Time series forecasting

In this workshop: Focus on Supervised Learning (Classification)
""")


# ===== SECTION 6: Simple Prediction Example =====
print("\n=== SIMPLE PREDICTION EXAMPLE ===\n")

print("""
Use case: Predict if someone will buy a product

Features:
- Age
- Income
- Previous purchases
- Time spent on site

Label:
- Bought (Yes/No)

Steps:
1. Collect historical data
2. Train model with features and labels
3. Use trained model to predict for new customer
""")

try:
    import numpy as np
    from sklearn.preprocessing import StandardScaler
    from sklearn.tree import DecisionTreeClassifier
    
    # Simulated customer data
    # Features: [Age, Income (in $1000s), Previous Purchases]
    X = np.array([
        [25, 30, 2],   # Young, low income, few purchases -> No
        [45, 80, 15],  # Middle age, high income, many purchases -> Yes
        [30, 50, 5],   # Young, medium income, some purchases -> Yes
        [22, 25, 1],   # Young, low income, no purchases -> No
        [55, 100, 20], # Older, high income, many purchases -> Yes
        [35, 60, 10],  # Middle age, medium income, some purchases -> Yes
    ])
    
    # Labels: 0 = No purchase, 1 = Yes purchase
    y = np.array([0, 1, 1, 0, 1, 1])
    
    # Train model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)
    
    # Predict for new customer
    new_customer = [[30, 55, 8]]  # 30 years old, $55k income, 8 previous purchases
    prediction = model.predict(new_customer)
    probability = model.predict_proba(new_customer)
    
    print("Customer Profile:")
    print(f"  Age: 30")
    print(f"  Income: $55,000")
    print(f"  Previous Purchases: 8")
    
    print(f"\nPrediction:")
    print(f"  Will buy: {'Yes' if prediction[0] == 1 else 'No'}")
    print(f"  Confidence (No): {probability[0][0]:.2%}")
    print(f"  Confidence (Yes): {probability[0][1]:.2%}")
    
except Exception as e:
    print(f"Error running example: {e}")


# ===== SECTION 7: AI/ML Roadmap =====
print("\n\n=== AI/ML LEARNING ROADMAP ===\n")

print("""
After this workshop, your learning path:

PHASE 1: FOUNDATIONS (Current + 2-4 weeks)
├─ Python fundamentals ✓
├─ Data manipulation (Pandas)
├─ Basic statistics
└─ Visualization (Matplotlib, Seaborn)

PHASE 2: MACHINE LEARNING (4-8 weeks)
├─ Supervised learning algorithms
├─ Model evaluation and validation
├─ Feature engineering
├─ Classification problems
└─ Regression problems

PHASE 3: ADVANCED TECHNIQUES (8-16 weeks)
├─ Ensemble methods
├─ Cross-validation
├─ Hyperparameter tuning
├─ Text processing (NLP)
└─ Time series analysis

PHASE 4: DEEP LEARNING (16+ weeks)
├─ Neural networks (TensorFlow/Keras)
├─ Convolutional Neural Networks (CNN) - Image recognition
├─ Recurrent Neural Networks (RNN) - Sequential data
└─ Transformers - State-of-the-art NLP

PHASE 5: SPECIALIZATION (Choose your path)
├─ Computer Vision
│  └─ Object detection, Image segmentation
├─ Natural Language Processing (NLP)
│  └─ Text classification, Translation
├─ Recommender Systems
│  └─ Personalized recommendations
├─ Reinforcement Learning
│  └─ Game AI, Robotics
└─ MLOps & Deployment
   └─ Model serving, Monitoring, Scaling

Resources:
- Kaggle (datasets and competitions)
- Coursera (structured courses)
- Fast.ai (practical deep learning)
- Papers With Code (latest research)
""")


# ===== SECTION 8: AI in Real World =====
print("\n=== AI IN REAL WORLD ===\n")

print("""
Current AI Applications:

1. RECOMMENDATION SYSTEMS
   ├─ Netflix: Movie recommendations
   ├─ Amazon: Product recommendations
   └─ Spotify: Music recommendations

2. NATURAL LANGUAGE PROCESSING
   ├─ Chatbots (ChatGPT, Gemini, etc.)
   ├─ Translation (Google Translate)
   ├─ Sentiment analysis
   └─ Text classification

3. COMPUTER VISION
   ├─ Face recognition
   ├─ Object detection
   ├─ Medical imaging
   └─ Autonomous vehicles

4. AUTOMATION
   ├─ RPA (Robotic Process Automation)
   ├─ Document processing
   ├─ Data entry
   └─ Customer service

5. PREDICTIVE ANALYTICS
   ├─ Stock price prediction
   ├─ Weather forecasting
   ├─ Disease diagnosis
   └─ Customer churn prediction

6. GENERATIVE AI
   ├─ Image generation (DALL-E, Midjourney)
   ├─ Text generation (ChatGPT, Claude)
   ├─ Code generation (GitHub Copilot)
   └─ Video generation

Career opportunities:
- Machine Learning Engineer
- Data Scientist
- AI Researcher
- MLOps Engineer
- AI Product Manager
- AI Ethics Specialist
""")


# ===== SECTION 9: AI + Automation Combined =====
print("\n=== AI + AUTOMATION ===\n")

print("""
Combining AI with Automation:

1. INTELLIGENT RPA
   ├─ Use AI to understand documents
   ├─ Automate decision-making
   └─ Learn from new patterns

2. PREDICTIVE MAINTENANCE
   ├─ Monitor equipment with sensors
   ├─ Use ML to predict failures
   ├─ Schedule maintenance proactively
   └─ Reduce downtime

3. INTELLIGENT WORKFLOWS
   ├─ Auto-route documents
   ├─ Classification
   ├─ Priority assignment
   └─ Alert escalation

4. CHATBOT + AUTOMATION
   ├─ AI chatbot understands user intent
   ├─ Triggers automated workflows
   ├─ Handles complex scenarios
   └─ Routes to human when needed

Tools:
- n8n + Python: Automation + ML
- Make.com: Visual automation + integrations
- Zapier: No-code automation + webhooks
- Custom Python scripts: Full control

Example:
  Automated Email Processing:
  1. Email arrives
  2. AI extracts information
  3. Automation routes to correct department
  4. Workflow starts automatically
  5. Sends status to user
""")


# ===== SECTION 10: Project Ideas Using AI + Automation =====
print("\n=== PROJECT IDEAS ===\n")

print("""
Beginner Projects:
1. Iris Flower Classification
   - Classic ML dataset
   - Learn classification basics
   - Implement DecisionTree, RandomForest

2. Email Spam Detection
   - Text classification
   - Learn about NLP basics
   - Feature extraction

3. House Price Prediction
   - Regression problem
   - Real estate dataset
   - Model evaluation

Intermediate Projects:
1. Customer Churn Prediction
   - Business analytics
   - Feature engineering
   - Model comparison

2. Sentiment Analysis
   - NLP + classification
   - Twitter/Review data
   - Deploy as API

3. Credit Risk Assessment
   - Binary classification
   - Business impact
   - Interpretability focus

Advanced Projects:
1. Image Classification
   - Deep learning
   - Convolutional neural networks
   - Transfer learning

2. Time Series Forecasting
   - Stock prices or weather
   - RNNs or LSTMs
   - Performance monitoring

3. Recommendation System
   - Collaborative filtering
   - Content-based recommendations
   - A/B testing
""")


# ===== SECTION 11: Next Steps =====
print("\n=== NEXT STEPS ===\n")

print("""
After completing this workshop:

Week 1-2: PRACTICE & REINFORCE
├─ Re-run all lessons
├─ Complete all exercises
├─ Build the final projects
└─ Share your work

Week 3-4: EXPLORE & EXPERIMENT
├─ Try Kaggle datasets
├─ Modify examples
├─ Combine Day 1-3 concepts
└─ Start simple ML project

Month 2: DEEPEN KNOWLEDGE
├─ Take structured ML course
├─ Learn more about Pandas & NumPy
├─ Build real project with real data
└─ Learn data visualization

Resources:
- Online Communities:
  └─ r/learnprogramming, r/MachineLearning, Stack Overflow
- Practice Platforms:
  └─ LeetCode, HackerRank, Codewars
- Free Courses:
  └─ Fast.ai, Coursera (audit option), YouTube tutorials
- Books:
  └─ \"Python Crash Course\", \"Hands-On ML with TensorFlow\"

Remember:
- Practice consistently
- Build projects, don't just watch tutorials
- Join communities and ask questions
- Share your learnings
- Celebrate small wins
- Keep learning!
""")


print("\n✅ Lesson 10 Complete!")
print("🎉 You've completed Day 3 - AI & Automation Systems!")
print("\n🎓 WORKSHOP COMPLETE!")
print("═" * 50)
print("You now have:")
print("✓ Python fundamentals")
print("✓ Automation skills")
print("✓ File handling capabilities")
print("✓ API integration knowledge")
print("✓ Introduction to AI/ML")
print("✓ Error handling experience")
print("\nNext: Work on Final Projects!")
print("═" * 50)
