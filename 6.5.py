text = "X-DSPAM-Confidence:    0.8475";
t=text.find(":    ")
b=(text[t+1:])
c=float(b.strip())
print(c)
