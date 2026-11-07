# PHISHING EMAIL DETECTION MODEL
## Assignment Report

### 1. Introduction
Phishing is a cyberattack in which an attacker sends deceptive messages to trick recipients into revealing confidential information, clicking malicious links, or downloading harmful files. This project uses machine learning to identify suspicious email messages and classify them as **Phishing** or **Safe**.

### 2. Objectives
- Build a basic email classification model using Scikit-learn.
- Prepare labelled phishing and legitimate email examples.
- Extract useful textual and URL-related features.
- Evaluate the model using accuracy, precision, recall, F1-score and a confusion matrix.

### 3. Tools and Technologies
- Programming language: Python
- Machine-learning library: Scikit-learn
- Data handling: Pandas
- Text representation: TF-IDF
- Visualisation: Matplotlib

### 4. System Working
1. Load the labelled email dataset from `data/emails.csv`.
2. Clean and validate the input records.
3. Split the dataset into training and testing portions.
4. Convert email text into TF-IDF features.
5. Extract URL and message indicators such as URL count, suspicious words, uppercase ratio and message length.
6. Train a Random Forest classifier.
7. Predict labels for the test emails and display evaluation metrics.
8. Optionally classify a new email supplied by the user.

### 5. Key Features
- Learns from phishing and safe email examples.
- Analyses words and phrases commonly found in suspicious messages.
- Checks URL-related and formatting signals.
- Classifies messages into two categories.
- Displays a confusion matrix and standard classification metrics.

### 6. Expected Outcome
The program produces a predicted label, either **PHISHING** or **SAFE**, and prints model evaluation results. The exact scores depend on the dataset and train/test split. The supplied small synthetic dataset is intended only to demonstrate the complete workflow.

### 7. Testing
Test the program with:
- A normal meeting or college announcement email.
- An email asking for a password or OTP.
- An email containing an urgent account-verification link.
- An email containing no URL but suspicious requests.

Check that the program runs without errors, displays metrics and saves `confusion_matrix.png`. Predictions should be reviewed rather than treated as guaranteed.

### 8. Limitations
- The sample dataset is small and synthetic.
- Attackers continuously change wording, domains and techniques.
- URL text alone cannot confirm whether a website is malicious.
- Real-world deployment requires a larger representative dataset, privacy controls and ongoing monitoring.

### 9. Future Scope
- Train and validate using a larger public phishing-email dataset.
- Add sender-domain, header, attachment and domain-reputation analysis.
- Build a web interface for pasting or uploading email text.
- Add model versioning and periodic retraining.
- Integrate with an email client only after security and privacy review.

### 10. Conclusion
The project demonstrates how machine learning and text analysis can support phishing email detection. TF-IDF captures word patterns, while engineered features provide additional information about links and message structure. The model classifies messages as phishing or safe and reports its performance through evaluation metrics and a confusion matrix. It provides a foundation for further development, but should not be considered a production-grade security solution.
