from flask import Flask, render_template, request

app = Flask(__name__)

# Sample recipe data
recipes = [
    {
        "name": "Pasta Primavera",
        "ingredients": ["pasta", "tomato", "spinach", "garlic", "olive oil"]
    },
    {
        "name": "Vegetable Stir Fry",
        "ingredients": ["broccoli", "carrot", "bell pepper", "soy sauce", "garlic"]
    },
    {
        "name": "Tomato Soup",
        "ingredients": ["tomato", "onion", "garlic", "olive oil", "basil"]
    },
    {
        "name": "Garlic Bread",
        "ingredients": ["bread", "garlic", "butter", "parsley"]
    }
]

# Home route to display the input form
@app.route('/')
def home():
    return render_template('index.html')

# Route to process the available ingredients and recommend recipes
@app.route('/recommend', methods=['POST'])
def recommend():
    # Get ingredients from the form
    available_ingredients = request.form.get('ingredients').lower().split(',')
    available_ingredients = [ingredient.strip() for ingredient in available_ingredients]

    # Debugging statement
    print(f"Available ingredients: {available_ingredients}")

    # Find matching recipes (Check if at least one ingredient in the recipe matches the available ingredients)
    recommended_recipes = []
    for recipe in recipes:
        if any(ingredient in available_ingredients for ingredient in recipe['ingredients']):
            recommended_recipes.append(recipe)
    
    # Debugging statement
    print(f"Recommended recipes: {recommended_recipes}")

    # Return the results page
    return render_template('result.html', recipes=recommended_recipes)

if __name__ == '__main__':
    app.run(debug=True)