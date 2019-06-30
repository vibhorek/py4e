fname = input("Enter file name: ")
fh = open(fname)
list=[]
for lines in fh:
    words=lines.split()
    for word in words:
        if word not in list :
            list.append(word)
list.sort()
print(list)
