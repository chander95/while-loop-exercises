#Once battery reaches 50%, it should begin to charge faster, when it hits 80%, it slows down to prevent overcharge

battery = 0

while battery < 100:
    if battery <= 80 and battery >= 50:
        battery += 5
        print(battery)
    elif battery >= 80 and battery < 100:
        battery += 0.5
        print(battery)
    else:
        battery += 1
        print(battery)
print("The battery is full!")
