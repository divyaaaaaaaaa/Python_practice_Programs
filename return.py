#user defined function without return statement
def calculate_sum(a, b):
    print(a + b)#4

my_sum = calculate_sum(3, 1) 
print(my_sum) # None

#with return statement
def calculate_sum(a, b):# # a and b are parameters
    return(a + b)

my_sum = calculate_sum(3, 1)  #3 and 1 are arguments
print(my_sum) #4
