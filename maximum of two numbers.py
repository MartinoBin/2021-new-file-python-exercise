num1=input('Give a number:')
num2=input('Give a second number:')

if int(num1)>int(num2):
    print (num1,'is larger than', num2)

if int(num1)==int(num2):

    print (num1,'is equal to', num2)
    
if int(num1)<int(num2):
    print (num2, 'is larger than', num1)

#############

# Method 1

def maximum(a,b):
    if a>=b:
        return a
    else:
        return b

# Driver code

a=2
b=4
print(maximum(a,b))

# Method 2

a=2
b=4

maximum =max(a,b)
print(maximum)
