def merge_the_tools(string, k):
    split_strings = []
    for index in range(0, len(string), k):
        split_strings.append(string[index:index+k])
   
    for sub_str in split_strings:
        dup_rmv = ""
        for letter in sub_str:
            if letter not in dup_rmv:
                dup_rmv += letter
        print(dup_rmv)
        dup_rmv = ""
