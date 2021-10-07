count1 = 0
count2 = 0
print("Please enter the first whole number.")
number1 = int(input())
if number1 % 2 == 0:
    count1 += 1
else:
    count2 += 1

print("Please enter the second whole number.")
number2 = int(input())
if number2 % 2 == 0:
    count1 += 1
else:
    count2 += 1

print("Please enter the third whole number.")
number3 = int(input())
if number3 % 2 == 0:
    count1 += 1
else:
    count2 += 1

print(f"There were {count1} even and {count2} odd numbers")
