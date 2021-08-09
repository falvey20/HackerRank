def average(array):
    sum_unique_arr = sum(set(array))
    len_unique_arr = len(set(array))
    output = sum_unique_arr/len_unique_arr
    return output

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
