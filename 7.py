def name(fname,lname):
    print("Hello,",fname,lname)
    
    
name("Rehman","Nawaz")

def isgreater(num1,num2):
  if num1 > num2:
      print("First Number is greater than Second")
  else:
      print("Second is greater")

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
isgreater(a,b)

def Mtable(number1,limit=10):

 print(f"\n Multiplication table of {number1} till {limit}: \n")
 for i in range(1, limit+1):
     print({number1},"x",{i}, "=" ,{number1 * i})
     
v=int(input("Enter number whose multiplication table you want to find:"))
Mtable(v)
 

def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operator"

a=int(input("Enter 1 number:"))
b=int(input("Enter 2 number:"))
c=str(input("Enter operation:"))
print(calculator(a,b,c))
 
 
 
 
 

