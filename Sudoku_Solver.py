# Bilal Raja 
import copy
#Create Sudoku class
class SudokuGrid(): 
    def __init__(self, source_grid = None): 
        # whenever we create a sudoku grid this will start#
        if source_grid is None:
            # create these 'nine lists'
            self.grid = []
            for i in range (9):
                self.grid.append([None] *9) 
        #check legal grid 
        else:
            if (type(source_grid) !=list):
                raise ValueError("Grid is not a list")
            if (len(source_grid) != 9):
                raise ValueError("Only 9x9 grids for this solver")
            for col in source_grid:
                if (type(col) != list):
                    raise ValueError("Not a list of lists")
                if (len(col) != 9):
                    raise ValueError("not a 9x9 grid")
                for item in col:
                    if (type(item) == int):
                        if item not in range(1,10):
                            raise ValueError("Source Grid does not contain range 1 to 9")
                    elif (item is not None):
                        raise ValueError("Source Grid contains illegal object")
            self.grid = copy.deepcopy(source_grid)  
            
    def _find_subgrids_num(self, col_num,row_num): 
        initial_row = row_num - (row_num % 3) 
        initial_col = col_num - (col_num % 3)
        nums = []
        for i in range(3):
            for j in range(3):
                item = self.grid[initial_col + i][initial_row + j]
                if item is not None:
                    nums.append(item)
        return nums
            
    def get_nums_in_col(self,col_num):
        # want to retrieve all the numbers in the column
        return [item for item in self.grid[col_num] if item is not None]
    
    def get_nums_in_row(self, row_num):
        # get all the numbers in rows by taking it from the cols
        return [col[row_num] for col in self.grid if col[row_num] is not None]
    def get_legal_moves(self,col_num,row_num):
        return [i for i in range(1,10)
            if i not in self.get_nums_in_row(row_num) 
            and i not in self.get_nums_in_col(col_num) 
            and i not in self._find_subgrids_num(col_num, row_num)]
    def find_next_open_square(self):
        # check each col for empty spot otherwise return that col is full
        for i in range(9):
            for j in range(9):
                if self.grid [i][j] is None:
                    return (i,j)
        return (-1, -1)
    
    def set_next_square(self, new_value): 
        if new_value not in range(1,10):
            raise ValueError ("Not a value between 1 to 9")

        (next_col, next_row) = self.find_next_open_square()
        if new_value not in self.get_legal_moves(next_col,next_row):
            raise ValueError("Not a legal move")        
        if next_col == -1:
            raise Exception("Grid is full")
        new_grid = SudokuGrid(self.grid) 
        # new grid is a new Class and new_grid.grid is a grid within this class
        new_grid.grid [next_col][next_row] = new_value
        return new_grid
    def __str__(self):
        repr = ""
        for i in range(9):
            for j in range(9):
                if type(self.grid[j][i]) == int:
                    repr += f' {self.grid[j][i]} '
                else:
                    repr += '.'
            repr += '\n'
        return repr
    
def solve_sudoku(sudoku_grid):
    (next_col, next_row) = sudoku_grid.find_next_open_square()
    if next_col == -1:
        return sudoku_grid
    legal_moves = sudoku_grid.get_legal_moves(next_col,next_row) 
    # create the next few sudoku grids for all the legal moves
    next_stage = [sudoku_grid.set_next_square(i) for i in legal_moves]
        
    for grid in next_stage:
        result = solve_sudoku(grid)
        if result is not None:
            return result
    return None
if __name__ == '__main__':
    sample_grid =\
    [[5, 6, None, 8, 4, 7, None, None, None],
    [3, None, 9, None, None, None, 6, None, None],
    [None, None, 8, None, None, None, None, None, None],
    [None, 1, None, None, 8, None, None, 4, None],
    [7, 9, None, 6, None, 2, None, 1, 8],
    [None, 5, None, None, 3, None, None, 9, None],
    [None, None, None, None, None, None, 2, None, None],
    [None, None, 6, None, None, None, 8, None, 7],
    [None, None, None, 3, 1, 6, None, 5, 9]]    
    answer = solve_sudoku(SudokuGrid(sample_grid))
    print(answer)
    
                
            
                    
          
        
        
        
            
            