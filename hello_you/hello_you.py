# Provide your name
name = input("What's your Name?: ")
print (name)

# Provide your Age
age = input ("How old are you?: ")
print (age)

# Ask user for city
city = input("Which city are you from?: ")
print (city)

# Ask what the user enjoys
love = input("What's your hobby?: ")
print (love)

# Create output text
string = "Your name is {} and you are {} years old. You live in {} and you enjoy {}"
output = string.format(name, age, city, love)

# Print the output
print(output)