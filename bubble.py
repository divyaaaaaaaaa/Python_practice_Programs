def bubble(num): #here function parameter is num
    n=len(num)
    for i in range(n-1):
        for j in range(n-i-1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
    return num


arr=[12,4,3,122,56,8]
result=bubble(arr)
print("bubble sorted array",result)