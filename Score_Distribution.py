import math
import random

n = int(input("Input the number of students: "))
s_avg = [random.uniform(0, 10) for _ in range(n)]

total = sum(s_avg)
heighest = max(s_avg)
lowest = min(s_avg)
avg = total / n

print("Total Score: " + str(round(total, 2)))
print("Heighest Score: " + str(round(heighest,2)))
print("Lowest Score: " + str(round(lowest, 2)))
print("Average: " + str(round(avg,2)))

for s in s_avg:
    if s >= 9.0:
        print("A")
    elif s >= 8.0:
        print('B')
    elif s >= 7.0:
        print('C')
    elif s >= 6.0:
        print('D')
    else:
        print('F')
