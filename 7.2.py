# Use the file name mbox-short.txt as the file name
#numbers extracted and stored in a list
x = open(input("Enter file name: "))
z=list()
for y in x:
    y=y.rstrip()
    if not y.startswith("X-DSPAM-Confidence:") : 
        continue
    a=float(y[20:])
    z.append(a)
#finding average
total=0
count=0
for num in z:
   total=total+num 
   count=count+1 
average=total/count
print("Average spam confidence:", average)
