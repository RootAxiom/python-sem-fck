

# ✅ **1. Factorial**

```python
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)
```

---

# ✅ **2. Prime Check**

```python
n = int(input())
flag = True

if n <= 1:
    flag = False

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        flag = False
        break

print("Prime" if flag else "Not Prime")
```

---

# ✅ **3. Fibonacci Series (first n terms)**

```python
n = int(input())
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

---

# ✅ **4. GCD of Two Numbers**

### Method 1: Euclid Algorithm

```python
a, b = map(int, input().split())

while b != 0:
    a, b = b, a % b

print(a)
```

---

# ✅ **5. Power (Xⁿ)**

```python
x, n = map(int, input().split())
p = 1

for _ in range(n):
    p *= x

print(p)
```



---

## **1. Factorial of a Number**

```python
n = int(input())
f = 1
for i in range(1, n+1):
    f *= i
print(f)
```

---

## **2. Check Prime Number**

```python
n = int(input())
flag = True
if n <= 1:
    flag = False
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        flag = False
        break
print("Prime" if flag else "Not Prime")
```

---

## **3. Fibonacci Series Using Recursion**

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = int(input())
for i in range(n):
    print(fib(i), end=" ")
```

---

## **4. GCD of Two Numbers**

```python
a, b = map(int, input().split())
while b:
    a, b = b, a % b
print(a)
```

---

## **5. Power X^n**

```python
x, n = map(int, input().split())
p = 1
for _ in range(n):
    p *= x
print(p)
```

---

## **6. 1 + (1+2) + (1+2+3) + ... + n**

```python
n = int(input())
s = 0
for i in range(1, n+1):
    s += sum(range(1, i+1))
print(s)
```

---

## **7. Sum of Digits**

```python
n = input()
print(sum(int(i) for i in n))
```

---

## **8. Reverse of a Number**

```python
n = input()
print(n[::-1])
```

---

## **9. String Palindrome**

```python
s = input()
print("Palindrome" if s == s[::-1] else "Not Palindrome")
```

---

## **10. Multiplication Table**

```python
n = int(input())
for i in range(1, 11):
    print(n, "*", i, "=", n*i)
```

---

## **11. Matrix Multiplication (2x2 example)**

```python
A = []
B = []
for _ in range(2):
    A.append(list(map(int, input().split())))
for _ in range(2):
    B.append(list(map(int, input().split())))

C = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(row)
```

---

## **12. File Copy**

```python
f1 = open("a.txt", "r")
f2 = open("b.txt", "w")
f2.write(f1.read())
f1.close()
f2.close()
```

---

## **13. sin(x) series: x – x^3/3! + x^5/5! …**

```python
import math
x = float(input())
n = int(input())
s = 0
for i in range(n):
    s += ((-1)**i) * (x**(2*i+1)) / math.factorial(2*i+1)
print(s)
```

---

## **14. Expression: 1^2 + 2^2 + 3^2**

```python
n = int(input())
print(sum(i*i for i in range(1, n+1)))
```

---

---

## **1. Leap Year Check**

```python
y = int(input())
if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")
```

---

## **2. Dictionary Creation (Student Name, Roll, Marks)**

```python
d = {}
name = input()
roll = input()
mark = input()
d["name"] = name
d["roll"] = roll
d["mark"] = mark
print(d)
```

---

## **3. Largest Among Three Numbers**

```python
a, b, c = map(int, input().split())
print(max(a, b, c))
```

---

## **4. Armstrong Number**

```python
n = input()
s = sum(int(i)**len(n) for i in n)
print("Armstrong" if s == int(n) else "Not Armstrong")
```

---

## **5. Count Number of Vowels in a String**

```python
s = input().lower()
v = "aeiou"
c = 0
for i in s:
    if i in v:
        c += 1
print(c)
```

---

## **6. Store Student Info in File and Display**

### **Write**

```python
f = open("stud.txt", "w")
name = input()
roll = input()
mark = input()
f.write(name + " " + roll + " " + mark)
f.close()
```

### **Read**

```python
f = open("stud.txt", "r")
print(f.read())
f.close()
```

---

## **7. Bank Account Using Class & Object**

```python
class Bank:
    def __init__(self, name, bal):
        self.name = name
        self.bal = bal

    def deposit(self, amt):
        self.bal += amt

    def withdraw(self, amt):
        if amt <= self.bal:
            self.bal -= amt

    def display(self):
        print(self.name, self.bal)

name = input()
bal = int(input())
obj = Bank(name, bal)

obj.deposit(int(input()))
obj.withdraw(int(input()))
obj.display()
```
