# Find the day
enterednumber = int(input("Enter a number: "))

days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

def days_of_the_week(enterednumber):
    number = enterednumber % 7
    day = days[number]
    print(day,  number)

days_of_the_week(enterednumber)


