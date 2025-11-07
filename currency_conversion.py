
pounds_to_euros = 1.13      #British pounds to euros conversion rate

pounds_input = input("Enter British pounds amount: ")       #user input

pounds = float(pounds_input)        #type conversion to float

euros_total = pounds * pounds_to_euros      #convert pounds to euros

print("Euros total:", euros_total)      #print result