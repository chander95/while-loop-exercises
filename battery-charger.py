#Once battery reaches 50%, it should begin to charge faster, when it hits 80%, it slows down to prevent overcharge

battery = 0
increment = 1

while battery < 100:
    battery += increment
    print(f"{battery}%")
    if battery == 50:
        increment = 15
        print(f"Efficiency check: Fast charging enabled.")
        #print(f"{battery}%")
    elif battery == 80:
        increment = 0.5
        print(f"Efficiency check: Slowing down charge to prevent overcharging.")
        #print(f"{battery}%")
    # else:
    #     battery += 1
    #     print(f"{battery}%")
print("The battery is fully charged.")
