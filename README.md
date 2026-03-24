# 🔍 TrustLensAI — Fake Review Detection System

TrustLensAI is a Flask-based web application that detects whether a product review is **Fake or Real** and assigns a **Trust Score (0–100)**.

It helps:

* 🛍️ Consumers evaluate review authenticity
* 🏢 Businesses monitor suspicious feedback
* 🛠️ Admins manage system-wide analytics

---

## 🚀 Features

* ✅ Fake vs Real Review Classification (SVM)
* 📊 Trust Score Calculation (0–100)
* 📈 Dashboard & Analytics
* 👥 Role-based Access (User / Business / Admin)
* 🧠 NLP Pipeline (TF-IDF + SVM)
* 🌐 Flask Web Interface

---

## 🧠 Tech Stack

* **Backend:** Flask (Python)
* **Machine Learning:** scikit-learn (SVM)
* **Database:** SQLite / MySQL
* **Frontend:** HTML, CSS, JS (Bootstrap)
* **Model Storage:** joblib (.pkl files)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/TrustLensAI.git
cd TrustLensAI
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Train Model (Optional)

```bash
python train_model.py
```

### 5️⃣ Run Application

```bash
python app.py
```

### 6️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 📊 Machine Learning Pipeline

1. Text preprocessing:

   * Lowercasing
   * Stopword removal
   * Punctuation cleaning

2. Feature Extraction:

   * TF-IDF (uni + bi-grams)

3. Model:

   * Linear Support Vector Machine (LinearSVC)

4. Output:

   * Fake / Real classification
   * Confidence Score
   * Trust Score (heuristic-based)

---

## 🔐 Trust Score Logic

Score is reduced based on:

* Excessive punctuation (!!)
* ALL CAPS words
* Contradictory sentiment
* Very short negative reviews
* Generic complaints

Final score is clipped between **0–100**

---

## 🏗️ Project Structure

```
TrustLensAI/
│── app.py
│── train_model.py
│── reviews.csv
│── svm_model.pkl
│── vectorizer.pkl
│── requirements.txt
│── templates/
│── static/
│── utils/
```

---

## 👥 User Roles

| Role     | Access         |
| -------- | -------------- |
| User     | Submit reviews |
| Business | View analytics |
| Admin    | Full control   |

---

## 📈 Use Cases

* E-commerce platforms
* Review moderation systems
* Brand monitoring tools
* Browser extensions for trust scoring

---

## 🔒 Security Notice

Sensitive data such as:

* API keys
* Database credentials
* Secret keys

are **NOT included** in this repository.

Use `.env` file for local configuration.

---

## 📌 Future Improvements

* 🔐 Two-Factor Authentication
* 💳 Payment Integration
* ☁️ Cloud Deployment
* 📡 Public API

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first.

---

## 📜 License

This project is for educational purposes.

---

## 👩‍💻 Author

Shravani Shinde
