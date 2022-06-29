known_users = ["Sid", "Rahul", "Rohan", "Alok", "Peter", "Sohail", "Alex", "Anjali"]

print (len(known_users))

while True:
    print ("Hi, I am Travis")
    name = input("What is your name ?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Do you want your name to be removed from the user list? y/n: ").strip().lower()

        if remove == "y":
            print(known_users)
            known_users.remove(name)
            print (known_users)
    
    
else:
    print("Name not recognized")