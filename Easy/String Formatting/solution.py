def print_formatted(number):
    largest_width = len(str(bin(number))[2:])
    for i in range(1, number+1):
        print(str(i).rjust(largest_width, ' '), oct(i)[2:].rjust(largest_width, ' '), hex(i).upper()[2:].rjust(largest_width, ' '), bin(i)[2:].rjust(largest_width, ' '))
