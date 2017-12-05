# problem 1
# Find the sum of all the multiples of 3 or 5 below 1000
target =999
sum = 0
for i in range(target):
    if (i%3 == 0 or i%5 == 0):
        sum=sum+i
print(sum)