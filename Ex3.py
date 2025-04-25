xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
def grade(xs):
    for i in xs:
        if i >= 75:
            print("First", i)
        elif i >= 70 and i < 75:
            print("Upper Second", i)
        elif i >= 60 and i < 70:
            print("Second", i)
        elif i >= 50 and i < 60:
            print("Third", i)
        elif i >= 45 and i < 50:
            print("F1 Supp", i)
        elif i >= 40 and i < 45:
            print("F2", i)
        else:
            print("F3", i)

grade(xs)
