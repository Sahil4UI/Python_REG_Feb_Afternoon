#write a program to print first 20 numbers skipping the ,multiple of 5
for i in range(1,21):
    if (i%5==0):
        continue
    print(i)

