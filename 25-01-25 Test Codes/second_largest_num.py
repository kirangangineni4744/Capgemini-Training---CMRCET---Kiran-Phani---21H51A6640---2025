def second_largest(arr):
    max=-float('inf')
    second_max=-float('inf')
    for i in arr:
        if i>max:
            second_max=max
            max=i
        elif i>second_max and i!=max:
            second_max=i
    return second_max
arr=[]

n=int(input("Enter the no. of numbers:\n"))
print("Enter the numbers:")
for i in range(n):
    arr.append(int(input()))
print("Second largest number is:\n",second_largest(arr))