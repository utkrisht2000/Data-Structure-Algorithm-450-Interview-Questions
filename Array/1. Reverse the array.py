n = int(input()) # No of Test Case

for i in range(0,n):
    m = int(input()) # No of element in Array
    arr = list(map(int,input().split(" "))) # Insertion in array
    for i in range(0,m):
        print(arr[(m-1)-i], end = " ") # Reverse the array
