# 📧 Spam Mail Prediction Using Machine Learning and Django

This project is a full-stack **Spam Email Classifier Web App** built using **Django** and a **Logistic Regression ML model**. It allows users to **register, log in**, input email content, and get real-time **spam predictions**, with personal prediction history.

---   
   
## 📁 Project Overview  

- Built with Django and deployed on **Railway**
- Uses **TF-IDF Vectorizer** and **Logistic Regression**
- User authentication (register, login, logout)
- Predictions and history saved per user
- Clean and responsive UI with Bootstrap 5

---

## 🧠 Machine Learning Model 

The ML model was trained using `mail_data.csv` with the following steps:

- **Preprocessing**: Lowercasing, stopword removal, tokenization
- **Feature Extraction**: TF-IDF Vectorizer
- **Model**: Logistic Regression
- **Evaluation**:
  - Training Accuracy: ~97%
  - Testing Accuracy: ~96%

Final files used in the app:

- `spam_model.pkl`: Saved ML model  
- `vectorizer.pkl`: Saved TF-IDF Vectorizer

---

## 🗂️ Key Files

- `Spam Mail Prediction Using ML.ipynb`: Jupyter Notebook for model training  
- `mail_data.csv`: Dataset with labeled emails  
- `spam_model.pkl`, `vectorizer.pkl`: Trained model & vectorizer  
- `spam_app/`: Django app folder (views, templates, static files)  
- `spam_detector/`: Django project config (settings, URLs)  
- `templates/spam_app/`: HTML templates  
- `static/style.css`: CSS styling  

---

## ⚙️ Installation (Local)

1. Clone the repository:

```bash
git clone https://github.com/prav0106/Spam-Mail-Prediction.git
cd Spam-Mail-Prediction
```

2. Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver
```

App will run at `http://127.0.0.1:8000/`

---

## 🌍 Live Deployment

🔗 Deployed on Railway:  
[https://spam-mail-prediction-production.up.railway.app/](https://spam-mail-prediction-production.up.railway.app/)

(*Note: Deployment might throw error if `.pkl` files aren't loaded properly on Railway — works fine locally.*)

---

## 📌 Note

This project is for academic use and personal learning. Not intended for production-scale use.
