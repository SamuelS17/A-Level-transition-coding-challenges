num = int(input("Enter a denrary number: "))
base = int(input("Enter the base you would like to convert to (2,8,16):"))
if base == 16:
  hexa = hex(num)
  print(hexa[2:])
elif base == 2:
  binary = bin(num)
  print(binary[2:])
elif base == 8:
  octa = oct(num)
  print(octa[2:])