# Refrence:
# https://github.com/JonathanSuen/2D-Lists---Minesweeper/blob/main/minesweeper.py

input_mine = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

rows = len(input_mine)

cols = len(input_mine[0])

output_mine = [row[:] for row in input_mine] # create a copy of input_mine

for i, row in enumerate(input_mine): # this loop starts with checking values in the original matrix, i = row index

    for j, cell in enumerate(row): # j = column index

        if cell == "-": # here we look for "-""

            count = 0 # initialize a counter

            # now we look in a 3*3 grid around the current cell:
            for x in range(i - 1, i + 2): # we look in the x axis [i-1, i+1, i+2], where i-1 is the previous row, i+1 is the current row, and i+2 is the next row

                for y in range(j - 1, j + 2):  # similar to above in the y axis (column) 

                    if 0 <= x < rows and 0 <= y < cols: # check if x and y are within the limits of the original matrix (boundary condition)

                        if input_mine[x][y] == "#": # if we find "#" within the 3*3 grid
                            
                            count += 1 # increment the count by 1

            output_mine[i][j] = str(count) # store the value in output then next j (back to the second for loop)

for i in range(len(output_mine)):
    print(output_mine[i])