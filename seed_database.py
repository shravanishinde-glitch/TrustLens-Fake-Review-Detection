"""
Database seeding script to populate the database with sample data.
Run this after training the model to populate the app with realistic data.
"""

from app import app, db, User, Company, Product, Review
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random

def seed_database():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        print("Database cleared and recreated")

        # ============ CREATE USERS ============
        users_data = [
            # Regular Users
            {"name": "John Doe", "email": "john@example.com", "password": "password", "role": "user"},
            {"name": "Jane Smith", "email": "jane@example.com", "password": "password", "role": "user"},
            {"name": "Mike Johnson", "email": "mike@example.com", "password": "password", "role": "user"},
            {"name": "Emma Davis", "email": "emma@example.com", "password": "password", "role": "user"},
            {"name": "David Wilson", "email": "david@example.com", "password": "password", "role": "user"},
            {"name": "Sarah Martinez", "email": "sarah.m@example.com", "password": "password", "role": "user"},
            {"name": "Robert Anderson", "email": "robert@example.com", "password": "password", "role": "user"},
            {"name": "Lisa Thompson", "email": "lisa@example.com", "password": "password", "role": "user"},
            {"name": "James Garcia", "email": "james@example.com", "password": "password", "role": "user"},
            {"name": "Maria Rodriguez", "email": "maria@example.com", "password": "password", "role": "user"},
            
            # Business Users
            {"name": "Sarah Williams", "email": "sarah@example.com", "password": "password", "role": "business"},
            {"name": "Alex Brown", "email": "alex@example.com", "password": "password", "role": "business"},
            {"name": "Michael Zhang", "email": "michael@example.com", "password": "password", "role": "business"},
            {"name": "Jennifer Lee", "email": "jennifer@example.com", "password": "password", "role": "business"},
            {"name": "Christopher Paul", "email": "christopher@example.com", "password": "password", "role": "business"},
            {"name": "Diana Murphy", "email": "diana@example.com", "password": "password", "role": "business"},
        ]

        users = []
        for user_data in users_data:
            user = User(
                name=user_data["name"],
                email=user_data["email"],
                password=generate_password_hash(user_data["password"]),
                role=user_data["role"]
            )
            db.session.add(user)
            users.append(user)
        
        db.session.commit()
        print(f"✅ Created {len(users)} users")

        # ============ CREATE COMPANIES ============
        business_users = [u for u in users if u.role == "business"]
        
        companies_data = [
            {"name": "TechGear Pro", "owner_id": business_users[0].id},
            {"name": "ElectroHub", "owner_id": business_users[1].id},
            {"name": "SmartHome Solutions", "owner_id": business_users[2].id},
            {"name": "DigitalFirst Store", "owner_id": business_users[3].id},
            {"name": "Premium Electronics", "owner_id": business_users[4].id},
            {"name": "TechWorld Retail", "owner_id": business_users[5].id},
        ]

        companies = []
        for company_data in companies_data:
            company = Company(
                name=company_data["name"],
                owner_id=company_data["owner_id"]
            )
            db.session.add(company)
            companies.append(company)
        
        db.session.commit()
        print(f"✅ Created {len(companies)} companies")

        # ============ CREATE PRODUCTS ============
        products_data = [
            # TechGear Pro products
            {"name": "Wireless Headphones", "company_id": companies[0].id, "price": 79.99},
            {"name": "USB-C Cable Pro", "company_id": companies[0].id, "price": 19.99},
            {"name": "Phone Screen Protector", "company_id": companies[0].id, "price": 9.99},
            
            # ElectroHub products
            {"name": "Power Bank 20000mAh", "company_id": companies[1].id, "price": 39.99},
            {"name": "USB Hub 7-Port", "company_id": companies[1].id, "price": 34.99},
            {"name": "Smart LED Bulb", "company_id": companies[1].id, "price": 24.99},
            
            # SmartHome Solutions products
            {"name": "Smart Door Lock", "company_id": companies[2].id, "price": 149.99},
            {"name": "WiFi Thermostat", "company_id": companies[2].id, "price": 99.99},
            {"name": "Smart Camera", "company_id": companies[2].id, "price": 89.99},
            
            # DigitalFirst Store products
            {"name": "Portable SSD 1TB", "company_id": companies[3].id, "price": 119.99},
            {"name": "Wireless Mouse", "company_id": companies[3].id, "price": 44.99},
            {"name": "Mechanical Keyboard", "company_id": companies[3].id, "price": 129.99},
            
            # Premium Electronics products
            {"name": "Laptop Stand", "company_id": companies[4].id, "price": 49.99},
            {"name": "Monitor Light Bar", "company_id": companies[4].id, "price": 69.99},
            {"name": "USB-C Dock", "company_id": companies[4].id, "price": 89.99},
            
            # TechWorld Retail products
            {"name": "Portable Charger", "company_id": companies[5].id, "price": 29.99},
            {"name": "Phone Tripod Stand", "company_id": companies[5].id, "price": 19.99},
            {"name": "Ring Light", "company_id": companies[5].id, "price": 34.99},
        ]

        products = []
        for product_data in products_data:
            product = Product(
                name=product_data["name"],
                company_id=product_data["company_id"],
                price=float(product_data["price"])
            )
            db.session.add(product)
            products.append(product)
        
        db.session.commit()
        print(f"✅ Created {len(products)} products")

        # ============ CREATE REVIEWS ============
        real_reviews = [
            "Great product excellent quality and fast shipping",
            "Very satisfied with this purchase works perfectly",
            "Exceeded expectations outstanding product",
            "Best value for money highly recommend",
            "Perfect fit exactly as described",
            "Excellent quality great customer service",
            "Worth every penny love this item",
            "Amazing purchase very impressed",
            "Outstanding quality highly recommend",
            "Fantastic product great service",
            "Perfect quality excellent value",
            "Great design excellent construction",
            "Excellent purchase very satisfied",
            "Amazing product perfect fit",
            "Outstanding highly recommend",
            "Great quality reliable product",
            "Highly recommend excellent product",
            "Love this item perfect solution",
            "Best purchase excellent quality",
            "Fantastic product great value",
        ]

        fake_reviews = [
            "Worst product ever complete waste of money",
            "Best buy must have now unbelievable deal",
            "Absolutely fantastic unbelievable quality",
            "Complete scam do not waste your money",
            "Terrible quality broke after one week",
            "Waste of money poor quality materials",
            "Total junk save your money look elsewhere",
            "Absolutely useless just returned it",
            "Defective and unreliable waste of cash",
            "Rubbish quality worst purchase ever",
            "Totally broken completely unusable",
            "Worst thing I bought this year",
            "Cheap junk quality is awful",
            "Falling apart poor quality design",
            "Fraud not as described at all",
            "Not worth the money cheap quality",
            "Defects everywhere poor manufacturing",
            "Garbage product false advertising",
            "Unreliable breaks easily poor quality",
            "Completely broken not as advertised",
        ]

        reviews = []
        base_date = datetime.utcnow()

        for product in products:
            # Add 20-40 reviews per product for more data
            num_reviews = random.randint(20, 40)
            
            for i in range(num_reviews):
                is_real = random.random() > 0.3  # 70% real, 30% fake
                review_text = random.choice(real_reviews) if is_real else random.choice(fake_reviews)
                
                # Simulate confidence scores
                confidence = random.uniform(0.75, 0.99) if is_real else random.uniform(0.60, 0.95)
                trust_score = confidence - (random.uniform(0, 0.2) if not is_real else random.uniform(0, 0.1))
                
                review = Review(
                    text=review_text,
                    product_id=product.id,
                    prediction="Real" if is_real else "Fake",
                    confidence=round(confidence, 3),
                    trust_score=round(trust_score, 3),
                    created_at=base_date - timedelta(days=random.randint(0, 90))
                )
                db.session.add(review)
                reviews.append(review)
        
        db.session.commit()
        print(f"✅ Created {len(reviews)} reviews")

        print("\n" + "="*50)
        print("Database seeding completed successfully!")
        print("="*50)
        print(f"\nSummary:")
        print(f"  Users: {len(users)}")
        print(f"  Companies: {len(companies)}")
        print(f"  Products: {len(products)}")
        print(f"  Reviews: {len(reviews)}")
        print(f"\nYou can now login with:")
        print(f"  User: john@example.com / password123")
        print(f"  Business: sarah@example.com / password123")


if __name__ == "__main__":
    seed_database()
