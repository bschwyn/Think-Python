#You go on a wonderful holiday leaving on a day number 3 (a Wednesday).
#You return home after 137 nights. Write a general version of the program
#which asks for the starting day number,and the length of your stay,
#and it will tell you the number of day of the week you will return on.

#assign inputs to variables
dayLeft = input('What day are you leaving on?')
timeGone = input('How long will you be gone?')

dayReturn = int(dayLeft)+int(timeGone) % 7

print('You will return on day number',dayReturn,'of the week.\nHopefully your trip was pleasant.')

#   ***expanding on this exercise***

# In chapter 11, Dictionaries are introduced.
# Use a dictionary to tell what day of the week it is.

#One questions I encountered is ---which should be  the key and which the value?
#keys---any type
#value---any python object

#This means that keys have to be a single thing like a int, or a string
#   but they cannot be a list, array, or a dictionary.
#The value can be such. Here, since both weekdays and day number of the week it doesn't matter much.

#variable = dictionary with key: value
days_of_the_week = {'1':'Monday', '2':'Tuesday', '3':'Wednesday', '4':'Thursday','5':'Friday','6':'Saturday','7':'Sunday'}

dayName = days_of_the_week[str(dayReturn)]
print('You will return on',dayName)
                    
