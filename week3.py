# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return(round(price * (100 - discount_percent) / 100, 2))
    else:
        return(price)
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage.
try:
    price = float(input('How much is the product?\n'))
    discount = float(input('At what discount were you offered the product? For example, 20 for 20%, 1.9 for 1.9% and so on\n'))
except:
    print ('Your entry must be a number!')
else:
    # Print the final price after applying the discount, or if no discount was applied, print the original price.
    print(f'Your final price is: {calculate_discount(price, discount)}')
