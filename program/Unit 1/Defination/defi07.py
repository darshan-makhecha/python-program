no1 = float(input("Enter first number: "))
no2 = float(input("Enter second number: "))

# choise operation
print("Operation: +, -, *, /")
select = input("Select operations: ")


if select == "+":
    print(no1, "+", no2, "=", no1+no2)

elif select == "-":
    print(no1, "-", no2, "=", no1-no2)

elif select == "*":
    print(no1, "*", no2, "=", no1*no2)

elif select == "/":
    print(no1, "/", no2, "=", no1/no2)

else:
    print("Invalid input")
