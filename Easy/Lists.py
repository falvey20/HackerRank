if __name__ == '__main__':
    N = int(input())
    
    myList = [];
    for i in range(0,N):
        ip = input().split()
        if ip[0] == "print":
            print(myList)
        elif ip[0] == "insert":
            myList.insert(int(ip[1]),int(ip[2]))
        elif ip[0] == "remove":
            myList.remove(int(ip[1]))
        elif ip[0] == "pop":
            myList.pop()
        elif ip[0] == "append":
            myList.append(int(ip[1]))
        elif ip[0] == "sort":
            myList.sort()
        else:
            myList.reverse()
