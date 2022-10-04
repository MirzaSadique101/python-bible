try:
    file_obj = open("/home/user/Downloads/python_bible/python-bible/Mouse_mover/practice/creds_write.txt",'r')
    cred_list = file_obj.readlines()
    print(cred_list)
except:
    file_obj = open("/home/user/Downloads/python_bible/python-bible/Mouse_mover/practice/creds_write.txt",'w')
    file_obj.write("username=eshophub.com\npassword=123456")
finally:
    file_obj.close()