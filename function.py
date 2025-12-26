def greeta():
    print("hello world")#defining the fun
    
greeta()#call function

def marriage():
    print("boy married girl")

def marriage(boy,girl):#parameter
    print(f"boy name: {boy}")
    print(f"girl name: {girl}")
    print(f"{boy} married {girl}")

marriage("krishna","rukmini")#specialized argument
marriage("rama","sitha")#specialized argument


#default parameter
def marriage(boy,girl="Girl"):#parameter
    print(f"boy name: {boy}")
    print(f"girl name: {girl}")
    print(f"{boy} married {girl}")

marriage("ramu")#specialized argument
'''
#without default parameter
def marriage(boy,girl):#parameter
    print(f"boy name: {boy}")
    print(f"girl name: {girl}")
    print(f"{boy} married {girl}")

marriage("ramu")#specialized argument
#o/p:TypeError: marriage() missing 1 required positional argument: 'girl'
'''
#create table using for loop
for i in range(1,11):
    for j in range(1,11):
        print(f"{i}x{j}={2*i}")
     
#create table using def 
def table():
    for i in range(1,11):
        for j in range(1,11):
            print(f"{i}x{j}={2*i}")
table()

#Sum Function: Write a function add_numbers(a, b) that returns the sum of two numbers. Call this function with different values.
def add_numbers(a,b):
    return a+b

n=add_numbers(3,7)
print(n)
