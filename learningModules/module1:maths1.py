#Now we would learn about modules. Modules are basically header files of c++. We import them to use the functionalities in them.
#Now first we would learn about some commanly used modules


#import math
#print("Factorial of 10 is",math.factorial(5))
#print("Floor of 15/2 is",math.floor(15/2))



#Now insetead of writing math.function_name() everytime, why don't we simply import all the statements as it is in this file(i.e in this python module). Eg-
from math import * #It will import whole code from the math module to it as it is i.e copy the lines above and then start
#All the functions discussed from here are imported from math module


print("Factorial of 10 is",factorial(5))

print("Floor of 15/2 is",floor(15/2))

print("GCD of 16 and 24 is",gcd(16,24))

print("Value of 20 to the base e is",log(10))
print("Value of e to the base e is",log(e)) #If we have simply imported math module using import math -> Then e could have been accessed by math.e
#If we want that base if different from e. Then we can import it like this ->
base = 10
print("Value of 100 to the base 10 is",log(100,base))


print()
#Now some more values which are in maths module are == pi,inf,-inf
print(pi)
print(inf) #inf can't ne represented, but it will be the most positive number in python
print(-inf)#most negative number in python

