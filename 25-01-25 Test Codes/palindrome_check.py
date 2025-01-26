def is_palindrome(string):
    Reverse_String=string[::-1]
    if string==Reverse_String:
        return True
    else:
        return False
    
string=input("Enter the string: ")
if(is_palindrome(string)):
    print("Yes")
else:
    print("No")