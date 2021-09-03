if __name__ == '__main__':
    
    scores_list = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores_list.append([name, score])
        
    second_lowest = sorted(set(score for name, score in scores_list))[1]
    print('\n'.join(sorted(name for name, score in scores_list if score == second_lowest)))
