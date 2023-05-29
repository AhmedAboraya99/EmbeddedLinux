#receive input from cmd
n1, n2 = input("Please Enter Two Numbers\n").split(" ",2)
n1 = int(n1)
n2 = int(n2)

#Math operations
sum = n1+n2
print("sum", sum)

sub = n1-n2
print("sub",sub)

div = n1/n2
print("div",div)

mul = n1*n2
print("mul", mul)

pow = n1**n2
print("power", pow)

mod = n1%n2
print("mod", mod)

#floor divison
floor = (n1//n2)
print("floor =", floor)

#Bitwise operations
AND = n1&n2
print("and = ", AND)

OR = n1|n2
print("\n or", OR)

XOR = n1^n2
print("xor = ",XOR)

SHIFT_LEFT = n1<<n2
print("SHIFT_RIGHT", SHIFT_LEFT)

SHIFT_RIGHT = n1>>n2
print("SHIFT_RIGHT", SHIFT_RIGHT)

#Relational operations
eq = n1==n2
print("Equal = ", eq)

neq = n1!=n2
print("not Equal = ", neq)

smaller = n1<=n2
print("smaller =", smaller)

bigger = n1>=n2
print("bigger = ", bigger)