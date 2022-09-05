cities = {
    'london': {
        'population': 'too many',
        'country': 'united kingdom',
        'fact': 'it\'s used for money laundering',
        },
    'lleida':{
        'population': 'some people',
        'country': 'spain',
        'fact': 'i grew up there',
        },
    'helsink':{
        'population': 'quite a bit',
        'country': 'finland',
        'fact': 'is fucking cold',
        },
            }

for city, city_info in cities.items():
    country = f"{city_info['country']}"
    fact = f"{city_info['fact']}"
    print(f"{city.title()} Is located in {country.title()} {fact.title()}")

