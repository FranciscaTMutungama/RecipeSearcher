import requests


def recipe_search(ingredient, app_id, app_key):
    # Make a request to the Edamam API
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient,app_id, app_key)
    )
    data = result.json()
    return data['hits']


def get_user_input():

    # Ask the user to enter an ingredient
    ingredient = input('Enter an ingredient: ')
    allergy = input('Enter any allergies (optional): ')
    meal_type = input('Enter preferred meal type (e.g., breakfast, lunch, dinner, snack - optional): ')
    cuisine = input('Enter preferred cuisine (e.g., Italian, Indian, Chinese - optional): ')
    return ingredient, allergy, meal_type, cuisine

def display_recipes(recipes):
    # Display the recipes for each search result
    for result in recipes:
        recipe = result['recipe']
        print("Recipe: {}".format(recipe["label"]))
        print("URl : {}".format(recipe["url"]))
        print()
