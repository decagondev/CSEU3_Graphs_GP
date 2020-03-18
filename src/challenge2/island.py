class Stack():
    pass

def island_counter(matrix):
    # create a visited matrix
    # walk through each cell in the matrix
        # if it has not been visited...
            # when i reach a 1...
                # do a dft and mark each as visited
                # then increment a counter
    pass

def dft(row, col, matrix, visited):
    '''
    This will mark each connected component as visited
    Return visited matrix
    '''
    # Create an empty stack

    # push the starting vertex on to the stack eg (row, col)

    # while stack is not empty
        # pop the first vertex from the top of the stack

        # if it has not been visited
            # mark it as visited

            # then push each '1' neighbor on to the top of the stack
            # maybe break down or decompose in to a get neighbors function
    
    # return visited
    pass

# HINT to do a 2d list you can just write it like this books[row][col] col = east and west, row = north and south
def get_neighbors(row, col, graph_matrix):
    # create a neighbors list

    # check north

    # check south

    # check east

    # check west

    # return the neighbors
    pass

# tests

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands)  # 4

islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

island_counter(islands)  # 13