n=input('enter the name:')
print(n)
n1=int(input('enter the number:'))
print(n1)
#user entering the list 
s='Learnig Python feeling good'
x=s.split()#split():it put each word here as an element in a list 
print(x)

s=input("enter a list of integers:")#enter a list of integers:1 2 45 67
print(s)#gives o/p as string as o/p:1 2 45 67
# convert string to list we use split()
r=s.split()
print(r)#o/p:['1', '2', '45', '67']convert to list but there is again error its in string type but we need to convert to integer
l=[int(n) for n in r]#defination collection of r where n is string litteral and int(n) experation of integer and these store it in l variable
#it will convert the string litteral to integer litteral
print(l)
 # short cut or
p=[input("enter a list of integers: ")].split()
x=[int(num1) for num1 in p]
print(x)
 # another shortcut
x=[int(num1) for num1 in input("enter a list of integers: ").split()]
#this above definition here we use list comperhension.
'''
use string split method.finally convert the type to int
finally you take the input of the list
'''
print(x)