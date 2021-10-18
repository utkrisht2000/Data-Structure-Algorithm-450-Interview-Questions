#Find the maximum and minimum element in an array

n = int(input()) # Size of Array
lis = list(map(int, input().split(" "))) # Insertion in array
min = lis[0]
max = lis[0]

for i in range(0,n):
    if lis[i] > max:
        max = lis[i]
    if lis[i] < min:
        min = lis[i]

print("Min:", min)
print("Max:", max)
