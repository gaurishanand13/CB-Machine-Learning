#Note - sys module provides us the information related to system and python interpretor
import sys


## Note --> sys.argv is a list
print(type(sys.argv))    #At sys.argv[0] we have the name of the file in which we are calling this. i.e sys.argv[0] = 'module3_sys_Module.py'
#Now we must be wondering what are the other values in sys.argv? It is the same argv[0] which is present by default in java main or c++ main,
#but we never use it. Like when we run this file by writing the command ==> python module3_sys_Module.py 10 hello 30, then in this case
##sys.args[0] is file_name
##sys.args[1] is 10
##sys.args[2] is hello
##sys.args[3] is 30


print(sys.argv)
print(int(sys.argv[1]) + int(sys.argv[3]))

print()
print(sys.version)#It would print the current version of python installed in the system
print(sys.path)#Interpreter would list all the packages in the path , it searches for. If the module we are importing is not those paths
#then then interpreter would not be able to import that module



print()
print()

print(sys.maxsize)
##Therefore stdin and stdout are used to input and output
print(sys.stdin)
print(sys.stdout)

