number=int(input('Give a number:'))

def check_armstrong(num):
    if num in range(1,10):
        return True
    
    order=len(str(num))
    sum=0

    original=num
    while num>0:
        digit=num%10
        sum+=pow(digit,order)
        num=num//10

    if sum == original:
        return True
    else:
        return False

if check_armstrong(number):
    print('This is armstrong number')
else:
    print('This is not armstrong number')
        

