import re  
"""
print (dir(re))
print ("-------------------------------------------------------")
print (re.findall.__doc__)
"""
text= """This alert service notifies mirza.sadique@gmail.com, mirza.sadique91@gmail.com and ezshophub.com@gmail.com"""
list_of_email= re.findall("[a-z0-9\.\+-_]+@+[a-z0-9\.\+-_]+.[a-z]+",text)
print (list_of_email)