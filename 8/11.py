def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last name'] = last
    return user_info

user_profile = build_profile('albert','einstein',location='princeton', field='physics')
oscar=build_profile('oscar','aranega',passion='computers',loves='valentine')
print(user_profile)
print(oscar)
