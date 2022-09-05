message = "How manny people in the booking "
people = input(message)
people = int(people)

if people > 8:
    print("We don't have an avalible table please wait")
else:
    print("Please take a seat")

