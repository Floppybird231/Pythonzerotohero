calculation_of_units=24
name_of_units="hours"


def days_to_units(num_of_days):
    return (f"{num_of_days} days are {num_of_days* calculation_of_units} {name_of_units}")

def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number>=0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif num_of_days == 0:
            print("You entered 0, put a valid positive number please")
        else:
            print("You entered a negative number, put a valid positive number please")


    except ValueError:
        print('your input is not a valid number')


user_input = input("Hey user, enter a number and i will convert it to hours!\n")
validate_and_execute()

