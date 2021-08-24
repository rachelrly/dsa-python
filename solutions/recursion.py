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

    # base case: end of maze
    if maze[row][col] == 'e':
        print('End of game', res)
        return res
    # end of line, go down
    elif col + 1 >= col_len:
        res += 'D'
        solve_maze(maze, row + 1, col, res)
    # can't go down, go left
    elif row >= row_len - 1:
        res += 'L'
        solve_maze(maze, row, col - 1, res)
    # next is empty, go right
    elif maze[row][col + 1] == ' ':
        res += 'R'
        solve_maze(maze, row, col + 1, res)
    # otherwise, go down
    else:
        res += 'D'
        solve_maze(maze, row + 1, col, res)


small_maze = [[' ', ' ', ' '], [' ', '*', ' '], [' ', ' ', 'e']]

large_maze = [[' ', ' ', ' ', '*', ' ', ' ', ' '],
              ['*', '*', ' ', '*', ' ', '*', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', '*', '*', '*', '*', '*', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', 'e']]

# solve_maze(large_maze)

# Solve all paths to the maze


def solve_all_maze_paths(maze):
    paths = set()

    def solve_paths(col=0, row=0, str=''):
        row_len = len(maze)
        col_len = len(maze[row])

        # base case: end of maze
        if maze[row][col] == 'e':
            paths.add(res)
            return
        # end of line, go down
        # LIMIT FOR ALL PATHS
        elif col + 1 >= col_len:
            res += 'D'
            solve_paths(maze, row + 1, col, res)

            #if col+1 good go there
            # if row+1 good duplicate str and go there
            # if col-1 duplicate str and go there
        # can't go down, go left
        elif row >= row_len - 1:
            res += 'L'
            solve_paths(maze, row, col - 1, res)
        # next is empty, go right
        elif maze[row][col + 1] == ' ':
            res += 'R'
            solve_paths(maze, row, col + 1, res)
        # otherwise, go down
        else:
            res += 'D'
            solve_paths(maze, row + 1, col, res)

    print(paths)
    return paths