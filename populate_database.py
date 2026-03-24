from app import app, db, User, Company, Product, Review
from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import random

def populate_database():
    """
    Populate the database with comprehensive test data
    """
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        print("✓ Database tables created successfully")

        # ============ CREATE USERS ============
        print("\n--- Creating Users ---")
        
        # Regular Users
        regular_users = [
            User(name="John Smith", email="john@example.com", password=generate_password_hash("password"), role="user"),
            User(name="Sarah Johnson", email="sarah@example.com", password=generate_password_hash("password"), role="user"),
            User(name="Michael Brown", email="michael@example.com", password=generate_password_hash("password"), role="user"),
            User(name="Jessica Lee", email="jessica@example.com", password=generate_password_hash("password"), role="user"),
            User(name="David Wilson", email="david@example.com", password=generate_password_hash("password"), role="user"),
            User(name="Emily Martinez", email="emily@example.com", password=generate_password_hash("password"), role="user"),
            User(name="Robert Taylor", email="robert@example.com", password=generate_password_hash("password"), role="user"),
            User(name="Laura Anderson", email="laura@example.com", password=generate_password_hash("password"), role="user"),
            User(name="James Thomas", email="james@example.com", password=generate_password_hash("password"), role="user"),
            User(name="Patricia Jackson", email="patricia@example.com", password=generate_password_hash("password"), role="user"),
        ]
        
        # Business Users
        business_users = [
            User(name="Alex Williams", email="alex@business.com", password=generate_password_hash("password123"), role="business"),
            User(name="Emma Davis", email="emma@business.com", password=generate_password_hash("password123"), role="business"),
            User(name="Chris Kumar", email="chris@business.com", password=generate_password_hash("password123"), role="business"),
            User(name="Rebecca White", email="rebecca@business.com", password=generate_password_hash("password123"), role="business"),
        ]
        
        # Admin User
        admin_user = User(
            name="Admin",
            email="admin@trustlens.com",
            password=generate_password_hash("admin123"),
            role="admin"
        )
        
        all_users = regular_users + business_users + [admin_user]
        db.session.add_all(all_users)
        db.session.commit()
        print(f"✓ {len(all_users)} Users created (10 regular, 4 business, 1 admin)")

        # ============ CREATE COMPANIES ============
        print("\n--- Creating Companies ---")
        
        # Create Companies
        companies = [
            Company(name="TechGear Solutions", owner_id=business_users[0].id),
            Company(name="Fashion Plus Ltd", owner_id=business_users[1].id),
            Company(name="Home Essentials Inc", owner_id=business_users[2].id),
            Company(name="Beauty & Wellness Co", owner_id=business_users[3].id),
        ]
        
        db.session.add_all(companies)
        db.session.commit()
        print(f"✓ {len(companies)} Companies created")

        # ============ CREATE PRODUCTS ============
        print("\n--- Creating Products ---")
        
        # TechGear Solutions Products
        products_techgear = [
            Product(name="Wireless Bluetooth Headphones", description="Premium noise-cancelling wireless headphones with 30-hour battery life", company_id=companies[0].id, price=129.99),
            Product(name="USB-C Fast Charger", description="65W fast charging adapter compatible with laptops and phones", company_id=companies[0].id, price=49.99),
            Product(name="Mechanical Gaming Keyboard", description="RGB mechanical keyboard with customizable switches", company_id=companies[0].id, price=149.99),
            Product(name="4K Webcam", description="Ultra HD webcam for streaming and professional video calls", company_id=companies[0].id, price=199.99),
            Product(name="Portable SSD 1TB", description="Ultra-fast external solid state drive for data transfer", company_id=companies[0].id, price=99.99),
            Product(name="Laptop Stand", description="Adjustable aluminum laptop stand for better ergonomics", company_id=companies[0].id, price=34.99),
        ]
        
        # Fashion Plus Products
        products_fashion = [
            Product(name="Cotton T-Shirt", description="Organic cotton t-shirts available in multiple colors", company_id=companies[1].id, price=29.99),
            Product(name="Denim Jeans", description="Classic blue denim jeans with premium fit", company_id=companies[1].id, price=79.99),
            Product(name="Leather Jacket", description="Genuine leather jacket for all seasons", company_id=companies[1].id, price=199.99),
            Product(name="Athletic Sneakers", description="Comfortable running shoes with cushioned sole", company_id=companies[1].id, price=119.99),
            Product(name="Wool Sweater", description="Cozy merino wool winter sweater", company_id=companies[1].id, price=89.99),
            Product(name="Summer Dress", description="Lightweight breathable summer dress perfect for warm weather", company_id=companies[1].id, price=59.99),
        ]
        
        # Home Essentials Products
        products_home = [
            Product(name="Cotton Bed Sheets Set", description="Premium Egyptian cotton bed sheets set with deep pockets", company_id=companies[2].id, price=69.99),
            Product(name="Stainless Steel Cookware Set", description="Professional 10-piece cookware set with non-stick coating", company_id=companies[2].id, price=129.99),
            Product(name="LED Smart Bulbs", description="WiFi-enabled RGB LED bulbs with app control", company_id=companies[2].id, price=39.99),
            Product(name="Air Purifier", description="HEPA filter air purifier removes dust, pollen, and allergens", company_id=companies[2].id, price=159.99),
            Product(name="Coffee Maker", description="Programmable coffee maker with thermal carafe", company_id=companies[2].id, price=79.99),
            Product(name="Desk Lamp", description="Adjustable LED desk lamp with USB charging port", company_id=companies[2].id, price=49.99),
        ]
        
        # Beauty & Wellness Products
        products_beauty = [
            Product(name="Organic Face Serum", description="Anti-aging face serum with Vitamin C and hyaluronic acid", company_id=companies[3].id, price=34.99),
            Product(name="Moisturizing Cream", description="Rich healing moisturizer for dry skin", company_id=companies[3].id, price=44.99),
            Product(name="Yoga Mat", description="Non-slip eco-friendly yoga mat 6mm thickness", company_id=companies[3].id, price=29.99),
            Product(name="Protein Powder", description="Whey protein powder with natural vanilla flavor", company_id=companies[3].id, price=39.99),
            Product(name="Fitness Tracker", description="Waterproof fitness tracker with heart rate monitor", company_id=companies[3].id, price=99.99),
            Product(name="Aromatherapy Diffuser", description="Ultrasonic essential oil diffuser with LED lights", company_id=companies[3].id, price=34.99),
        ]
        
        all_products = products_techgear + products_fashion + products_home + products_beauty
        db.session.add_all(all_products)
        db.session.commit()
        print(f"✓ {len(all_products)} Products created (6 TechGear, 6 Fashion, 6 Home, 6 Beauty)")

        # ============ CREATE REVIEWS ============
        print("\n--- Creating Reviews ---")
        
        # Sample review texts for authentic data
        real_reviews = [
            "Excellent product! Great quality and fast shipping. Highly recommend.",
            "Really happy with my purchase. It works exactly as described.",
            "Best value for money. Great customer service too.",
            "Absolutely love it! Better than expected.",
            "Very satisfied with this purchase. Great build quality.",
            "Fantastic product. Arrived quickly and in perfect condition.",
            "Perfect! Exactly what I was looking for.",
            "High quality and durable. Worth every penny.",
            "Amazing service and great product quality.",
            "This is the best purchase I've made in a while.",
            "Surpassed all my expectations. Highly satisfied!",
            "Outstanding quality and excellent delivery service.",
            "Five stars all the way! Recommend to everyone.",
            "Great product, great price, great service.",
            "Couldn't be happier with my purchase.",
            "This product has changed my life for the better.",
            "Exactly as pictured and described. Very happy.",
            "Best investment I've made. Works wonderfully.",
            "Professional quality at an affordable price.",
            "Impressed with the durability and performance.",
        ]
        
        fake_reviews = [
            "This is the BEST PRODUCT EVER!!! EVERYONE MUST BUY NOW!!!",
            "I don't own this but heard it's amazing 5 stars!!!",
            "SCAM SCAM SCAM DO NOT BUY GET BETTER PRODUCT!!!",
            "WORST EVER TOTAL GARBAGE DO NOT WASTE MONEY",
            "My friend's cousin's uncle says this is fake buy PREMIUM instead",
            "BUY BUY BUY NOW NOW NOW BEST DEAL EVER!!!",
            "Not real product cheap junk definitely scam AVOID",
            "CHECK THIS INCREDIBLE DEAL LINK IN PROFILE",
            "ABSOLUTELY AMAZING PRODUCT BEST IN MARKET",
            "DO NOT BELIEVE OTHER REVIEWS THIS IS FAKE",
            "FAKE NEWS FAKE PRODUCT DONT TRUST THEM",
            "Only idiots would buy this, get my link instead!!!",
            "This company SUCKS buy from MY competitor NOW",
            "UNBELIEVABLE PRICE YOU WONT FIND ANYWHERE ELSE",
            "DONT BUY SUPER DANGEROUS MANY INJURIES REPORTED",
            "EXPOSED: Company hiding WORST SECRET about this item",
            "celebrities are using FAKE reviews HERE IS TRUTH",
            "THIS WILL CHANGE YOUR LIFE CLICK HERE FOR 70% OFF",
            "Government BANS this specific product because DANGEROUS",
            "I BOUGHT 100 ALREADY SO EFFECTIVE AND CHEAP",
        ]
        
        reviews = []
        
        # Add reviews for all products
        for product in all_products:
            num_reviews = random.randint(8, 15)
            for i in range(num_reviews):
                is_real = random.choices([True, False], weights=[75, 25])[0]  # 75% real, 25% fake
                review_text = random.choice(real_reviews if is_real else fake_reviews)
                
                if is_real:
                    confidence = random.uniform(75, 99)
                    trust_score = random.uniform(70, 95)
                else:
                    confidence = random.uniform(60, 85)
                    trust_score = random.uniform(15, 45)
                
                review = Review(
                    text=review_text,
                    prediction="Real" if is_real else "Fake",
                    confidence=round(confidence, 2),
                    trust_score=round(trust_score, 2),
                    product_id=product.id,
                    created_at=datetime.utcnow() - timedelta(days=random.randint(1, 90))
                )
                reviews.append(review)
        
        db.session.add_all(reviews)
        db.session.commit()
        print(f"✓ {len(reviews)} Reviews created")

        # ============ SUMMARY ============
        print("\n" + "="*60)
        print("DATABASE POPULATION COMPLETE!")
        print("="*60)
        print("\n📊 DATABASE SUMMARY:")
        print(f"  • Users: {len(all_users)} (10 regular users, 4 business owners, 1 admin)")
        print(f"  • Companies: {len(companies)}")
        print(f"  • Products: {len(all_products)}")
        print(f"  • Reviews: {len(reviews)}")
        
        print("\n👤 TEST ACCOUNTS - Regular Users:")
        print("    • john@example.com / password123")
        print("    • sarah@example.com / password123")
        print("    • michael@example.com / password123")
        print("    • jessica@example.com / password123")
        print("    • david@example.com / password123")
        print("    • emily@example.com / password123")
        print("    • robert@example.com / password123")
        print("    • laura@example.com / password123")
        print("    • james@example.com / password123")
        print("    • patricia@example.com / password123")
        
        print("\n👤 TEST ACCOUNTS - Business Owners:")
        print("    • alex@business.com / password123 (TechGear Solutions)")
        print("    • emma@business.com / password123 (Fashion Plus Ltd)")
        print("    • chris@business.com / password123 (Home Essentials Inc)")
        print("    • rebecca@business.com / password123 (Beauty & Wellness Co)")
        
        print("\n👤 TEST ACCOUNTS - Admin:")
        print("    • admin@trustlens.com / admin123")
        
        print("\n🏢 COMPANIES & PRODUCTS:")
        print("\n  1️⃣ TechGear Solutions (Owner: alex@business.com)")
        print("     • Wireless Bluetooth Headphones - $129.99")
        print("     • USB-C Fast Charger - $49.99")
        print("     • Mechanical Gaming Keyboard - $149.99")
        print("     • 4K Webcam - $199.99")
        print("     • Portable SSD 1TB - $99.99")
        print("     • Laptop Stand - $34.99")
        
        print("\n  2️⃣ Fashion Plus Ltd (Owner: emma@business.com)")
        print("     • Cotton T-Shirt - $29.99")
        print("     • Denim Jeans - $79.99")
        print("     • Leather Jacket - $199.99")
        print("     • Athletic Sneakers - $119.99")
        print("     • Wool Sweater - $89.99")
        print("     • Summer Dress - $59.99")
        
        print("\n  3️⃣ Home Essentials Inc (Owner: chris@business.com)")
        print("     • Cotton Bed Sheets Set - $69.99")
        print("     • Stainless Steel Cookware Set - $129.99")
        print("     • LED Smart Bulbs - $39.99")
        print("     • Air Purifier - $159.99")
        print("     • Coffee Maker - $79.99")
        print("     • Desk Lamp - $49.99")
        
        print("\n  4️⃣ Beauty & Wellness Co (Owner: rebecca@business.com)")
        print("     • Organic Face Serum - $34.99")
        print("     • Moisturizing Cream - $44.99")
        print("     • Yoga Mat - $29.99")
        print("     • Protein Powder - $39.99")
        print("     • Fitness Tracker - $99.99")
        print("     • Aromatherapy Diffuser - $34.99")
        
        print("\n✅ Database ready for use!")
        print("="*60)

if __name__ == "__main__":
    populate_database()
