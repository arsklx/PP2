from time import sleep as sl
#1
li, n = map(int, input().split()), int(input())
print(*map(lambda x : x * n, li))
print("===============")
#2
n = input()
print(len(list(filter(lambda x : 65 <= ord(x) <= 90 or 97 <= ord(x) <= 122, n))))
print("===============")
#3
print("YES" if n == "".join(list(reversed(n))) else "NO")
print("===============")
#4
a = int(input())
n = int(input()) / 1000
sl(n)
print(f'Square root of {a} after {n} miliseconds is {a**0.5}')
print("===============")
#5
li = tuple(map(int, input().split()))
#li = (True, True, 1, 0, 7)
print("True" if all(li) else "False")
