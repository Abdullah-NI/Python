f=open("lec 07 FileInputAndOutPut\BsampleWrite.txt","w")   #w likhne se overwite hota ha means all erasr hokar nwe likah jata hai jaise hi open hotii hai
f.write("i am learning python")       #if file exit nhin karti hai to dusri ba jati hai
f.close()

#for aapending
f=open("lec 07 FileInputAndOutPut\BsampleWrite.txt","a")  #yabhi if file exit nhi katri new creart ho jati hai
f.write("\nand also i am learning java")
f.close()
