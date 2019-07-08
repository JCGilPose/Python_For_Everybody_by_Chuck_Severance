import re

handle = open('regex_sum_209274.txt')

num_list = list()
sum = 0
#count = 0

for line in handle:
    line = line.rstrip()
    num_strings = re.findall('([0-9]+)', line)
    for i in num_strings:
        num = int(i)
        num_list.append(num)
    
for number in num_list:
    sum += number
 #   count += 1

#print("There are", count, "numbers in this file.")
print(sum)