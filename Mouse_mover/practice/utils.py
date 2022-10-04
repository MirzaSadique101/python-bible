import re

def email_finder():
    email = input("Please provide a sentence, we will strip email id for you: ")
    list_of_email= re.findall("[a-z0-9\.\+-_]+@+[a-z0-9\.\+-_]+.[a-z]+",email)
    print (list_of_email)

def file_read():
    file_reader = open("/home/user/Downloads/python_bible/python-bible/Mouse_mover/practice/creds.txt",'r')
    cred_list = file_reader.readlines()
    file_reader.close()
    return cred_list

