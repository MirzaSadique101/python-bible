'''
integers = [1,2,3,4,5]
value = input("Enter an integer value: ")

new_integer = integers.append(value)

print (new_integer)
'''
#input size of the list
n = int(input("Enter the Size of the List: "))

# Store integers in a list using map, split, and strip functions
# Below line read inputs from user using map() function

lst = list(map(int,input("Enter the integer elements of list(Space-Separated): ").strip().split()))[:n]

print('The list is:', lst)