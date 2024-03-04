import os
#1
n = r"C:\Users\Arsen\PP2\Lab6"
directories = []
for i in os.listdir():
    if os.path.isdir(i):
        directories.append(i)
print(directories)
print(os.listdir())
print([i for i in os.listdir(n) if not os.path.isdir(i)])
print("========================")
#2
print(os.access(n, os.F_OK))
print(os.access(n, os.R_OK))
print(os.access(n, os.W_OK))
print(os.access(n, os.X_OK))
print("========================")
#3
print(os.path.exists(n))
print(os.path.basename(n))
print(os.path.dirname(n))
#4
with open("somefile.txt", "r") as ff:
    counter = 0
    while ff.readline():
        counter += 1
print(counter)
#5
li = ["some", "things", "in", "a", "list"]
with open("somefile.txt", "w") as ff:
    for item in li:
        ff.write(item + " ")
#6
import string
letters = string.ascii_uppercase
for letter in letters:
    with open(letter + ".txt", "a") as file:
        pass
#7
with open("first.txt", "r") as file1, open("second.txt", "w") as file2:
    for lines in file1.read():
        file2.write(lines)
#8
n = "somepath"
location = "its location in disc"
path = os.path.join(location, n)
if os.path.exists(path):
    os.remove(path)
