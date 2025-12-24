'''
Write a program to count how many 
times a while loop runs from 1 to 10.
'''
count=0
i=1

while i<=10:
    count+=1
    i+=1

print(count)

'''
Write a program that 
counts from 1 to 10 using a while loop.
'''
count=0
i=1

while i<=10:
    count+=1
    print(count,end="-")
    i+=1
'''
Create a program that prints all odd numbers between 1 and 20 using a while loop.
'''
i=1
while i<=20:
    if(i%2!=0):
        print(f"odd no:{i}")
        
    i+=1
'''
Write a program that counts down from 10 to 1 using a while loop and prints "Happy New Year!" after the countdown is over.
'''
count=0
i=10
while i>=1:
    count+=1
    print(f"count-{count}")
    i-=1
print("Happy new year")
