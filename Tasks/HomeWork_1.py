#Task №1
import random

list = []
for i in range(10):
    list.append(random.random())

max_list = max(list)
min_list = min(list)
mid_list = sum(list)/10

print(min_list)
print(mid_list)
print(max_list)