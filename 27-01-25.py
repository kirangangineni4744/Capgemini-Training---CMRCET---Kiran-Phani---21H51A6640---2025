### LISTS in PYTHON

# List1=[]
# print("1. An empty list",List1)  

# List2=[1,2,3,4,5]
# print("2. A list with five elements",List2)

# List3=["abcd","efgh",1,2,3]
# print("3. The nested list",List3)

# #creating a list from a string
# List4=list("Kiran Phani Kumar")
# print("4. List created from a string",List4)

# #creating a list from a range of integers
# List5=list(range(-4,4))
# print("5. List from a range of integers",List5)

# List6=[1,2,3,4,5]
# print("6. Element at index 3 is:",List6[3])

# #Accessing an element from a nested list by using index
# List7=['a',[1,2,3,4],'b','c']
# print("7. Element at List7[1][3] is:",List7[1][3])

# #Slicing a list
# List8=[1,2,3,4,5,6,7]
# print("8. Slicing List8 from index 2 to 5",List8[2:6])

# print("9.Length of the list is:",len(List8))

# List10=[1,2,[3,4,5,6],7,8]
# print("10a. Element at index 1:",List10[1])
# print("10b. Element at List10[2][3]:",List10[2][3])
# print("10c. Slicing List10 from index 1 to 3 is:",List10[1:4])





# a,b,c,d,e=map(int,input().split())
# print(a+b+c+d+e)

# List1=[1,2,3,4,5]
# print("Sum:",List1[0]+List1[1]+List1[2]+List1[3]+List1[4])

# numbers=[int(input(f"Enter number {i+1}:")) for i in range(5)]
# total=sum(numbers)
# print("Sum of numbers:",total)





# import math
# n=int(input())
# min=math.inf
# max=-math.inf
# numbers=[int(input(f"Enter the number {i+1}:\n")) for i in range(n)]
# for i in range(n):
#     if numbers[i]>max:
#         max=numbers[i]
#     if numbers[i]<min:
#         min=numbers[i]
# print(min,max)




# # printing all prime numbers in a range in list form 
# # and finding the largest and smallest numbers among them

# def is_prime(num):
#     if num<=1:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#     return True

# def prime_num_in_range(start,end):
#     list1=[]
#     for num in range(start,end+1):
#         if is_prime(num):
#             list1.append(num)
#     return list1

# start=int(input("Enter starting number:\n"))
# end=int(input("Enter the ending number:\n"))

# print(f"Prime numbers in range {start} to {end}:")
# list1=prime_num_in_range(start,end)
# print(list1)

# print("Smallest number in this prime numbers list:",list1[0])
# print("Largest number in this prime numbers list:",list1[-1])





# # checking if the given string is a palindrome 
# # and then printing it in a list form

# def is_palindrome(string):
#     letters=list(string)
#     print(letters)
#     Reverse_String=string[::-1]
#     if string==Reverse_String:
#         return True
#     else:
#         return False

# string=input("Enter the string: ")
# if(is_palindrome(string)):
#     print("Yes! It is a Palindrome")
# else:
#     print("No! It is not a Palindrome")










### DICTIONARIES

# D1={}
# print("Empty Dictionary:",D1)

# D2={"spam":2,"eggs":3}
# print("The Two-item dictionary is:",D2)

# # D3={"food":D2}
# # print("The nested dictionary is:",D3)

# D3={"food": {"ham":1,"egg":2}}
# print("The nested dictionary is:",D3)

# D4=dict(name="bob",age=40)
# print("Alternative construction of a dictionary",D4)

# keys_list=[1,2,3,4,5]
# values_list=["A","B","C","D","E"]
# D5=dict(zip(keys_list,values_list))
# print("Zipped pairs ,key lists and keywords of a dictionary",D5)

# D6=dict.fromkeys(["a","b"])
# print(D6)

# print(len(D1),"\n",len(D2))

D2={"spam":2,"eggs":3}
D4={"spa":20,"egg":30}

print(D2.items())

print(D2.keys())

print(D2.values())

print(D2.get("spa",6))

D2.update(D4)
print(D2)

D4=D2.copy()
print(D4)

D4.clear()
print(D4)