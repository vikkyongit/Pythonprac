num_list = input("Please enter a list of numbers seperated by spaces")
num_list = num_list.split()
num_list.sort()

msg = input("Please enter a value to search")
first = 0
last = len(num_list)-1
found = False

while(first <= last and not found):
    mid = (first + last)//2
    if num_list[mid] == msg :
        found = True
    else :
        if msg < num_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
if found:
    print("The value is present")
else:
    print("Item not found")
