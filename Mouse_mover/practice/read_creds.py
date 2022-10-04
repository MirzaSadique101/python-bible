
from utils import file_read
'''
def file():
    file_reader = open("/home/user/Downloads/python_bible/python-bible/Mouse_mover/practice/creds.txt",'r')
    cred_list = file_reader.readlines()
    file_reader.close()
'''

cred_list = file_read()

for creds in cred_list:
    print (creds.split("=")[1])