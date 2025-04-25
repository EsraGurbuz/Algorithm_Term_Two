def is_rightangled(a, b, c):
    list = sorted([a, b, c])

    if list[2]**2 == list[1]**2 + list[0]**2:
        return True
    else:
        return False
    
first = int(input( "Enter a value: "))
second = int(input( "Enter a value: "))
third = int(input( "Enter a value: "))

print(is_rightangled(first, second, third))