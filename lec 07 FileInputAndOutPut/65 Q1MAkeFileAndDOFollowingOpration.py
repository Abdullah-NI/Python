#---->1
with open("lec 07 FileInputAndOutPut\Hpractice.txt","w")as f:
    f.write("hi everyone\nWe are learning File I/O\n")
    f.write("using java\nI like programing in java")
#---->2    
with open("lec 07 FileInputAndOutPut\Hpractice.txt","r") as f:
    data=f.read()
    newdata=data.replace("java","python")
    print(newdata)

with open("lec 07 FileInputAndOutPut\Hpractice.txt","w") as f:
    f.write(newdata)

#--->3
def check_WordPresent():     #  function ke bhar ke varibal acees kar sakte hai fnc me(like global varibal witout  static)   
    with open("lec 07 FileInputAndOutPut\Hpractice.txt","r") as f:   #but fun ke varibal bhar asix kar akte hai 
        new_data=f.read()

    word="learning"     # ya ise bhi wih ke ander hi likh do
    if(new_data.find(word)!=-1):   # word in new_data ,likho condition me 
        print("find")
    else:
        print("not  persenr")

check_WordPresent()

