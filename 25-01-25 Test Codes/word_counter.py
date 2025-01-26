def wordcounter(string):
    words=string.split()
    word_count={}
    for char in words:
        if char in word_count:
            word_count[char]+=1
        else:
            word_count[char]=1
    return word_count

string=input("Enter string:\n")
word_counts=wordcounter(string)
for word, count in word_counts.items():
    print(f"{word}: {count}")