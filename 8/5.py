def describe_city(name, country='united kingdom'):
    """Define a a city with a country name on it"""
    message = f"{name.title()}, is in {country.title()}"
    print(message)

describe_city('london')
describe_city('edinburgh')
describe_city('valencia', country='spain')
describe_city('Dublin', 'Ireland')

