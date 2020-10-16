type_of_expression = input('Which expression do you want to choose?\n\t"P" to find a perimetr,\n\t"S" to find an area \n>').lower()
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
p = (a+b)*2
s = a*b
if type_of_expression == "p":
    print(p)
elif type_of_expression == "s":
    print(s)
else:
    print(" Invalid expression! ")
