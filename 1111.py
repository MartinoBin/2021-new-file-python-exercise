def factorial(n):

    return 1 if (n==1 or n==0) else n*factorial(n-1);

num=int(input('Give a number:'))

print('Factorial of', num, 'is',factorial(num))



