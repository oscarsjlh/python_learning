def car_info(manufacturer, model, **other):
    other['manufacturer'] = manufacturer
    other['model'] = model
    return other

car = car_info('subaru', 'outback',color='blue',tow_package=True)
print(car)
