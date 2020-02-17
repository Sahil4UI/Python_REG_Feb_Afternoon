'''n = 123
sum1 = 0
for i in range(0,3):
    rem = n%10
    sum1 += rem
    #sum1 = sum1+rem
    n = n//10
print(sum1)
n = input("enter any number")
length =  len(n)

sum1 = 0
for i in range(1,length+1):
    rem = int(n)%10
    sum1 += rem
    n = int(n)//10
print(sum1)
'''
n = int(input("enter any number"))
sum1 = 0
for i in range(1,len(str(n))+1):
    rem = n%10
    sum1 += rem
    #sum1 = sum1+rem
    n = n//10
    

