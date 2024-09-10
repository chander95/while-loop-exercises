coffee_types = ["Americano", "Latte", "Cold Brew", "Red Eye", "Iced Coffee", "Mocha", "Espresso"]
coffee_resevior = len(coffee_types)


while coffee_resevior > 0:
    print(coffee_types)
    selection = input("Which drink would you like? ")
    if selection in coffee_types:
        coffee_types.remove(selection)
        print(f"You've selected {selection}. \n" )
        coffee_resevior -= 1
    else:
        print("Please select an item from our menu: \n")

print("We're unable to make anymore drinks today. Sorry!")
