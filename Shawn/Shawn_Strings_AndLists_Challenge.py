# You run a startup media company called Ripple Media
# It's typical when you hire a new employee in your company, to setup an email id for them

employee_name = 'Ash Rahman'

# You have decided the format of the email should be: Ash Rahman -> ash.rahman@ripplemedia.com
# Let's write some code that converts a name into an email id that matches this format
# 1.1 TODO: Let's save the lowercase version of the employee_name in a new variable 'lower_name' (use a string method to lower the name)
lower_name= employee_name.lower()
print(lower_name)

# 1.2 TODO: We want to separate the first name and last name and save it in a variable 'names_list' (use a string method to split the string into a list)
names_list= lower_name
my_list= lower_name.split(' ')
#print(names_list)
print(my_list)
# 1.3 TODO: We want to join the first name and last name with a '.' and save it in a variable called 'joined_names' (use a string method to join the list into a new string)
joined_names= '.'.join(my_list)
print(joined_names)
