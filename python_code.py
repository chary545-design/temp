from collections import namedtuple

# Define a named tuple
chary = namedtuple('chary', ['x', 'y'])
p = chary(10, 20)

print(p.x, p.y)

	********************************
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)  # Add to left
dq.append(4)      # Add to right
print(dq)  

	********************************
from collections import Counter

cnt = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(cnt)        # Counter({'a': 3, 'b': 2, 'c': 1})
print(cnt.most_common(1)) 

	********************************
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
print(od)

	********************************
from collections import defaultdict

dd = defaultdict(int)  # Default value is 0
dd['a'] += 1
print(dd['a'])  # 1
print(dd['b'])

from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.pop()
print(dq)

	********************************

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
	
	words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
	
	********************************
	
	# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
		
		********************************
		
		for i in range(5):
    print(i)
	
	0
1
2
3
4
********************************
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

0 Mary
1 had
2 a
3 little
4 lamb
********************************
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
********************************
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
********************************
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
********************************

class xyz:
    name = "chary"

abc = xyz()
print(abc.name)

result : Chary
********************************
class xyz:
    def name(self, x):
        self.x = x
        print("its a name")

    def cal(self):
        if self.x % 2 == 0:
            print("even")
        else:
            print("odd")

abc = xyz()
abc.name(9)   # sets x
abc.cal()     # prints "even"

Answer :  odd
********************************
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof! I'm {self.age} years old.")


my_dog = Dog("Buddy", 3)
print(my_dog.name)  
my_dog.bark()  

**********************************
class rectangle:
    def __init__(self,width,height):
                 self.width = width
                 self.height = height
    def area(self):
            return self.width * self.height
    
abc = rectangle(5,3)
print(abc.area())
    
   Ans : 15
**********************************
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance


account = BankAccount()
account.deposit(60)
account.withdraw(50)
print(account.get_balance())

Ans : 10 
**********************************
class Vehicle:
    def __init__(self, name: str, fuel: str):
        self.name = name
        self.fuel = fuel

    def describe(self):
        return f"{self.name} ({self.fuel})"


class TwoWheeler(Vehicle):
    def __init__(self, name: str, fuel: str, wheels: int = 2):
        super().__init__(name, fuel)
        self.wheels = wheels

    def describe(self):
        base = super().describe()
        return f"{base} - {self.wheels} wheels"

class FourWheeler(Vehicle):
    def __init__(self, name: str, fuel: str, wheels: int = 4):
        super().__init__(name, fuel)
        self.wheels = wheels

    def describe(self):
        base = super().describe()
        return f"{base} - {self.wheels} wheels"


# Usage
v = Vehicle("car", "diesel")
print(v.describe())  # car (diesel)

b = TwoWheeler("bike", "petrol")         # wheels defaults to 2
print(b.describe())  # bike (petrol) - 2 wheels

c=FourWheeler("car","diesel")
print(c.describe())

Ans :
    class Vehicle:
    def __init__(self, name: str, fuel: str):
        self.name = name
        self.fuel = fuel

    def describe(self):
        return f"{self.name} ({self.fuel})"


class TwoWheeler(Vehicle):
    def __init__(self, name: str, fuel: str, wheels: int = 2):
        super().__init__(name, fuel)
        self.wheels = wheels

    def describe(self):
        base = super().describe()
        return f"{base} - {self.wheels} wheels"

class FourWheeler(Vehicle):
    def __init__(self, name: str, fuel: str, wheels: int = 4):
        super().__init__(name, fuel)
        self.wheels = wheels

    def describe(self):
        base = super().describe()
        return f"{base} - {self.wheels} wheels"


# Usage
v = Vehicle("car", "diesel")
print(v.describe())  # car (diesel)

b = TwoWheeler("bike", "petrol")         # wheels defaults to 2
print(b.describe())  # bike (petrol) - 2 wheels

c=FourWheeler("car","diesel")
print(c.describe())

**********************************
class School:
    def __init__(self, name, clas):
        self.name = name
        self.clas = clas

    def describe(self):
        return f"{self.name} {self.clas}"


class Room(School):
    def __init__(self, name, clas, size):
        # Call base constructor with only the args it expects
        super().__init__(name, clas)
        self.size = size

    def describe(self):
        # Extend the base description
        base = super().describe()
        return f"{base} {self.size}"


# Usage
school1 = School("siddardha", 4)
#print(school1.name)              # siddardha
#print(school1.describe())        # siddardha 4

room1 = Room("siddardha", 4, 30)
print(room1.describe())          # siddardha 4 30


        
        Ans :
siddardha 4 30
**********************************
class Employee:
    def __init__(self,Name,EmpId,EmpAdd):
        self.Name = Name
        self.EmpId = EmpId
        self.EmpAdd = EmpAdd
    def describe(self):
      return f"{self.Name} {self.EmpId} {self.EmpAdd}"
class company(Employee):
    def __init__(self, Name, EmpId, EmpAdd,Dept):
        super().__init__(Name, EmpId, EmpAdd)
        self.Dept = Dept

    def describe(self):
        base = super().describe()
        return f"{base} {self.Dept}"
    
Job = company("Veda" , 101, "vij" , "HR")
print(Job.describe())

Ans :
    Veda 101 vij HR
**********************************

class Travell:
    def __init__(self,Source,Destination):
        self.Source = Source
        self.Destination = Destination
 
    def describe(self):
     return f"{self.Source} {self.Destination}"
class Trip(Travell):
   def __init__(self, Source, Destination,Price):
            super().__init__(Source, Destination)
            self.Price = Price
 
   def describe(self):
       base = super().describe()
       return f" {base} {self.Price}"
     
Trip1 = Trip("Hyd","Gnt" ,550)
print(Trip1.describe())
 
Ans :
Hyd Gnt 550
**********************************
class Company:
    def __init__(self,CompanyName,Add):
        self.CompanyName = CompanyName
        self.Add = Add
 
    def describe(self):
        return f"{self.CompanyName} {self.Add}"
class Employee(Company):
    def __init__(self,CompanyName,Add,Dept):
        super().__init__(CompanyName,Add)
        self.Dept = Dept
 
    def describe(self):
        base = super().describe()  
        return f" {base} {self.Dept}"
   
Loc = Employee("UST","Hyd","HR")
print(Loc.describe())
 
     
Ans
 
UST Hyd HR
**********************************
class school:
    def __init__(self,StudentName,ParentName):
        self.StudentName = StudentName
        self.ParentName = ParentName
    def describe(self):
        return f"{self.StudentName} {self.ParentName}"
class Student(school):
    def __init__(self,StudentName,ParentName,Class):
        super().__init__(StudentName,ParentName)
        self.Class = Class

    def describe(self):
        base = super().describe()
        return f" {base} {self.Class}"
    
class Parent(school):
    def __init__(self,StudentName,ParentName,Class,Add):
        super().__init__(StudentName,ParentName)
        self.Class = Class
        self.Add = Add

    def describe(self):
        base = super().describe()
        return f"{base} {self.Class} {self.Add}"
    
Result = Parent("Veda","Chary","2nd","Hyd")
print(Result.describe())

Ans :
    Veda Chary 2nd Hyd
**********************************
class office:
    def __init__(self,Emp,Add):
        self.Emp = Emp
        self.Add = Add
    def describe(self):
        return f"{self.Emp} {self.Add}"
    
class Employee(office):
    def __init__(self,Emp,Add,Dept):
        super().__init__(Emp,Add)
        self.Dept = Dept
    def describe(self):
        base = super().describe()
        return f" {base} {self.Dept}"  
class Department(Employee):
    def __init__(self,Emp,Add,Dept,Sal):
        super().__init__(Emp,Add,Dept)
        self.Dept = Dept
        self.Sal = Sal
    def describe(self):       
         base = super().describe()
         return f" {base} {self.Dept} {self.Sal}"        
Loc = Department("siba","Hyd","Hr",10000)
print(Loc.describe())
Loc = Department("Jana","Hyd","Dev",90000)
print(Loc.describe())
Loc = Department("shabeera","Hyd","Lead",12000)
print(Loc.describe())
Loc = Department("Ram","Bang","Dev",13000)
print(Loc.describe())

Ans :
    
    esktop/Demo/1.py
  siba Hyd Hr Hr 10000
  Jana Hyd Dev Dev 90000
  shabeera Hyd Lead Lead 12000
  Ram Bang Dev Dev 13000
  
  **********************************************
  
  Generator Functions 
  
  def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)
    
    #Print(hello world)
    ANS :
    esktop/Demo/1.py
1
2
3
4
5
  **********************************************
  **********************************************
  **********************************************
  **********************************************
  **********************************************
  **********************************************
  **********************************************