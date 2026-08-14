
l = open("pip.txt")
data = l.read()
print(data)
l.close()

hup = "hey rudi? uummm complete python fast"

f = open("hup.txt", "w")
f.write(hup)
f.close()

o = open("hup.txt")
lines = o.readlines()
print(lines, type(lines))
o.close()

o = open("hup.txt")

line1 = o.readlines()
print(line1)

line2 = o.readlines()
print(line2)

o.close()

o = open("lol.txt" , "ice-cream") 
line = o.readline()

while line != "":
    print(line)
    line = o.readline()

o.close() 