from flask import Flask, render_template, request, redirect
from datetime import datetime
import solver

app = Flask(__name__)                 

@app.route("/", methods=['GET','POST'])
def solverSudoku():
    
    error=None
    range_n_rows = range(9)
    
    if request.method == 'POST':
        grid = []
        for row in range(1,10):
            row_content = []
            for column in range(1,10):
                #Generate html class name and obtain from template
                html_class = 'row' + str(row) + 'column' + str(column)
                try:
                    value = int(request.form.get(html_class))
                #Prevent invalid inputs
                except ValueError:
                    value = 0
                if value not in range(0,10):
                    value = 0
                row_content.append(value)
            grid.append(row_content)
        #Check if duplicate values break sudoku rules
        if solver.isNotDuplicate(puzzle=grid):
            solved_sudoku = solver.Solve()
            solved_sudoku.solveSudoku(grid)
        else:
            error='Unsolvable Sudoku!'
        return render_template('sudoku.html', range_n_rows=range_n_rows, grid=grid, error=error)


    return render_template('sudoku.html', range_n_rows=range_n_rows)