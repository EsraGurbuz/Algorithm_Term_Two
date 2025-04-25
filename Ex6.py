def is_rightangled(a, b, c):
    result1 = a**2 == b**2 + c**2
    result2 = b**2 == a**2 + c**2
    result3 = c**2 == b**2 + a**2
    return result1, result2, result3

first = int(input( "Enter a value: "))
second = int(input( "Enter a value: "))
third = int(input( "Enter a value: "))

r1, r2, r3 = is_rightangled(first, second, third)

print(r1, r2, r3)