def check_leap(num):
    return (num%4==0 and num%100!=0) or (num%400==0)

while True:
    num=int(input("Enter the year: "))
    if(check_leap(num)):
        print("Leap year")
    else:
        print("Not a leap year")
    