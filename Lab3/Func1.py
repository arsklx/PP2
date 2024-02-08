#1
def gtoO(grams):
    return 28.3495231 * grams
#2
def ftoc(f):
    c = (5 / 9) * (f - 32)
    print(c)
#3
def solve(numheads, numlegs):
    x = (numheads * 4 - numlegs) / 2
    y = numheads - x
    print(y, x)
#4
def filter_prime(li):
    new_li = []
    for i in li:
        p = 1
        for j in range(2, i):
            if i % j == 0:
                p = 0
                break
        if p:
            new_li.append(i)
    return new_li
#5
from itertools import permutations as per
s = input()
print(*list(per(s)))
#6
def stringrev(s):
    print(*reversed(s.split()))
#7
def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i-1] == 3 and nums[i] == 3:
            return True
    return False
#8 
def spy_game(nums):
    nums = map(str, nums)
    s = "".join(nums)
    if s.find("007") != -1:
        print(True)
    else:
        print(False)
#9
def sphere(r):
    return 3/4 * 3.14 * r ** 3
#10
def uniques(li):
    s = ""
    new_li = []
    for i in li:
        if i not in s:
            new_li.append(i)
    return new_li
#11
def palindrome(a):
    if a == a[::-1]:
        return True
    else:
        return False
#12
def histogram(li):
    for i in range(len(li)):
        print("*" * li[i])
#13
import random
def game():
    counter = 0
    z = random.randint(1, 20)
    print("Hello! What is your name?")
    s = input()
    print(f"Well, {s}, I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    d = int(input())
    while d != z:
        if d > z:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
        counter += 1
    print(f"Good job, KBTU! You guessed my number in {counter} guesses!")
            
    