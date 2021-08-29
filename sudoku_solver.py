'''
This project allows us to solve any Sudoku puzzle.

The GUI of this project has been created using Tkinter and a backtracking algorithm.
'''

from tkinter import *

root = Tk()
root.geometry('330x370')
  
# Sudoku solver class
class SudokuSolver():

    def __init__(self):
        self.setZero()
        self.solve()
        
    def setZero(self):
        for i in range(9):
            for j in range(9):
                if filledBoard[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    filledBoard[i][j].set(0)

    # Solve using backtracking    
    def solve(self):
        findEmpty = self.emptyCell()
        
        if not findEmpty:
            return True   
        else:
            row, column = findEmpty
        
        for i in range(1,10):
            if self.isValid(i, (row, column)):
                filledBoard[row][column].set(i)

                if self.solve():
                    return True

                filledBoard[row][column].set(0)
        
        return False
         
    def isValid (self, num, pos):
        # Checking Row
        for i in range(9):
            if filledBoard[pos[0]][i].get() == str(num):
                return False
        # Checking Column 
        for i in range(9):
            if filledBoard[i][pos[1]].get() == str(num):
                return False

        # Checking Sub Grid
        row = pos[0] // 3 
        column = pos[1] // 3 

        for i in range(row * 3, (row * 3) + 3):
            for j in range(column * 3, (column * 3) + 3):
                if filledBoard[i][j].get() == str(num):
                    return False 
        return True

    def emptyCell(self):
        for row in range(9):
            for column in range(9):
                if filledBoard[row][column].get() == '0':
                    return (row,column)
        return None

# Interface class
class Interface():
    def __init__(self, window):
        self.window = window
        window.title("Sudoku Solver")

        font = ('Arial', 20)
        color = 'white'

        solve = Button(window, text = 'Solve', command = self.Solve)
        solve.grid(column=3,row=20)
        clear = Button(window, text = 'Clear', command = self.Clear)
        clear.grid(column = 5,row=20)

        self.board  = []
        for row in range(9):
            self.board += [["","","","","","","","",""]]

        for row in range(9):
            for col in range(9):
                if (row < 3 or row > 5) and (col < 3 or col > 5):
                    color = 'white' 
                elif (row >= 3 and row < 6) and (col >=3 and col < 6):
                    color = 'white'
                else:
                    color = 'grey'
                
                self.board[row][col] = Entry(window, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 2,
                                          highlightcolor = 'yellow', highlightthickness = 0, highlightbackground = 'black', 
                                          textvariable = filledBoard[row][col]) 
                self.board[row][col].bind('<FocusIn>', self.gridChecker) 
                self.board[row][col].bind('<Motion>', self.gridChecker)                        
                self.board[row][col].grid(row = row, column = col)


    def gridChecker(self, event):
        for row in range(9):
            for col in range(9):
                if filledBoard[row][col].get() not in ['1','2','3','4','5','6','7','8','9']:
                    filledBoard[row][col].set('')

    
    def Solve(self):
        SudokuSolver()

    def Clear(self):
        for row in range(9):
            for col in range(9):
                filledBoard[row][col].set('')


filledBoard = []
for row in range(9): 
    filledBoard += [["","","","","","","","",""]]
for row in range(9):
    for col in range(9):
        filledBoard[row][col] = StringVar(root)    

# Main Loop
Interface(root)
root.mainloop()



