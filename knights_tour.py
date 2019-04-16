'''
Genetic algorithm for solving the Knight's Tour problem
'''

class Board:
	'''
	Class for a chessboard with an integer number of rows and columns.
	Includes a method to display the board in the console. self.squares
	contains the board as a nested list populated with the string '00'
	'''
	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.squares = [['00'] * columns for i in range(rows)]

	def __repr__(self):
		for i in range(self.rows):
			print(self.squares[i])

class Tour:
	'''
	Class for an individual candidate tour. Instantiates a board for the
	tour using the Board class above. Each move is encoded as a 3-bit binary
	string - details of the encoding can be found in the paper for which
	this algorithm was produced - see header.

	Contains methods isLegalMove(), tourFitness() and generateTour()
	'''
	def __init__(self,start):
		self.start = start
		self.pos = start
		self.tour = []
		self.fitness = 0
		
		self.board = Board(8,8)
		(row, column) = self.start
		self.board.squares[column - 1][row - 1] = '01'
		
		self.board.__repr__()

	def isLegalMove(self,move):
		moves = [(1,2), (2,1), (2,-1), (1,-2),
		 (-1,-2), (-2,-1), (-2,1), (-1,2)]
		
		decMove = int(move,2)
		moveTup = moves[decMove]

		testPos0 = self.pos[0] + moveTup[0]
		testPos1 = self.pos[1] + moveTup[1]

		if testPos0 > 0 and testPos0 <= 8 and testPos1 > 0 and testPos1 <= 8:
			return True
		else:
			return False

	#def generateTour(self):
	#	while len(self.tour) < 63:


	def tourFitness(self):
		if self.fitness == 0:
			self.fitness = len(self.tour)
		return self.fitness


#Testing statements below

testRt = Tour((1,1))
testBin = bin(4)
print(testRt.isLegalMove(testBin))