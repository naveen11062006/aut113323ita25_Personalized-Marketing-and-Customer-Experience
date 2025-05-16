# Personalized product recommendation based on user purchase history
user_history = ['phone', 'charger', 'headphones']
product_catalog = {
    'phone': ['screen protector', 'phone case'],
    'charger': ['power bank'],
    'headphones': ['earbuds', 'wireless adapter']
}

def recommend(user_history):
    recommendations = []
    for item in user_history:
        recommendations += product_catalog.get(item, [])
    return set(recommendations)

print("Recommended Products:", recommend(user_history))
