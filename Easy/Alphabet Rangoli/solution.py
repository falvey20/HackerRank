def print_rangoli(size):
    # List of all letters
    letters = list(map(chr, range(97, 123)))
    # Determine longest line
    max_line = letters[size-1::-1] + letters[1:size]
    max_len = len('-'.join(max_line))
    
    # Top Half
    for i in range(1, size):
        print('-'.join(letters[size-1:size-i:-1] + letters[size-i:size]).center(max_len, '-'))
    # Center Line and Bottom Half
    for i in range(size, 0, -1):
        print('-'.join(letters[size-1:size-i:-1] + letters[size-i:size]).center(max_len, '-'))
    
