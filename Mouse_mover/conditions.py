cloud_env=input("Enter your Env").lower()
services=input("Enter your service")

if cloud_env=="AWS":
    print ("You are in AWS")
    if services=="ec2":
        print("you are in ec2")
    else:
        print("Some other service")
else:
    print("You are not in AWS")
print("both are running")

if cloud_env=="GCP":
    print ("You are in GCP")