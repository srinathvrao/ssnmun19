f = open("index.php", "r")
s=""
for x in f:
  s+=x[:len(x)-1]
f.close()

f = open("test.txt","w")
f.write(s)
f.close()