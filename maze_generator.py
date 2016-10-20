# Code by Erik Sweet and Bill Basener

import random
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

num_rows = int(input("Rows: ")) # number of rows
num_cols = int(input("Columns: ")) # number of columns

M = np.zeros((num_rows,num_cols,5), dtype=np.uint8)
# The array M is going to hold the array information for each cell.
# The first four coordinates tell if walls exist on those sides
# and the fifth indicates if the cell has been visited in the search.
# M(LEFT, UP, RIGHT, DOWN, CHECK_IF_VISITED)
image = np.zeros((num_rows*10,num_cols*10), dtype=np.uint8)
# The array image is going to be the output image to display

# Set starting row and column
r = 0
c = 0

# Here goes your implementation



# Open the walls at the start and finish
M[0,0,0] = 1
M[num_rows-1,num_cols-1,2] = 1

# Generate the image for display
for row in range(0,num_rows):
    for col in range(0,num_cols):
        cell_data = M[row,col]
        for i in range(10*row+1,10*row+9):
            image[i,range(10*col+1,10*col+9)] = 255
            if cell_data[0] == 1:image[range(10*row+1,10*row+9),10*col] = 255
            if cell_data[1] == 1:image[10*row,range(10*col+1,10*col+9)] = 255
            if cell_data[2] == 1:image[range(10*row+1,10*row+9),10*col+9] = 255
            if cell_data[3] == 1:image[10*row+9,range(10*col+1,10*col+9)] = 255

# Display the image
plt.imshow(image, cmap = cm.Greys_r, interpolation='none')
plt.show()
