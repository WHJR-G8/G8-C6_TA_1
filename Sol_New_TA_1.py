number_1 = int(input("Enter the first number : "))
number_2 = int(input("Enter the second number : "))
number_3 = int(input("Enter the third number : "))

print("The multiplication of number 1 and number 2 is : ", number_1 * number_2)
print("The division of number 1 and number 2 is : ", number_1 / number_2)
print("The addition of number 1 and number 2 is : ", number_1 + number_2)
print("The subtraction of number 1 and number 2 is : ", number_1 - number_2)

if number_1 > number_2 and number_1 > number_3:
    print("\n Number 1 is the largest")
elif number_2 > number_1 and number_2 > number_3:
    print("\n Number 2 is the largest")
else:
    print("\n Number 3 is the largest")