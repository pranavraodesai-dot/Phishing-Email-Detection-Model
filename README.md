# Phishing Email Detection Model

## Overview
A Python machine-learning project that classifies email text as **Phishing** or **Safe** using Scikit-learn.

## Features
- Trains on labelled phishing and legitimate email examples.
- Converts email text into TF-IDF word features.
- Extracts additional signals: URL count, HTTP/HTTPS presence, suspicious words, uppercase ratio, message length and exclamation marks.
- Reports test accuracy, precision, recall and F1-score.
- Displays and saves a confusion matrix.
- Can classify a message entered on the command line.

## Requirements
Python 3.9 or later.

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

## Run training and evaluation
From this folder:
```bash
python main.py
```
This prints evaluation metrics and saves `confusion_matrix.png`.

## Classify a message
```bash
python main.py --message "URGENT: verify your password at http://example.test"
```

## Dataset
`data/emails.csv` contains two columns:
- `email_text`: the email content
- `label`: `safe` or `phishing`

The included dataset is a small, synthetic demonstration dataset so the project runs immediately. For a meaningful real-world evaluation, replace it with a larger, ethically sourced and labelled dataset, remove duplicates, and test on emails not used during training.

## Important limitation
This is an educational prototype, not a production email security gateway. Do not use its prediction as the sole basis for security decisions. A model can miss new phishing tactics or incorrectly flag legitimate emails.
