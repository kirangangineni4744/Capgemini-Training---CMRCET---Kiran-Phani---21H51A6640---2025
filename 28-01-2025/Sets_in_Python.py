set1={} # or empty_set = set()
print("Empty Set:",set1)

set2={1,2,3,4,"E"}
set3={1,2,"A","B","c","d"}

set2.add(7)
set4=set2
print(set4)
set2.remove(7)
print(set2)

#Union
print("Union of two sets:",set2|set3)

#Intersection
print("Intersection of two sets:",set2 & set3)

#Difference
print("Difference of two sets:",set2-set3)