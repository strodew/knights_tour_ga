import numpy as np;

class Board:
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.squares = [[0] * columns for i in range(rows)]

	def __repr__(self):
		for i in range(self.rows):
			print(self.squares[i])

class Tour:
	def __init__(self,start):
		self.start = start
		self.tour = []
		self.fitness = 0
		
		self.board = Board(8,8)
		(row, column) = self.start
		self.board.squares[column - 1][row - 1] = 1
		
		self.board.__repr__()

	def tourFitness(self):
		if self.fitness == 0:
			self.fitness = len(self.tour)
		return self.fitness

testRt = Tour((5,7))