num1, num2 = input("Enter two number for calculations ").split()
num1 = int(num1)
num2 = int(num2)

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotent = num1 / num2
div = num1 // num2

print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotent))
print("{} // {} = {}".format(num1, num2, div))