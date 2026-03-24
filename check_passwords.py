from app import app, User
from werkzeug.security import check_password_hash

with app.app_context():
    emails = ['john@example.com', 'alex@business.com', 'admin@trustlens.com']
    for email in emails:
        user = User.query.filter_by(email=email).first()
        print('\nChecking', email, '->', 'found' if user else 'missing')
        if user:
            for pwd in ['password', 'password123', 'admin123']:
                print('   test', pwd, '=>', check_password_hash(user.password, pwd))
