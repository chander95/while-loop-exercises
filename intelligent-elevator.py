#Building has 9 floors
current_floor = 9
floors_requested = [2,5,8]

#desired_floors = int(input("Pick a floor: "))
#floors_requested.append(desired_floors)

while current_floor > 1:
    print(f"We are now on level {current_floor}")
    if current_floor in floors_requested:
        floors_requested.remove(current_floor)
        print(f"We have arrived at your desired floor.")
    current_floor -= 1
    if current_floor == 1:
        print(f"We have reached the ground level.")

