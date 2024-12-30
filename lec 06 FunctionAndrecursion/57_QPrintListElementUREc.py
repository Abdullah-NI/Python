def print_list(list,idx):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

list=[5,2,4,"Abdulah","hgj"]
print_list(list,0)