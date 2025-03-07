#area of rectangle using functions
# def display(data):
#     print(f"The area is {data}")
    
# def get_input():
#     received_length=float(input("Length: "))
#     received_width=float(input("Width: "))
    
#     return (received_length,received_width)

# def compute_area(length,width):
#     area=length*width
#     return area
    
# def main():
#     (length,width)=get_input()
#     area=compute_area(length,width)
#     display(area)
    
# main()
    
# l,b=map(int,input().split())
# area=l*b
# print(area)






# a,b,c,d=map(int,input().split())
# avg=(a+b+c+d)/4
# print(avg)

# #inputs of four numbers
# def inputs():
#     p=float(input("first number:\n"))
#     q=float(input("second number:\n"))
#     r=float(input("third number:\n"))
#     s=float(input("fourth number:\n"))
#     return (p,q,r,s)

# #calculating the sum
# def calculate_sum(p,q,r,s):
#     sum=p+q+r+s
#     return sum

# #calculating the average
# def calculate_avg(sum):
#     avg=sum/4
#     return avg

# #displaying the calculated average
# def display(avg):
#     print(f"average of four numbers:{avg}")
    
# #main function
# def main():
#     p,q,r,s=inputs()
#     sum=calculate_sum(p,q,r,s)
#     avg=calculate_avg(sum)
#     display(avg)
# main()






# # # findign the maximum of three numbers

# def inputs():
#     a=float(input("First Number:\n"))
#     b=float(input("Second Number:\n"))
#     c=float(input("Third Number:\n"))
#     return (a,b,c)

# def compare_num(a,b,c):
#     if (a>=b and a>=c):
#         return a
#     elif(b>=a and b>=c):
#         return b
#     else:
#         return c
    
# def display_max(Max):
#     print(f"Maximum of three numbers is:{int(Max)}")
    
# def main():
#     a,b,c=inputs()
#     Max=compare_num(a,b,c)
#     display_max(Max)
# main()
    
    
# import dis

# def inputs():
#     a=float(input("1st Number:\n"))
#     b=float(input("2nd Number:\n"))
#     c=float(input("3rd Number:\n"))
#     d=float(input("4th Number:\n"))
#     return (a,b,c,d)
    
# def Maximum_num(a,b,c,d):
#     str1 = " "
#     str2 = " "
#     str3 = " "
#     if a>=b:
#         M=a
#         str1="a"
#     else:
#         M=b
#         str1="b"
        
#     if c>=d:
#         N=c
#         str2="c"
#     else:
#         N=d
#         str2="d"
        
#     if M>=N:
#         str3 = str1
#         return M,str3
        
#     else:
#         str3 = str2
#         return N,str3
         
# def display(Max,Var):
#     print(f"The maximum no. of a,b,c,d is {Var} and it's value is {Max}")
    
# def main():
#     a,b,c,d=inputs()
#     Max,Var=Maximum_num(a,b,c,d)
#     display(Max,Var)
#     dis.dis(Maximum_num)
# main()
    
    



# # # prime numbers code
# import math
# import dis
# def inputs():
#     n=int(input("Given number:\n"))
#     return n

# def if_prime(n):
#     if n%2==0:
#         return False
#     else:
#         for i in range(3,int(math.sqrt(n)),2):
#             if n%i==0:
#                 return False
#         return True
    
# def display(P,n):
#     if P==True:
#         print(f"{n} is prime\n")
#     else:
#         print(f"{n} is not prime")

# def main():
#     n=inputs()
#     P=if_prime(n)
#     display(P,n)
#     dis.dis(if_prime)
    
# main()                
    
   
    
import math
import dis
def inputs():
    n=int(input("Given number:\n"))
    return n

def if_prime(n):
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3,int(math.sqrt(n)),2):
            if n%i==0:
                return False
        return True

def main():
    n=inputs()
    P=if_prime(n)
    print(f"{P}")
    dis.dis(if_prime)
main()


