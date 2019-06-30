text = "X-DSPAM-Confidence:    0.8475";
pos=text.find(":")
t=text.split(":")
(a,b)=t
print(float(b))
