def make_car(brand, model, **car_info):
    car_info['car_brand'] = brand
    car_info['car_model'] = model
    return(car_info)

car = make_car('subaru','outback',color='blue',tow_package='true')
print(car)


