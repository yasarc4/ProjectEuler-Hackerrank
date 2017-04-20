#https://www.hackerrank.com/contests/projecteuler/challenges/euler011
import sys

maxi=0
grid = []
for grid_i in xrange(20):
    grid_temp = map(int,raw_input().strip().split(' '))
    grid.append(grid_temp)

for i in range(0,20):
    for j in range(0,20):
        if(j<17):
            temp = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            if (temp>maxi):
                maxi=temp
        if(i<17):
            temp = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
            if(temp>>maxi):
                maxi=temp
        if(j<17) and (i<17):
            temp = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            if(temp>maxi):
                maxi=temp
        if(j<17) and (i>2):
            temp = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
            if(temp>maxi):
                maxi=temp

print maxi
