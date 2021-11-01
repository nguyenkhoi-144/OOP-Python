fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist0 = [x for x in fruits if "a" in x]
newlist = [x for x in fruits if x != "apple"]
newlist = [x for x in fruits]
newlist1 = [x for x in range(10)]
newlist2 = [x for x in range(10) if x < 5]
newlist3 = [x.upper() for x in fruits]
newlist = ['hello' for x in fruits]
newlist5 = [x if x != "banana" else "orange" for x in fruits]
print(newlist0)
