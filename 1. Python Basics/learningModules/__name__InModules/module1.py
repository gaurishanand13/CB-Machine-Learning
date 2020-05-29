

print(__name__)

#Note if (__name__ is run for the module in which we are acutally in , then it would be '__main__'. But if this (__name__) is run in this module by a different
#module for this module, then it won't be '__main__'

if __name__=='__main__':
   print("__name__ is run from the same module")
else:
   print("__name__ is run from the different module")
