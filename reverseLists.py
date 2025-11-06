# This function combines two lists of profit years into one chronological list.
# It first reverses the order of the most recent years, appends them to the older list,
# Then returns the combined list in order from oldest to newest.


def record_profit_years(recent_first, recent_last):

    # Reverse the order of the "recent_first" list so that it is in chronological order
    recent_first.reverse()

    # Extend the "recent_last" list by appending the newly reversed "recent_first" list
    recent_last.extend(recent_first)

    # Return the "recent_last", which now contains the two lists combined in chronological order
    return recent_last

# Assign the two lists to the two variables to be passed to the record_profit_years() function.
recent_first = [2022, 2018, 2011, 2006]
recent_last = [1989, 1992, 1997, 2001]

# Call the record_profit_years() function and pass the two lists as parameters
print(record_profit_years(recent_first, recent_last))
