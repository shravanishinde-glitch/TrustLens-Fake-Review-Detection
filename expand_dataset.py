import pandas as pd
import random

# Read existing dataset
df = pd.read_csv('dataset/reviews.csv')
print(f"Original dataset size: {len(df)}")

# Real review templates
real_templates = [
    "This product is {adj} and works {adv} well. {detail} Very satisfied with my purchase.",
    "Great quality and {feature}. Would definitely recommend to others.",
    "Exactly as described. {positive_comment} Fast shipping too.",
    "Been using this for {time} and it's {adj}. No complaints at all.",
    "Good value for money. {specific_detail} Will buy again.",
    "The {feature} is impressive. {personal_experience} Worth every penny.",
    "Solid product. {practical_comment} Does what it says it does.",
    "Happy with this purchase. {usage_comment} Better than expected.",
    "Reliable and {adj}. {comparison} Highly recommend.",
    "Perfect for my needs. {specific_use} Excellent customer service too."
]

# Fake review templates (too perfect)
fake_perfect_templates = [
    "This product is absolutely fantastic and works perfectly in every situation. The quality is outstanding and the performance is excellent. I highly recommend this amazing product to everyone.",
    "Unbelievable quality! This is the best purchase I've ever made. Perfect in every way, exceeds all expectations. Five stars doesn't do it justice!",
    "Absolutely perfect! Nothing but praise for this incredible product. Works flawlessly, amazing quality, fantastic value. Must-have item!",
    "Outstanding performance! This product is simply exceptional. Perfect design, perfect function, perfect results. Highly impressed!",
    "Incredible value! This amazing product delivers perfection in every aspect. Outstanding quality, flawless performance, total satisfaction!"
]

# Fake review templates (contradictory)
fake_contradictory_templates = [
    "This product is terrible and doesn't work at all. However, I have to admit it has some minor uses. But overall, it's a complete waste of money.",
    "Worst purchase ever. The quality is awful and it broke immediately. Although I suppose it might work for some people, but not for me.",
    "Complete disappointment. Doesn't function properly at all. Despite this, I can see why some might like it, but it's not for me.",
    "Terrible product. Poor quality and doesn't meet expectations. But maybe it's okay for basic use, though I wouldn't recommend it.",
    "Awful experience. The item arrived damaged and doesn't work. However, the packaging was nice, but that's not enough to save it."
]

# Fake review templates (generic complaints)
fake_generic_templates = [
    "Does not work at all. Very bad quality. Complete waste of money. Total disappointment. Would not recommend.",
    "Poor quality product. Not good at all. Terrible performance. Waste of time and money. Stay away from this.",
    "Useless item. Doesn't function properly. Bad design. Awful customer service. Complete failure.",
    "Worst product ever. Breaks easily. Poor construction. Not worth the money. Total scam.",
    "Disappointing purchase. Doesn't work as advertised. Bad quality. Waste of money. Regret buying this."
]

# Word lists for templates
adjectives = ['good', 'excellent', 'great', 'amazing', 'wonderful', 'fantastic', 'superb', 'outstanding']
adverbs = ['really', 'very', 'quite', 'extremely', 'incredibly']
features = ['fast shipping', 'great customer service', 'excellent packaging', 'reliable performance']
details = ['Delivery was on time', 'Easy to use', 'Good customer support', 'Better than expected']
times = ['a week', 'a month', 'several weeks', 'a few months']

def generate_real_review():
    template = random.choice(real_templates)
    adj = random.choice(adjectives)
    adv = random.choice(adverbs)
    feature = random.choice(features)
    detail = random.choice(details)
    time = random.choice(times)
    positive_comment = random.choice(['Good value', 'Quality materials', 'Works as expected'])
    personal_experience = random.choice(['My experience has been positive', 'It exceeded my expectations'])
    practical_comment = random.choice(['Gets the job done', 'Reliable performance'])
    usage_comment = random.choice(['Easy to set up', 'Works perfectly'])
    comparison = random.choice(['Better than competitors', 'Much better than expected'])
    specific_use = random.choice(['Daily use', 'Professional work'])
    specific_detail = random.choice(['Durable materials', 'Good build quality'])

    review = template.format(
        adj=adj, adv=adv, feature=feature, detail=detail, time=time,
        positive_comment=positive_comment, personal_experience=personal_experience,
        practical_comment=practical_comment, usage_comment=usage_comment,
        comparison=comparison, specific_use=specific_use, specific_detail=specific_detail
    )
    return review

def generate_fake_reviews():
    review_type = random.choice(['perfect', 'contradictory', 'generic'])
    if review_type == 'perfect':
        return random.choice(fake_perfect_templates)
    elif review_type == 'contradictory':
        return random.choice(fake_contradictory_templates)
    else:
        return random.choice(fake_generic_templates)

# Generate additional reviews to reach 6000+ total
target_size = 7000  # Updated to 7000 total including header
current_size = len(df)

print(f"Current size: {current_size}, Target size: {target_size}")

new_reviews = []
while len(df) + len(new_reviews) < target_size:
    if random.random() < 0.5:
        review = generate_real_review()
        label = 'real'
    else:
        review = generate_fake_reviews()
        label = 'fake'

    new_reviews.append({'review': review, 'label': label})

# Add new reviews to dataframe
new_df = pd.DataFrame(new_reviews)
df_expanded = pd.concat([df, new_df], ignore_index=True)

# Shuffle the dataset
df_expanded = df_expanded.sample(frac=1, random_state=42).reset_index(drop=True)

print(f"Expanded dataset size: {len(df_expanded)}")
print(f"Real reviews: {len(df_expanded[df_expanded['label'] == 'real'])}")
print(f"Fake reviews: {len(df_expanded[df_expanded['label'] == 'fake'])}")

# Save expanded dataset
df_expanded.to_csv('dataset/reviews.csv', index=False)
print("✅ Dataset expanded and saved!")