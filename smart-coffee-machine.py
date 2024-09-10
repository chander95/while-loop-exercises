coffee_resevior = 7
coffee_types = ["Americano", "Latte", "Cold Brew", "Red Eye", "Iced Coffee", "Mocha", "Espresso"]


while coffee_resevior > 0:
    selection = input("Which drink would you like? \n")
    print(coffee_types)
    if selection in coffee_types:
        coffee_types.remove(selection)
        print(f"You've selected {selection}. \n" )
        coffee_resevior -= 1
    else:
        print("Please select an item from our menu: \n")

print("We're unable to make anymore drinks today. Sorry!")