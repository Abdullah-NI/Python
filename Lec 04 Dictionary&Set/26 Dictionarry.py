dictonary={
    "key":"value",
    "name":"apnacollege",
    "subject":["python","c","java","etc"],
    "topics":("dic","set"),
    "age":18,
    "isAdult":True,
    2:"my rool",
    2.45:34455,    #fees
    True:"boolean can be key ",
    ("mr",45,"et"):3,
    #[4,5,6,]:8,     list ko key nhi bana sakte hai chuki ye change ho sakti hai aur na hi dictonari ko key bana sakte hai ye bhi change ho sakte hai key use banate hai jo change ka ho
                      # dic me int ,float,String,boolean,tuple ko key bana sakte hai list aur dictionary ko key nhi bana sakte hai
    "sub dictonary":{     # yaha dic as a value use ki hai not key
        "my": "name",
        "age":18
    }
}

print(dictonary)
print()

print(dictonary["name"])
print(dictonary["subject"])
print(dictonary[2])

dictonary["name"]="Abdullah"  #modification is allow
dictonary["name"]=23
dictonary["surname"]="Ansari" #new key value order pair add karna ye last me add hoga
print(dictonary)