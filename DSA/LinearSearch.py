arr=[2,5,1,78,45,34,9,23,67]

def liner(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

print(liner(arr,9))
