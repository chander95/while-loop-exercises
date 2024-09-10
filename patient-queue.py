patients = 12

while patients != 0:
    print("Next patient!")
    patients -= 1
    print(f"{patients} patients are still in the queue.")
    if patients == 0:
        print("The queue is clear. Great job!")