# Enter your code here. Read input from STDIN. Print output to STDOUT
lines, width = map(int, input().split())

for i in range(1, lines, 2):
    print((".|." * i).center(width, "-"))
print(("WELCOME").center(width, "-"))
for i in range(lines-2, 0, -2):
    print((".|." * i).center(width, "-"))
