def in_which_line_wordPresent():
    word="learning"
    data=True
    line_no=1
    with open("lec 07 FileInputAndOutPut\Hpractice.txt","r") as f:    
        while data:
            data=f.readline()
            if(data.find(word)!=-1):  
                 return line_no
            line_no+=1
    return -1

line_no=in_which_line_wordPresent()
print(line_no)
