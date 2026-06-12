# Support Ticket Classification & Prioritization

An end-to-end machine learning system that automatically classifies customer support tickets and assigns priority levels.

## 📋 Overview

This solution addresses a real problem faced by support teams:
- **Hundreds of tickets** arrive daily across different channels
- **No automatic categorization** → tickets get misrouted or delayed
- **No priority sorting** → urgent issues pile up in the queue
- **Wasted time** → support staff spend hours on manual triage instead of solving problems

This ML system learns to:
1. **Classify** tickets into categories (Billing, Technical Issue, Account, General Query)
2. **Predict priority** (High, Medium, Low) based on ticket text
3. **Route intelligently** so urgent issues get handled first

## 🚀 Quick Start

### Option 1: Run the Notebook Directly

1. Open VS Code
2. Navigate to the workspace folder:
   ```
   d:\internship\FUTURE_ML_02\
   ```
3. Open the notebook:
   ```
   support_ticket_classification.ipynb
   ```
4. Select a Python kernel (3.9+)
5. Run all cells (`Ctrl+Alt+Enter` or use the notebook toolbar)

### Option 2: Set Up and Run from Terminal

```bash
# Navigate to the workspace
cd d:\internship\FUTURE_ML_02

# Create a virtual environment (optional)
python -m venv venv
venv\Scripts\activate

# Install required libraries
pip install pandas scikit-learn matplotlib seaborn jupyter

# Start Jupyter
jupyter notebook
```

## 📊 What the Notebook Does

### 1. **Data Loading**
- Includes a **realistic demo dataset** with 30 sample tickets
- Covers all four categories and three priority levels
- If you add a CSV file with ticket data, the notebook will use it automatically

### 2. **Text Cleaning**
- Lowercases text
- Removes URLs, punctuation, numbers
- Removes English stopwords (common words like "the", "a", "and")
- Keeps meaningful tokens for model training

### 3. **Feature Extraction (TF-IDF)**
- Converts text into numerical features
- Captures word importance and relevance
- Uses unigrams and bigrams to capture context

### 4. **Model Training**
- **Category Classifier**: Predicts the ticket type using Logistic Regression
- **Priority Classifier**: Predicts urgency level
- Both use the same pipeline: TF-IDF vectorizer + Logistic Regression

### 5. **Evaluation**
- **Accuracy**: Overall correctness
- **Precision & Recall**: Per-class performance
- **Confusion Matrix**: Shows which categories get confused
- **Classification Report**: Detailed per-class metrics

### 6. **Inference**
- Try the model on **new unseen tickets**
- See how it would route them in production

## 📁 Dataset Structure

If you use your own CSV file, it should have columns named something like:
- **Ticket text**: `ticket_text`, `text`, `description`, `message`, or `issue`
- **Category**: `category`, `topic`, `type`, or `label`
- **Priority** (optional): `priority`, `severity`, or `urgency`

The notebook will try to find these columns automatically.

### Recommended Public Datasets
If you want to test with real data:
1. **Customer Support Tickets (Kaggle)**: [Link](https://www.kaggle.com/datasets/suraj520/customer-support-ticket-dataset)
2. **IT Service Tickets (Kaggle)**: [Link](https://www.kaggle.com/datasets/adisongoh/it-service-ticket-classification-dataset)
3. **IT Support Tickets (Zenodo)**: [Link](https://zenodo.org/records/7648117)

## 🎯 Categories Used

| Category | Examples |
|----------|----------|
| **Billing** | Charges, refunds, payment methods, invoicing |
| **Account** | Login issues, password reset, account access |
| **Technical Issue** | Bugs, errors, performance, crashes |
| **General Query** | Feature questions, documentation, pricing info |

## 🔴 Priority Levels

| Level | Indicators | Response Time |
|-------|-----------|----------------|
| **High** | Locked account, service down, data loss, security issue | < 1 hour |
| **Medium** | Errors, delays, missing features | < 4 hours |
| **Low** | General questions, feature requests | < 24 hours |

## 📈 How It Works in Production

```
Customer submits ticket
          ↓
Model classifies category + priority
          ↓
Ticket routed to correct team
          ↓
High-priority tickets surfaced first
          ↓
Support team handles urgent issues faster
```

## 🔧 Model Performance

The demo notebook achieves high accuracy on the sample data. Real-world performance depends on:
- **Dataset size**: More tickets → better accuracy
- **Label quality**: Consistent categorization in training data
- **Text clarity**: Clear descriptions improve classification
- **Class balance**: Similar number of examples per category

## 💡 Key Insights

1. **TF-IDF + Logistic Regression** is a proven baseline for text classification
2. **Bigrams** (2-word phrases) capture more context than single words alone
3. **Priority prediction** often has patterns (keywords like "urgent", "down", "locked")
4. **Hybrid approach** works best: combine ML predictions with business rules for critical cases

## 🛠️ Customization

To adapt this to your support system:

1. **Swap categories**: Replace "Billing", "Technical", etc. with your team's structure
2. **Change priority levels**: Adjust High/Medium/Low to match your SLA
3. **Add business rules**: Flag certain keywords for automatic escalation
4. **Connect to ticketing system**: Integrate predictions into Zendesk, Jira, or similar

## 📦 Dependencies

- `pandas` – Data manipulation
- `scikit-learn` – ML models, TF-IDF, evaluation metrics
- `matplotlib` – Visualization
- `seaborn` – Enhanced plots (optional)

Install all at once:
```bash
pip install pandas scikit-learn matplotlib seaborn
```

## 📝 Notes

- The notebook uses a small demo dataset to run quickly and without external downloads
- Add your own CSV to the folder for larger-scale training
- The model trains in seconds even with modest hardware
- Confusion matrices help debug why certain tickets are misclassified

## 🎓 What You'll Learn

✔ How text preprocessing improves ML models  
✔ How TF-IDF transforms words into numbers  
✔ How to build and evaluate classification pipelines  
✔ How machine learning solves real business problems  
✔ How to interpret precision, recall, and confusion matrices  

## 📞 Support

If you encounter issues:
1. Ensure Python 3.9+ is installed
2. Run `pip install --upgrade scikit-learn pandas matplotlib`
3. Restart the Jupyter kernel
4. Check that the notebook file is valid JSON (valid VS Code should catch errors)

---

**Built as part of a real-world ML internship exercise.**
