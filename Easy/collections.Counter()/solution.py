# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

num_shoes = int(input())
shoe_sizes = Counter(map(int, input().split()))
num_customers = int(input())

total_sale = 0
for i in range(num_customers):
    size, cost = map(int, (input().split()))
    if shoe_sizes[size]:
        total_sale += cost
        shoe_sizes[size] -= 1
print(total_sale)
