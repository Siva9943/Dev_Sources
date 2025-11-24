def pushZerosToEnd(arr):
    left=0
    n=len(arr)
    right=n-1
    print("sdfs")
    while left<right:
        print("gd")
        if arr[left]<arr[right]:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        elif left == right:
            break
    print(arr)
            

    
if "__main__" == __name__:
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    print("fdf")
    print(pushZerosToEnd(arr))

