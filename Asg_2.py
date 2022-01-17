question 1

a) Find the length of the input string

n=input(" Enter string: ")
x=len(n)
print(x)

b) Reverse the order of the string in one line code

y=n[::-1]
print(y)

c) using slice function store " a case sensitive" in new string

z=slice(10,26)
s=" "
print(str(s) + str(n[z]))

d) Replace "a case sensitive" with "object oriented"

c="object oriented"
a=n.replace("a case sensitive" , c)
print(a)

e) Find index of substring "a" in a given input string

v=n.index("a")
v

f) Remove the white spaces from the given input string¶

def remove(n):
    return n.replace(" ","")
print(remove(n))


question 2

name="Rahul"
sid="18104107"
Dept_name="Electrical"
CGPA="7.8"
text1="Hey, {0} here!\nMy SID is {1}\nI am from {2} department and my CGPA is {3}".format(name,sid,Dept_name,CGPA)
print(text1)

question 3

A)

a=56 	#binary 111000, decimal 56
b=10 	#binary 001010, decimal 10
print(a&b)  # a And b , binary 001000(8-decimal)

B)

print(a|b) # a or b, binary 111010 (58-decimal)

C)

print(a^b) # a xor b , binary 110010 (50-decimal)

D)

print(a<<2) #1st time left shift 1110000(112-decimal),2nd time left shift 11100000(224-decimal)
print(b<<2) #1st time left shift 010100(20-decimal), 2nd time left shift 101000(40-decimal)

E)

print(a>>2) #1st right shift 011100(28-decimal),2nd time right shift (14-decimal)
print(b>>4) #1st right shift 011100(5-decimal),2nd time right shift (2-decimal)

question 4

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
if a>b and a>c:
    print(a, "is greater than", b ,"and", c)
elif b>c and b>a:
    print(b, "is greater than", c ,"and" , a)
else:
     print(c, "is greater than", a ,"and" , b)

question 5

string=input("Enter a string: ")
name=input("enter name: ")
if name in string:
    print("Yes")
else:
    print("No")

question 6

x=float(input("Enter 1st length: "))
y=float(input("Enter 2nd length: "))
z=float(input("Enter 3rd length: "))
print("\n")
if x>(y+z) or y>(x+z) or z>(x+y):
    print("No")
else:
    print("Yes")
    print(int(x))
    print(int(y))
    print(int(z))
