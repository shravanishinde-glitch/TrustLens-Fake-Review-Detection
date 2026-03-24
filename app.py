from flask import Flask, render_template, request, redirect, session, jsonify, flash, Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from datetime import datetime
from sqlalchemy import func
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import re
import joblib
import os
from dotenv import load_dotenv

# ---------------- LOAD ENV ----------------
load_dotenv()

# ---------------- APP SETUP ----------------
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")

# Ensure instance folder exists
os.makedirs(app.instance_path, exist_ok=True)

# Use SQLite (safe default)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ---------------- LOGIN MANAGER ----------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login_redirect'

# ---------------- SAFE MODEL LOADING ----------------
try:
    model = joblib.load("svm_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
except:
    model = None
    vectorizer = None
    print("⚠️ Model files not found. Run train_model.py first.")

# ---------------- DATABASE MODELS ----------------
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    role = db.Column(db.String(20), default="user")

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(500), default="")
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
    price = db.Column(db.Float, default=0.0)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    prediction = db.Column(db.String(10))
    confidence = db.Column(db.Float)
    trust_score = db.Column(db.Float)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# ---------------- CREATE TABLES ----------------
with app.app_context():
    db.create_all()

# ---------------- LOGIN LOADER ----------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ---------------- ROLE DECORATOR ----------------
def roles_required(*roles):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if 'role' not in session or session['role'] not in roles:
                return redirect('/login')
            return f(*args, **kwargs)
        return wrapped
    return decorator

# ---------------- ML FUNCTIONS ----------------
def calculate_trust_score(text, confidence):
    score = confidence
    score -= text.count("!") * 2
    score -= len(re.findall(r'\b[A-Z]{3,}\b', text)) * 3
    return max(0, min(100, score))

def model_predict(text):
    if not model or not vectorizer:
        return "Unknown", 50, 50
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0].capitalize()
    decision_score = model.decision_function(vec)[0]
    confidence = min(max(abs(decision_score) * 10, 50), 99)
    trust = calculate_trust_score(text, confidence)
    return pred, confidence, trust

# ---------------- ROUTES ----------------
@app.route('/')
def home():
    logout_user()
    session.clear()
    reviews = Review.query.order_by(Review.created_at.desc()).limit(5).all()
    return render_template("home.html", recent_reviews=reviews)

# -------- SIGNUP --------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])
        role = request.form.get('role', 'user')

        if User.query.filter_by(email=email).first():
            flash("Email already exists", "error")
            return redirect('/signup')

        user = User(name=name, email=email, password=password, role=role)
        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id
        session['role'] = role

        return redirect('/dashboard')

    return render_template("signup.html")

# -------- LOGIN --------
@app.route('/login/user', methods=['GET', 'POST'])
def login_user_route():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            session['user_id'] = user.id
            session['role'] = user.role
            return redirect('/dashboard')
        flash("Invalid credentials", "error")

    return render_template("login_user.html")

@app.route('/login')
def login_redirect():
    return redirect('/login/user')

# -------- LOGOUT --------
@app.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect('/')

# -------- DASHBOARD --------
@app.route('/dashboard')
@roles_required("user", "business", "admin")
def dashboard():
    products = Product.query.all()
    return render_template("user_dashboard.html", products=products)

# -------- SUBMIT REVIEW --------
@app.route('/submit/<int:product_id>', methods=['POST'])
def submit_review(product_id):
    text = request.form['review']
    pred, conf, trust = model_predict(text)

    review = Review(
        text=text,
        prediction=pred,
        confidence=conf,
        trust_score=trust,
        product_id=product_id
    )
    db.session.add(review)
    db.session.commit()

    return jsonify({
        "prediction": pred,
        "confidence": conf,
        "trust_score": trust
    })

# -------- SUPPORT FIX --------
@app.route('/submit_support_ticket', methods=['POST'])
def submit_support_ticket():
    try:
        data = request.get_json()
        return jsonify({'success': True})
    except Exception as e:
        print(e)
        return jsonify({'success': False}), 500

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)