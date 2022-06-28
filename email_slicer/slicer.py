# Get user email address
email = input("What is your email address?: ").strip()

# Slice out the username
username = email[:email.index("@")]

# Slice out the domain name
domain = email[email.index("@") + 1:]

# Format message

output = "Your username is {} and your domain name is {}".format (username,domain)

print (output)