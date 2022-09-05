def tshirt(size, text):
    
    if size == 'large':
        text = "I love python!"
    print(f"The shirt is {size} and has {text} written on it")


tshirt('big', 'dong')
tshirt('small', 'bum')
tshirt(text='dong', size='big')
tshirt(text='bum', size='small')
