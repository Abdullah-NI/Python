list=[1,4,9,16,25,36,49,64,81,100,49]
for ele in list:
    print(ele)

x=49
idx=0
for ele in list:
    if(ele==x) :
        print("found at index",idx)
        break
    idx+=1