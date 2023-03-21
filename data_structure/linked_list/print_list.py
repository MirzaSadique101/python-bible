def print_list(self,value):
    temp=self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next
print_list(4)