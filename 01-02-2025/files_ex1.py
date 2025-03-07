### method-01
# file=open("sample3.txt","w")
# file.write("Hello, this is a sample text !!!!!!")
# file.close()

with open("sample4.txt","w") as file:
    file.write("Hello, World!")   #file closes automatically