#1
def gener_square(n):
    for i in range(1, n+1):
        yield i * i
n = int(input())
for i in gener_square(n):
    print(i, end=" ")
print()
print("=======================")

#2
li = []
def gener2(n):
    for i in range(0, n+1, 2):
        yield i
n = int(input())
for i in gener2(n):
    li.append(str(i))
print(", ".join(li))
li.clear()
print("=======================")

#3
def gener3(n):
    for i in range(0, n+1, 12):
        yield i
n = int(input())
li.extend(gener3(n))
print(*li)
li.clear()
print("=======================")

#4
def gener4(a, b):
    for i in range(a, b+1):
        yield i * i
a, b = map(int, input().split())
gener_obj = gener4(a, b)
for i in gener_obj:
    print(i, end=" ")
print()
print("=======================")

#5
def gener5(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
for i in gener5(n):
    print(i, end=" ")
print()
