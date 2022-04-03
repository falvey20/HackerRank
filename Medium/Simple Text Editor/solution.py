Q = int(input().strip())
S = ''
history = []
    
for i in range(Q):
    args = input().strip().split(' ')
    
    if args[0] == '1':
        S += args[1]
        history.append([args[0], len(args[1])])
    elif args[0] == '2':
        deleted = S[-int(args[1]):]
        S = S[:-int(args[1])]
        history.append([args[0], deleted])
    elif args[0] == '3':
        print(S[int(args[1]) - 1])
    elif args[0] == '4':
        undo = history.pop()
        if undo[0] == '1':
            S = S[:-int(undo[1])]
        elif undo[0] == '2':
            S += undo[1]

