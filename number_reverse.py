#ArmStrong Number
a = 153
temp = 0
for i in range(1,4):
    rem = a%10
    temp += rem**3
    a = a//10

if temp ==a:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

