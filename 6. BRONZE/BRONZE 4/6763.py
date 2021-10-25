limit = int(input())
velocity = int(input())
speeding = velocity - limit

if speeding <= 0:
    print("Congratulations, you are within the speed limit!")
else:
    if speeding <= 20:
        fine = 100
    elif speeding <= 30:
        fine = 270
    else:
        fine = 500
    print(f"You are speeding and your fine is ${fine}.")
