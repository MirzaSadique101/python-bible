import json

policy_object = open("aws_policy.json",'r')
policy = policy_object.read()
policy_object.close()

print(type(policy))

policy_dict = json.loads(policy)
print(type(policy_dict))

policy_dict["Statement"][0]["Effect"] = "Reject"

new_policy_dict = json.dumps(policy_dict)
new_policy_object = open("new_aws_policy.json",'w')
new_policy_object.write(new_policy_dict)
new_policy_object.close()
'''
policy_object = open ("aws_policy.json",'w')
policy_object.write
'''