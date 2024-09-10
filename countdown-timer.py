time = int(input("How many seconds would you like to countdown? "))

while time != 0:
    time -= 1
    print(time)
    if time == 0:
        print("Time is up!")