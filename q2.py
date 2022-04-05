# Question 2

numb = int(input("Choose the number of rows: "))

for z in range (0, numb):
    for y in range (0, numb-z-1):
        print(end=" ")
    for y in range(0, z+1):
        print("x", end=" ")
    print()
