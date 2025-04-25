months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "November", "December"]
for i in months:
    print("One of the months of the year is " + i)

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# For different row
for i in xs:
    print(i)

# For one row
for i in xs:
    print(i, end=" ")

# Each number and its square on a new line
for i in xs:
    print(i, i*i)

# Adds all the numbers from the list into a variable called "total"
total = 0
for i in xs:
    total = total + i
print(total)

# Product of all the numbers in the list
product = 1
for i in xs:
    product = product * i
print(product)