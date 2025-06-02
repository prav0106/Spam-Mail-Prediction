# 📧 Spam Mail Prediction Using Machine Learning

This project is a machine learning-based spam email classifier that predicts whether a given email is **spam** or **not spam**. It uses natural language processing (NLP) techniques and machine learning models to analyze and classify email content.

---

## 📂 Project Structure

- `Spam Mail Prediction Using ML.ipynb`: Jupyter Notebook containing the entire pipeline — from preprocessing and vectorization to model training and prediction.
- `mail_data.csv`: Dataset containing labeled email messages.     

---

## 🚀 Features

- Email preprocessing (cleaning, tokenization, stemming)
- TF-IDF vectorization for converting text to numerical form
- Logistic Regression model for prediction
- Performance evaluation using accuracy, confusion matrix, and classification report

---

## 📊 Dataset Description

The dataset used (`mail_data.csv`) has the following columns:

- `Category`: The label (either `spam` or `ham`)
- `Message`: The email content

---

## 🧠 ML Techniques Used

- **Text Preprocessing**
  - Lowercasing
  - Removing special characters
  - Removing stopwords
  - Tokenization and Stemming
- **Feature Extraction**
  - TF-IDF Vectorizer
- **Model**
  - Logistic Regression

---

## 📈 Evaluation Metrics

- Accuracy Score
- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)

---

## 🛠️ Installation & Requirements

Install the required libraries using:

```bash
pip install numpy pandas scikit-learn matplotlib nltk
