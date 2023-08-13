# create variable lovely_loveseat_description 
lovely_loveseat_description = """  Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. """

# create varaible for the loveseat price
lovely_loveseat_price = 254.00;

# create variable settee description
stylish_settee_description = """ Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.  """

# create variable stylish price
stylish_settee_price = 180.50;

# create luxurious lamp description
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade. """

# create variable to set price for lamp
luxurious_lamp_price = 52.15;

# create variable that stores sales tax
sales_tax = .088;

# create variable that holds customers purchase
customer_one_total = 0;

# create a new variable for customer list
customer_one_itemization = " "

# Add the price of lovely seat to customer one total 
customer_one_total +=  lovely_loveseat_price;

# Add the description of the lovely loveseat to customer itemization
customer_one_itemization += lovely_loveseat_description;

# Add the price of the lamp to customer total price
customer_one_total += luxurious_lamp_price;

# Add the description of the lamp to itemization
customer_one_itemization += luxurious_lamp_description;

# Create a variable to calulate customer tax
customer_one_tax = customer_one_total * sales_tax;

# Add the sale task to customer total cost
customer_one_total += sales_tax

#Print the receipts to the screen
print("Customer One Items:")

#Print customer one itemization
print(customer_one_itemization)

#Print out the string total of customer
print("Customer One Total:")

#print the total of customer one
print(customer_one_total)

