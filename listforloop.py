l=[1,34,3,56]
total=0

for i in l:
    total=total + i
    print(total)

for num in l:
    total=total + num
print(total)# printed once after loop

for n in l:
    print(total)
    total=total + n
print(total)
    # printed inside loop



dl=[]

for num in l:
    dl.append(num*4)
    print(dl)

print(dl)



