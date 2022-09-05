sandwich_orders = ['blt','veggie','sausage','hummus','pastrami','pastrami','pastrami']
finished_order = []
print("Unfortanetly no pastrami today")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I've made {current_order}")

for sandwich in finished_order:
    print(f"I've made {sandwich}")

print("All sandwich are done")
