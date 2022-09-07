cost_per_tile = 0.6 #60p
area_of_tile = 0.04 # 20cm by 20cm
width = float(input("Enter the width of the floor: "))
length = float(input("Enter the length of the floor: "))
area = width*length
num_of_tiles = (area+0.039)//area_of_tile
price = num_of_tiles*cost_per_tile
print("That will cost £"+str(round(price,2)))