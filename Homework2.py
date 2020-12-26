list = []
a = input("What is your First Name?")
list.append(a)
b = input("What is your Last Name?")
list.append(b)
c = int(input("Your age?"))
list.append(c)
d = int(input("What is your born year?"))
list.append(d)

for i in list:
    print(i)

if c <= 18:
    print("You can not go out because it is too dangerous")
else:
    print("You can go out to the street")
