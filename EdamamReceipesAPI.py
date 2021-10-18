import requests

app_id = "aa36195e"
app_key = "120f3a085ddcfa5812357168370f6bc1"


def simple_search(app_id, app_key):
    ingredient = input('What ingredient are you looking for? ')
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    response = requests.get(url)
    parsed_result = response.json()

    print('The following result match your search query: ')

    for recipe in parsed_result['hits']:
        recipe = recipe['recipe']
        print(recipe['label'], ': ', recipe['url'])


def advanced_search(app_id, app_key):
    ingredient = input('What ingredient are you looking for? ')
    diet = input('What diet type the receipe should be? Select one of the following: ALL, BALANCED, HIGH-FIBER, HIGH-PROTEIN, LOW-CARB, LOW-FAT, LOW-SODIUM: ')
    health = input('What health type? ALL, VEGETARIAN, VEGAN, WHEAT-FREE, PEANUT-FREE, GLUTEN-FREE: ')
    cuisineType = input('What cuisine are you interested in? ALL, ASIAN, CHINESE, ITALIAN, KOSHER, MEXICAN: ')
    mealType = input('What type of meal is it? ALL, BREAKFAST, DINNER, LUNCH, SNACK, TEATIME: ')
    calories = input('How many calories should your meal have? e.g. 300-600: ')

    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)

    if diet != 'all':
        diet_url = '&diet={}'.format(diet)
        url = url + diet_url

    if health != 'all':
        health_url = '&health={}'.format(health)
        url = url + health_url

    if cuisineType != 'all':
        cuisineType_url = '&cuisineType={}'.format(cuisineType)
        url = url + cuisineType_url

    if mealType != 'all':
        mealType_url = '&mealType={}'.format(mealType)
        url = url + mealType_url

    calories_url = '&calories={}'.format(calories)
    url = url + calories_url

    response = requests.get(url)
    parsed_result = response.json()

    print(url)

    if len(parsed_result['hits']) != 0:
        print('The following result match your search query: ')

        for recipe in parsed_result['hits']:
            recipe = recipe['recipe']
            print(recipe['label'], ': ', recipe['url'])
    else:
        print('Your search query did not return any results :( Try again!')


simple_or_advanced = input('Would you like to run a simple or advanced receipt search? (S or A?) ')
if simple_or_advanced == 'S' or simple_or_advanced == 's':
    simple_search(app_id, app_key)
elif simple_or_advanced == 'A' or simple_or_advanced == 'a':
    advanced_search(app_id, app_key)
else:
    print('Wrong input :(')
