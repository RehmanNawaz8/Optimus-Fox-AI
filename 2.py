c= input("Enter your name: ")
a= "!Rehman!!!"
print(len(c))
print(c.upper())
print(c.lower())
print(c.rstrip("!"))
print(c.replace("Rehman","Nawaz"))
b= "rehmannawaz"
print(b.capitalize())
print(b.center(50))
print(b.count("n"))
print(a.endswith("!!!"))




# Makeing an if program

age = int(input('Enter your Age:'))
if age < 18:
  print('Cant Vote, Your underage ')
elif age > 18:
    print('You can vote')
else:
    print('Invalid age')


