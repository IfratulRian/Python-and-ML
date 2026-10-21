#code comperihansion
#this means making the code less line then before
list = [80,79,68,78,91]
# new_list = [x+2 for x in list]
new_list = [x for x in list if x > 80]
print(new_list)