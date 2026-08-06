add=[]
tot=0


for i in range (5):
    mark=int(input("enter your marks:"))
    add.append(mark)
    tot =tot+mark
    avg = tot/len(add)

print ("total mark is:",tot)
print("average:",avg)