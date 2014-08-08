import math

n = int(input('please input the n which is the root:'))
times = input('please input the times want to improve:')
guess = float(n)
print('the 1 guess is :', guess)

for i in range(0, n):
    guess = (guess + n / guess) / 2
    print('the ' + str(i + 2) + ' guess is : ', guess)
    
print('the root of ', n, ' is ', guess)
print('the root of ', n, ' computed from math is ', math.sqrt(n)) 
