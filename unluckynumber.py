import math
unlucky = 0
low = 0
high = 2
n=int(input())
while( n > high):
    diff = high - low
    low,high = high,high+diff*2
    

binvalue = bin(n-low-1).split('b')[-1]
bit = math.log(low+2)/math.log(2)
if len(binvalue) != bit:
    binvalue = '0'*(int(bit)-len(binvalue)) + binvalue

binvalue = binvalue.replace('1','3')
binvalue = binvalue.replace('0','1')

print(binvalue)
