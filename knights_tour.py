import numpy as np;

class Board:
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.squares = [[0] * columns for i in range(rows)]

	def __repr__(self):
		for i in range(self.rows):
			print(self.squares[i])

testBoard = Board(8,8)
testBoard.__repr__()