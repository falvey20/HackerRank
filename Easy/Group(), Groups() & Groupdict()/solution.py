import re

S = input()
subs = re.search(r"([a-zA-Z0-9])\1+", S)

if subs:
    print(subs.group(1))
else:
    print(-1)
