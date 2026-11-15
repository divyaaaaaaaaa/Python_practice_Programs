def linear_search(num,target):
    for i in range(len(num)):
        if arr[i] == target:
            return i
    return -1

arr=[21,18,3,1,2]
target=8
result=linear_search(arr,target)
if result!=-1:
    print(f'the element {target} found in ',result)
else:
    print("element not found in array")