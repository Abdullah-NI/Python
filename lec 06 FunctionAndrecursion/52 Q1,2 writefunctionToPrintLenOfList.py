# def print_len(list):
#     len=0
#     for ele in list:
#         len+=1
#     return len

def print_len(list):
    return len(list)

def print_list(list):
    for ele in list:
        print(ele,end=" ")


cities=["delhi","gurgaon","Noida","pune","Mumbai","Chennai"]
hero=["thor","ironman","shaktiman"]

# ---> print len of list
print(print_len(cities))
print(print_len(hero))

# print list element in same line
print_list(cities)
print()
print_list(hero)