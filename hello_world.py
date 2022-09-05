names = ', 'frodo', 'gandalf', 'golum']
names[3] =""
#print(f"Hello {names[0]} come to dinner")
#print(some text)
#print(f"Hello {} come to dinner")
#print(f"Hello {names[3]} come to dinner")
#print("Found a bigger table")
names.insert(0,'legolas')
names.insert(2,'boromir')
names.append('faramir')

print(f"Hello {names[0]} come to dinner")
print(f"Hello {names[1]} come to dinner")
print(f"Hello {names[2]} come to dinner")
print(f"Hello {names[3]} come to dinner")
print(f"Hello {names[4]} come to dinner")
print(f"Hello {names[5]} come to dinner")
print(f"Hello {names[6]} come to dinner")
uninvited1= names.pop()
print(f"Hello {uninvited1} please no longer come")
uninvited2= names.pop()
print(f"Hello {uninvited2} please no longer come")
uninvited3= names.pop()
print(f"Hello {uninvited3} please no longer come")
uninvited4= names.pop()
print(f"Hello {uninvited4} please no longer come")
uninvited5= names.pop()
print(f"Hello {uninvited5} please no longer come")
print(f"{names[0]}{names[1]} you guys are still invited to come")
del names[0]
del names[0]
print(names)
print(names)



||
