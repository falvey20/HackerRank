for i in range(int(input())):
    try:
        a,b = map(int, input().split())
        print(a//b)
    except Exception as err:
        print("Error Code:", err)
