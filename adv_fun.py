def add(*a):
    print(type(a))

add(1,2,3,4)

#keywords arguments
def student_info(**details):
    print(type(details))
    for key,value in details.items():
        print(f"{key}:{value}")

student_info(name="divya",age=21)

#lambda
add=lambda a,b : a+b
print(add(1,2))

double=lambda x:2*x
print(double(200))

#list of dictionary tudents
Student=[
    {"name":"divyaS","marks":12},
    {"name":"divya","marks":100},
    {"name":"ramu","marks":50},
]
Student.sort(key= lambda x: x["marks"])
print(Student)
#or we need reverse also to above student then
Student.sort(key= lambda x: x["marks"],reverse="true")
print(Student)