#1
class String12:
    def getString():
        global s
        s = input()
    def printString():
        print(s.upper())
#2
class Shape:
    def area(self):
        return 0 
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length
#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
#4 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, other):
        distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return distance
#5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        amount = int(input("Your Deposit amount:"))
        self.balance += amount
    def withdraw(self):
        amount = int(input("Your withdraw amount:"))
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("You Don't have enough money!")
#6
list1 = list(map(int, input().split()))
a = filter(lambda x : all((x % i) for i in range(2, x)), list1)
print(list(a))            
          