with open("lec 07 FileInputAndOutPut\FSmple withSyntex.txt","r") as f:
    data=f.read()
    print(data)
    # with apne aap close kkar dega
with open("lec 07 FileInputAndOutPut\FSmple withSyntex.txt","w") as f:
    f.write("new data")
    