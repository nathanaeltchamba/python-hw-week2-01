#  Question 1

print("A Addition")
print("S Subtraction")
print("M Multiplication")
print("D Division")

choice = input("Enter your choice : ")

num1 = float(input("Enter Number 1 : "))
num2 = float(input("Enter Number 2 : "))


if choice == "A":
    print(num1, "+", num2, "=", (num1+num2))
elif choice == "S":
    print(num1, "-", num2, "=", (num1-num2))
elif choice == "M":
    print(num1, "*", num2, "=", (num1*num2))
elif choice == "D":
    if num2 == 0.0:
        print("Divide by 0 Error")
    else:
        print(num1, "/", num2, "=", (num1/num2))


