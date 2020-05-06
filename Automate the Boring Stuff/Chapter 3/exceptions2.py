print("How many cats do you have?")
numCats = input()
try:
    if int(numCats) >= 4:
        print("That is a lot of cats.")
    elif int(numCats) == 0: 
        print("No cats? Shame!")
    elif int(numCats) < 0:
        print("Did you kill one or more cats you owned?")
    else:
        print("That is not many cats.")
except ValueError:
    print("You did not enter a number")
