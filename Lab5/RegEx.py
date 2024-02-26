import re
#1
txt = input()
p1 = re.findall("b*a", txt)
print(p1)
print("=======================")
#2
p2 = re.findall("bba|bbba", txt)
print(p2)
print("=======================")
#3
p3 = re.findall("^[a-z]+_[a-z]+$", txt)
print(p3)
print("=======================")
#4
p4 = re.findall("[a-z]+[A-Z]", txt)
print(p4)
print("=======================")
#5
p5 = re.findall(".+ab$", txt)
print(p5)
print("=======================")
#6
p6 = re.sub("[,. ]", ":", txt)
print(p6)
print("=======================")
#7
p7 = re.split("_+", txt)
p7 = p7[0] + "".join(map(lambda x : x.title(), p7[1:]))
print(p7)
print("=======================")
#8
p8 = re.findall("[A-Z][a-z]*", txt)
print(p8)
print("=======================")
#9
p9 = re.findall(r'[A-Z][a-z]*', txt)
print(" ".join(p9))
print("=======================")
#10
p10 = re.findall(r'[A-Z][a-z]*', txt)
print("_".join(map(str.lower, p10)))

