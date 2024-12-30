f=open("lec 07 FileInputAndOutPut\AdemoRead.txt","rt")  #if r na de by default read hi hota hai  if file dusre forder me hai uska path copy
                        #text file ke liye t likho but t yaha understood hai "rt"
data=f.read()       
print(data)
f.close()    # last me file close kar do

f=open("lec 07 FileInputAndOutPut\AdemoRead.txt","rt")
some_ch=f.read(5)   # starting ke 5 character  read karayga but hamne uper full file read kari isliye ab curser last me chala gaya hai isliye ab khuch print nhi hoga only next line print hogi chuki curser last line ka \n hi read karega  if karana hai to file dubara open close karo
print(some_ch)     # ab ham shuru se file open karege aur kam kare fil close karege
f.close()

f=open("lec 07 FileInputAndOutPut\AdemoRead.txt","rt")

line1=f.readline()  # curser las me pahuckar next line deta hai bcz string me last me \n hota hai
print(line1)

line2=f.readline()
print(line2)

line3=f.readline()  # yaha lines khatam ho gai hai aur curser last \n per aakar ruk jata hai baar baar use read karta hai isli empt print
print(line3)    # readlines se ssarei line read hot hai

f.close()