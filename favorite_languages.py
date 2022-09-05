favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

poll_takers =['mizmor','harry','valentine','elliot','phil','edward']
for poll_taker in poll_takers:
    if poll_taker not in favorite_languages.keys():
        print(f"{poll_taker} please fill the form\n")
    else:
        print(f"{poll_taker} thanks for filling the form\n")

