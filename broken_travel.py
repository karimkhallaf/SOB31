# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

# == changed into =
# changed int. to int(
# changed qoutation to double qoutation
year = int(input("Greetings! What is your year of origin? "))

if year <= 1900: #I added a colon
    #I added a backslash 
    print ('Woah, that\'s the past!')
elif year > 1900 and year < 2020: # && changed into and 
    print ("That's totally the present!")
else: # elif command changed into else 
    print ("Far out, that's the future!!")
