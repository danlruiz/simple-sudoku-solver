import numpy as np


class Solve():

        def findNextCellToFill(self, grid, i, j):
                for x in range(i,9):
                        for y in range(j,9):
                                if grid[x][y] == 0:
                                        return x,y
                for x in range(0,9):
                        for y in range(0,9):
                                if grid[x][y] == 0:
                                        return x,y
                return -1,-1

        def isValid(self, grid, i, j, e):
                rowOk = all([e != grid[i][x] for x in range(9)])
                if rowOk:
                        columnOk = all([e != grid[x][j] for x in range(9)])
                        if columnOk:
                                # finding the top left x,y co-ordinates of the section containing the i,j cell
                                secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                                for x in range(secTopX, secTopX+3):
                                        for y in range(secTopY, secTopY+3):
                                                if grid[x][y] == e:
                                                        return False
                                return True
                return False

        def solveSudoku(self,grid, i=0, j=0):
                i,j = self.findNextCellToFill(grid, i, j)
                if i == -1:
                        return True
                for e in range(1,10):
                        if self.isValid(grid,i,j,e):
                                grid[i][j] = e
                                if self.solveSudoku(grid, i, j):
                                        return True
                                # Undo the current cell for backtracking
                                grid[i][j] = 0
                return False



def isNotDuplicate(puzzle):
        #check row
        for row in puzzle:
                row_nums = list(range(1,10))
                for number in row:
                        if number == 0:
                                continue
                        try:
                                row_nums.remove(number)
                        except ValueError:
                                return False
        #check column
        for i in range(9):
                col_nums = list(range(1,10))
                for row in puzzle:
                        if row[i] == 0:
                                continue
                        try:
                                col_nums.remove(row[i])
                        except ValueError:
                                return False
        
        #check sub-grid
        poss1, poss2, poss3 = list(range(10)), list(range(10)), list(range(10))                
        for array in range(9):
                for index in range(3):
                        a, b, c = index, 3 + index, 6 + index
                        if (array == 3 or array == 6) and (prev != array):
                                poss1, poss2, poss3 = list(range(10)), list(range(10)), list(range(10))
                        prev = array
                        if checkPoss(puzzle, poss1, array, index) and checkPoss(puzzle, poss2, array, index) and checkPoss(puzzle, poss3, array, index):
                                pass
                        else:
                                return False
        return True



def checkPoss( puzzle, poss, array, index):
        if puzzle[array][index] == 0:
                return True
        else:
                try:
                        poss.remove(puzzle[array][index])
                        return True
                except ValueError:
                        return False



        
                
                
