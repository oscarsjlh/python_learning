def make_shirt(size, message):
    """display information about a shirt"""
    message = f"This shirt is {size.title()}, and it has the follwoing message: \"{message.title()}\" on it."
    print(message)

make_shirt('small','hail satan')
make_shirt(size='big', message='american burger')
make_shirt(message='blabla',size='medium')



