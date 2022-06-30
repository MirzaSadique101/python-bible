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
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")
    
    
    else:
        print("Hmmm, I don't think I have met you yet {}".format(name))
        add = input("Do you want your name to be added to the list (y/n): ").strip().lower()
        if add == "y":
            known_users.append(name)
            print("Congratulations!, Your name is added to the list of known users:{} ".format(known_users))
        elif add == "n":
            print("No worries, see you around")