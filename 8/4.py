def make_shirt(size='large', message='I love python!'):
    """display information about a shirt"""
    message = f"This shirt is {size.title()}, and it has the follwoing message: \"{message.title()}\" on it."
    print(message)

make_shirt()
make_shirt('small')
make_shirt(size='large',message='but but crustaceans!')

