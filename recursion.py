from functools import lru_cache

# LEFT OFF AT 8. Find a way out of the maze


# Counting Sheep
def counting_sheep(num):
    # base case
    if num <= 0:
        print('All sheep have jumped over the fence')
        return None
    # recurse
    print('Another sheep jumps over the fence')
    counting_sheep(num - 1)


#counting_sheep(5)


def counting_sheep_iterative(num):
    count = num
    while (count > 0):
        print('Another sheep jumps over the fence')
        count -= 1
    print('All sheep have jumped over the fence')


# Power Calculator
def power_calculator(base, exp, total=1):
    #base case
    if exp <= 0:
        print(total)
        return total

    total = total * base
    power_calculator(base, exp - 1, total)


# power_calculator(10, 2)


# Reverse String
def reverse_string(str, rts='', i=1):
    n = i * -1
    rts = rts + str[n]
    i = i + 1
    # base case below to use negative indexing
    # and catch last item
    if i > len(str):
        return rts
    reverse_string(str, rts, i)


#reverse_string('trial')

# Fibonacci


#caches first 1000 values
@lru_cache(maxsize=1000)
def fibonacci(n):
    # check type and type error
    if type(n) != int:
        raise TypeError("Input must be a positive integer")
    # check value and value error
    elif n < 1:
        raise ValueError("Input must be a positive integer")

    elif n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


#fibonacci(8)

# Factorial


def factorial(n, product=1):
    if n <= 0:
        print(product)
        return product
    product *= n
    n -= 1
    factorial(n, product)


#factorial(8)

# Find a way ouy of the maze


def solve_maze(maze, row=0, col=0, res=''):

    row_len = len(maze)
    col_len = len(maze[row])

    #is a space
    if maze[row][col] == ' ':
        if col >= col_len - 1:
            res += 'D'
            solve_maze(maze, row + 1, col, res)
        else:
            res += 'R'
            solve_maze(maze, row, col + 1, res)

    elif maze[row][col] == 'e':
        print('End of game', res)
        return res

    else:
        res += 'D'
        solve_maze(maze, row + 1, col, res)


small_maze = [[' ', ' ', ' '], [' ', '*', ' '], [' ', ' ', 'e']]

large_maze = [[' ', ' ', ' ', '*', ' ', ' ', ' '],
              ['*', '*', ' ', '*', ' ', '*', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', '*', '*', '*', '*', '*', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', 'e']]

solve_maze(large_maze)