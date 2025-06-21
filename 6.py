x = ['apple', 'mango']
for i in x:
    print(i)
    for fruits in i:
        print(fruits)
        
for a in range(0, 21, 3):
    print(a)
    # third value represents n-1 values will be left in itration
    
num = int(input("Enter a number to print its table: "))
limit = int(input("Enter the range (e.g., 10): "))

print(f"\nMultiplication Table of {num}:\n")

for i in range(1, limit + 1):
    print(f"{num} x {i} = {num * i}")
