traffic_light_colors = ["green", "yellow", "red"]
green_light_count = 0

while green_light_count < 6:
    for color in traffic_light_colors:
        print(f"The light is now {color}")
        if color == "green":
            green_light_count += 1
print("The traffic light is now closed for maintenance")
