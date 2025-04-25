def day_you_return(starting_day_number, length_of_stay):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return_day_number = (starting_day_number + length_of_stay) % 7
    return days[return_day_number]

start_day = 3  # Wednesday
length = 137
returned_day = day_you_return(start_day, length)
print(f"You return on a {returned_day}.")