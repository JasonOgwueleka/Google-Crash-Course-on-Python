# This function counts how many words are in a given string
# It splits the text into individual words using .split() and returns the total count with len().

# This function accepts a string variable "data_field"
def count_words(data_field):

    # Splits the string into individual words.
    split_data = data_field.split()

    # Then returns the number of words in the string using the len()function
    return len(split_data)

# Call to the function
print(count_words("Catalog item 3523: Organic raw pumpkin seeds in shell"))
# Output should be 9