time = float(input("Enter the time it took for the car to travel from the first camera to the second camera (in minutes): "))
num_plate = input("Enter the number plate: ")
distance = 1
time = time/60
speed = round(distance/time, 2)
print("The car is travelling at", str(speed)+"mph")

f = open("speeding_cars.txt", "a")
if speed >70:
    f.write(num_plate)
    f.write("\n")
    print("This car has broken the speed limit!")
f.close()