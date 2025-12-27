'''
listt compresensive
syntax:[exp for item in collection]
'''
l=[1,2,3,4,5]
dl=[item**2 for item in l]

print(dl)

l1=[x for x in range(1,6)]
dl1=[item*2 for item in l1]

print(dl1)

#list comprehensive with condition--for my ref writen
#[exp for item in collection if_condition]
l2=[x for x in range(1,6)]
edl=[item*2 for item in l2 if item%2==0]#dfination is l2 collection of all item if they prove or true then that value need to goto exp then that value store inside list


print(edl) 

#string comprehensive
l_1=["ramu","krish","chandu"]
dl_1=[y[1] for y in l_1 ]
print(dl_1)

#dictionary comprehensive
l_1=["ramu","krish","chandu"]
ddl_1={item:len(item) for item in l_1}


print(ddl_1)

#hw
#Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop.
iteam_dic={'pencil':5,'eraser':5,"pen":10,"book":50}
item={int(value) for key,value in (iteam_dic).items() }
print(item)
