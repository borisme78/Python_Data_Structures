# Use romeo.txt as the file name
try:
    fname = input("Enter file name: ")
    text_file = open(fname)
except:
    print('Not found file')
    exit()

#text_file = open(fname)
lst = list()
for line in text_file:
    list_words = line.split()
    for word in list_words:
        if word in lst: continue
        lst.append(word)
    
lst.sort()
print(lst)