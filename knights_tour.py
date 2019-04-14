import numpy as np;

class Board:
	def __init__(self, rows, columns):
		self.rows = [[1] * rows for i in range(columns)]

	def __repr__(self):
		print(self.rows)

testBoard = Board(5,4)
testBoard.__repr__()