#  File: Triangle.py

#  Description: Four types of algorithms were used to determine the path with the greatest sum for the triangle: brute force, greedy, divide and conquer, and dynamic programming

#  Student Name: Vaishnav Sathiyamoorthy

#  Student UT EID: vs25229

#  Partner Name: Saivachan Ponnapalli

#  Partner UT EID: sp48347

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 10/9/2022

#  Date Last Modified: 10/10/2022

import sys

from timeit import timeit


# returns the greatest path sum using exhaustive search
def brute_force (grid):
    overall=[]
    brute_force_helper (grid,overall,0,0,0)
    return max(overall)
    
def brute_force_helper (grid,overall,sums,index,sub):
    sums=sums+grid[index][sub]
    if (index==len(grid)-1):
        overall.append(sums)
    else:
        return brute_force_helper(grid, overall, sums, index+1, sub+1) or brute_force_helper(grid, overall, sums, index+1, sub)

# returns the greatest path sum using greedy approach
def greedy(grid):
    # The max of the 2 next to each other are taken and then added to the overall total
    total = grid[0][0]
    previous_index = 0
    for row in range(1, len(grid)):
        if grid[row][previous_index] > grid[row][previous_index+1]:
            total += grid[row][previous_index]
        else:
            total += grid[row][previous_index+1]
            previous_index += 1
    return total

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer(grid):
    # The helper function is called
    return divide_conquer_helper(grid, 0, 0)

def divide_conquer_helper(grid, row, col):
    # The base case of when it gets to the last row. If the row = col, then the number will just be returned. Otherwise, max of the 2 numbers is returned
    if row == len(grid) - 1:
        if row == col:
            return grid[row][col]
        elif grid[row][col] > grid[row][col + 1]:
            return grid[row][col]
        else:
            return grid[row][col + 1]
    else:
        # This recursive case takes the max of the next 2 numbers on the next row and adds it to the total
        return grid[row][col] + max(divide_conquer_helper(grid, row+1, col), divide_conquer_helper(grid, row+1, col+1))

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    # This is a bottom to top approach
    overall = grid[len(grid) - 1]
    for i in range(len(grid) - 1, 0, -1):
        first = grid[i - 1]
        second = overall
        overall = []
        for j in range(i):
            overall.append(max(first[j] + second[j], first[j] + second[j + 1]))
    return overall[0]

# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create an empty grid with 0's
    grid = [[0 for i in range(n)] for j in range(n)]

    # read each line in the input file and add to the grid
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list(map(int, row))
        for j in range(len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid


def main():
    # read triangular grid from file
    grid = read_file()

    '''
    # check that the grid was read in properly
    print (grid)
    '''
    # output greatest path from exhaustive search
    times = timeit('brute_force({})'.format(grid), 'from __main__ import brute_force', number=10)
    times = times / 10
    # print time taken using exhaustive search
    print("The greatest path sum through exhaustive search is")
    print(brute_force(grid))
    print("The time taken for exhaustive search in seconds is")
    print(times)

    # output greatest path from greedy approach
    times = timeit('greedy({})'.format(grid), 'from __main__ import greedy', number=10)
    times = times / 10
    print("The greatest path sum through greedy search is")
    print(greedy(grid))
    print("The time taken for greedy search in seconds is")
    print(times)

    # output greatest path from divide-and-conquer approach
    times = timeit('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number=10)
    times = times / 10
    # print time taken using divide-and-conquer approach
    print("The greatest path sum through divide and conquer approach is")
    print(divide_conquer(grid))
    print("The time taken for divide and conquer approach in seconds is")
    print(times)

    # output greatest path from dynamic programming
    times = timeit('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number=10)
    times = times / 10
    print("The greatest path sum through dynamic programming is")
    print(dynamic_prog(grid))
    print("The time taken for dynamic programming in seconds is")
    print(times)

if __name__ == "__main__":
    main()
