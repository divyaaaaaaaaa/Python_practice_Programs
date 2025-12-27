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
#Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.

food_type=["idli","veg palav","chicken birayani"]
food_t=[food.upper() for food in food_type]
print(food_t)

