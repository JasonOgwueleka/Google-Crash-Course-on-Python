# This program repeatedly asks the user to enter their hours worked and hourly rate until valid numeric input is provided
# It then calculates and displays the weekly earning
# If the user enters something that isn’t a number, it shows an error message and asks again

# Start a while loop that keeps asking the user for input until valid data is provided
while True:
    try:
        hours = float(input("Hours worked: "))
        rate_per_hour = float(input("Rate per hour: "))
        weekly_earning = hours * rate_per_hour

        # Display the calculated weekly earning
        print("Your weekly earning is: ", weekly_earning)

        # Exit the loop after successful calculation
        break
    except ValueError:

        # Handle cases where user doesn't enter a number
        print("Please enter numbers only! Let's try again...\n")
