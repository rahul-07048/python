Question 1

string=input("enter name: ")
char=input("enter letter: ")
count=0
for i in range(len(string)):
    if string[i]==char:
        count=count+1
print(count)


Question 2

year=int(input("enter year: "))
month=int(input("enter month (1-12): "))
day=int(input("enter day (1-31): "))
if (year%4==0):
    leap_year=True
elif (year%100==0):
    leap_year=False
elif (year%400==0):
    leap_year=True
else:
    leap_year=False

if month in (2,4,6,9,11): 
    month_length=30
elif month==2:
    if leap_year:
        month_length=29
    else:
        month_length=28
else:
    month_length=31
    
if day<month_length:
    day=day+1
else:
    day=1
    if month==12:
        month=1
        year=year+1
    else:
        month=month+1
print("Next date is [dd-mm-yyyy] %d-%d-%d." %(day,month,year))
    


Question 3


numbers=[3,9,10,12,23]
square=[3*3,9*9,10*10,12*12,23*23]
x=zip(numbers,square)
print(list(x))



Question 4


Grade=int(input("Grade- "))

try: 
    
    if Grade==10:
        print("Grade is A+ and Outstanding Performance. ")
    elif Grade==9:
        print("Grade is A and Excellent Performance. ")
    elif Grade==8:
        print("Grade is B+ and Very Good Performance. ")
    elif Grade==7:
        print("Grade is B and Good Performance. ")
    elif Grade==6:
        print("Grade is C+ and Average Performance. ")
    elif Grade==5:
        print("Grade is C and Below Average Performance. ")
    elif Grade==4:
        print("Grade is D and Poor Performance. ")
    
except:
    print("error message.")


Question 5


rows=int(input("enter rows: "))
for i in range(rows):
    print(" "*i,end='')
    for j in range(rows-2*i):
        print(chr(65+j),end='')
    print()
    


Question 6


sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}

while True:
    wish = input("Do you want to enter another student details(Y or N): ").upper()
    if wish == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif wish == 'N':
        break
    else:
     print('Invalid input!!!')

#a-part

print("a." ,students)

#b-part

print("b." ,{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#c-part

print("c." ,{k:v for k,v in sorted(students.items())})

#d-part

search = int(input("Please Enter SID Of The Student You Want To Search: " ))
print("d. Student With The Given SID Is: " ,students[search])



#QUESTION 7

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
terms=int(input("Enter The Number Of Terms In The Seires: "))
if (terms <= 0):    
   print("Plese enter a positive integer!")
else:
   print("Resultant Fibonacci sequence: ")
   sum=0
   for i in range(terms):
       print(fibo(i))
       sum=sum+fibo(i)
avg=float(sum/terms)
print("Average Of The Resultant Fibonacci Series = ",avg)




#QUESTION 8

Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}

# a part

A_Set = (Set1|Set2)-(Set1&Set2)
print("a. ", A_Set)

# b part

B_Set = (Set1|Set2|Set3) - ((Set1&Set2)|(Set2&Set3)|(Set3&Set1))
print("b. ", B_Set)

# c part

C_Set= ((Set1&Set2)|(Set1&Set3)|(Set3&Set2))-(Set1&Set2&Set3)
print("c. ",C_Set)

# d part

D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        D_Set.add(i)
print("d. ", D_Set)

# e part

E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        E_Set.add(i)
print("e. ", E_Set)
