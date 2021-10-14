print("Program Started")
print("Please enter an ASCII code:")
asc = int(input())
if asc in range(32, 126):
    char = chr(asc)
    print(f"The character represented by the ASCII code {asc} is {char}.")
else:
    print("Error!")
print("Program Ended")
