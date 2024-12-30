f=open("lec 07 FileInputAndOutPut\Dsample W+Mode.txt","w+")
print(f.read())  # file truncated mode me open hogi means phele khali ho jaygi fir oprn hogi

f.write("abc") # this likha hua tha isne thi ko abc bana diaya
f.close()

f=open("lec 07 FileInputAndOutPut\Dsample W+Mode.txt","r")  #yha only file ko read kara
print(f.read())
f.close()