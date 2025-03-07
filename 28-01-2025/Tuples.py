T1=()
print("Empty Tuple:",T1)

T2=(0)
print("One-item tuple:",T2)

T3=(0,"A",2,"B")
print("A four-item tuple:",T3)

T4=0,"A",2,"B"
print("A tuple with no brackets:",T4)

# T5=(x**2 for i in x)

T5=(0,1,'abc',('a','b',4,5))
print("Nested Tuple:",T5)

List1=[1,2,'a','b']
T6=tuple(List1)
print(T6)

T7=tuple('Spam')
print(T7)

T8=(1,2,3,'a',('b',6,7))
print("Element of tuple T8 at index 4:",T8[4])
print("Elements of tuple T8 from index 0 to 3:",T8[0:4])

print("Length of tuple is:",len(T8))