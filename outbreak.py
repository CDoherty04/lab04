def run():
    """Gets valid input to be called recursively"""

    while True:
        try:

            # Get input
            day = int(input("What day do you want a sick count for?\n"))

            # Check for day less than 1
            if day < 1:
                print("\nCan't have a day less than 1\n")
                continue

            else:
                # Begin recursive call, print the result, and end the loop
                print(get_total_sick(day))
                break

        # Loop continues until integers are given
        except ValueError:
            print("\nThe input requires integer values\n")


def get_total_sick(day):
    """Prints the total number of people sick on the given day"""

    # Base cases
    if day == 1:
        return 6
    elif day == 2:
        return 20
    elif day == 3:
        return 75

    # After day 3 return the total of the last 3 days sick
    else:
        return get_total_sick(day-1) + get_total_sick(day-2) + get_total_sick(day-3)
