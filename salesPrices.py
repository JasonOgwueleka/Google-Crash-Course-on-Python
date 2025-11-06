# This function extracts the item name and its price from a string
# It separates words (letters) from numbers, then returns a formatted sentence showing the item and its sale price
def sales_prices(item_and_price):

    item = ""
    price = ""
    # Variable "item_or_price" holds the result of the split
    item_or_price = item_and_price.split()

    # For each element "x" in the split variable "item_or_price"
    for x in item_or_price:

        # Checks if the element is a letter
        if x.isalpha():

            # If true, assign the element to the "item" string variable and add a space for any item names containing multiple words
            item += x + " "

        # If x is a number (if x.isalpha() is false
        else:
            # Assign the element to the "price" string variable
            price = x

    # Strip the extra space to the right of the last "item" word
    item = item.strip()

    # Return the item name and price formatted in a sentence
    return "{} are on sale for ${}".format(item,price)

print(sales_prices("Winter fleece jackets 49.99"))