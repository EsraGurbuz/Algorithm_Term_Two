def find_hypot(base, heigth):
    x = base * base + heigth * heigth
    hypotenuse = x ** 0.5 
    print(hypotenuse)

base = int(input("Enter a base: "))
heigth = int(input("Enter a heigth: "))

find_hypot(base, heigth)