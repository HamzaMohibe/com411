print("Program Started")
print("Please enter a standard character")
char = input()
if len(char) == 1:
    asc = ord(char)
    print(f"The ASCII code for {char} is {asc}.")
else:
    print("Error!")
print("Program Ended!")

