num_of_positions = int(input("Enter the number of items in the sequence: "))
def fibonacci_sequence(positions):
  sequence = ''
  x,y,z = 1,1,0
  sequence+= str(x)+', '+str(y)
  for i in range(0,positions-2):
    z=x+y
    sequence += ', '+str(z)
    x=y
    y=z
  return sequence

print(fibonacci_sequence(num_of_positions))