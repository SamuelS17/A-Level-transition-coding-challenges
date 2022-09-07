logic_gate = input("Enter your logic gate: ")
nums = input("What are the two inputs: ")

if logic_gate.upper() == "OR":
  if nums == "00":
    print("This would output 0")
  else:
    print("This would output 1")

elif logic_gate.upper() == "AND":
  if nums == "11":
    print("This would output 1")
  else:
    print("This would output 0")

elif logic_gate.upper() == "XOR":
  if nums == "00" or "11":
    print("This would output 0")
  else:
    print("This would output 1")

elif logic_gate.upper() == "NAND":
  if nums == "11":
    print("This would output 0")
  else:
    print("This would output 1")

elif logic_gate.upper() == "NOR":
  if nums == "00":
    print("This would output 1")
  else:
    print("This would output 0")

else:
    print("That is not a gate that this program knows about")