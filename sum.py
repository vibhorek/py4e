z=list()
while True:
  x=input("Enter number: ")
  if x=="done":
    break
  x=float(x)
  z.append(x)
print("Sum is", sum(z))
