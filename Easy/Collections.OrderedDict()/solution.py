from collections import OrderedDict

N = int(input())
od = OrderedDict()

for _ in range(N):
    item_name, net_price = input().rsplit(" ", 1)
    if item_name not in od:
        od[item_name] = int(net_price)
    else:
        od[item_name] += int(net_price)
        
for item in od.keys():
    print(item, od[item])
