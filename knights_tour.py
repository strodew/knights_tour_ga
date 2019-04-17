'''
Genetic algorithm for solving the Knight's Tour problem
'''

from random import randint
import numpy

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
		print('Current board state: ')
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
		self.visited = [self.start]
		self.fitness = 0
		
		self.board = Board(8,8)
		(row, column) = self.start
		self.board.squares[column - 1][row - 1] = '01'

		#list of knight's moves as tuples
		self.moves = [(1,2), (2,1), (2,-1), (1,-2),
		 (-1,-2), (-2,-1), (-2,1), (-1,2)]

	def isLegalMove(self,move):	
		'''
		Tests a proposed move to check for several conditions:
		An output of 'legal' means that the square has not been visited and exists on the board
		An output of 'visited' means that the square exists on the board, but has been visited before
		And and ouput of False means the square does not exist on the board.
		'''
		decMove = int(move,2)
		moveTup = self.moves[decMove]

		newPosX = self.pos[0] + moveTup[0]
		newPosY = self.pos[1] + moveTup[1]
		newPos = (newPosX,newPosY)

		if newPosX > 0 and newPosX <= self.board.columns and newPosY > 0 and newPosY <= self.board.rows:
			if newPos not in self.visited:
				return 'legal'
			else:
				return 'visited'
		else:
			return False

	def generateTour(self):
		'''
		Generates a candidate knight's tour.
		Move selection is based on random choice of one of 8 possible knight's moves,
		filtered by the isLegalMove method to make sure that they exist on the board.

		Allows for repeated visits to squares as this is merely intended to produce an initial
		population upon which selection, mutation and breeding can occur.
		'''
		while len(self.tour) < 63:
			nextMove = randint(0,7)
			binMove = bin(nextMove)[2:].zfill(3)
			
			if self.isLegalMove(binMove) == 'legal' or self.isLegalMove(binMove) == 'visited':
				self.tour.append(binMove)
				thisMove = self.moves[nextMove]

				newPosX = self.pos[0] + thisMove[0]
				newPosY = self.pos[1] + thisMove[1]
				newPos = (newPosX,newPosY)

				self.pos = newPos
				self.visited.append(newPos)

			else:
				pass

	def tourFitness(self):
		'''
		Fitness function for genetic algorithm
		Calculates an integer value for fitness between 1 and 63 for each tour,
		representing the total number of legal moves in the tour.
		'''
		newFitness = 0
		self.pos = self.start

		'''
		purging list of visited squares for testing fitness
		old visited list is retained as an iterator for updating self.pos
		'''
		positions = self.visited
		position = iter(self.visited)
		self.visited = []

		for move in self.tour:
			if self.isLegalMove(move) == 'legal':
				newFitness += 1
			else:
				self.fitness = newFitness
				return self.fitness
			self.pos = next(position)
		return self.fitness

def generatePop(size):
	'''
	Generates a new population of a given integer size. 
	Returns the population as a list of Tour objects.
	'''
	population = []
	for i in range(size):
		newTour = Tour((1,1))
		newTour.generateTour()
		population.append(newTour)

	return population

def rankTours(population):
	'''
	Ranks a population of tours based on fitness.
	Returns a list of the indexes of tours in the population,
	sorted by the fitness of the tours.
	'''
	fitnessDict = {}
	for i in population:
		fitnessDict[population.index(i)] = i.tourFitness()
	fitness_sorted = sorted(fitnessDict, key=fitnessDict.get, reverse=True)
	return fitness_sorted

def selection(population,eliteSize):
	'''
	First selects the 10 best-performing candidates and guarantees they will be
	selected at least once for populating the mating pool. 

	The remaining mating candidates are selected weighted by fitness from the 
	population. The resulting list, selected, will include a number of tours
	equal to the population size.
	'''
	selected = []
	sort_by_fitness = rankTours(population)
	elites = sort_by_fitness[:eliteSize]
	for i in elites:
		selected.append(population[i])

	#produce cumulative sum of fitnesses for calculating weightings
	fitness_sum = 0
	for i in population:
		fitness_sum += i.fitness

	#calculate a list of fitness-based weightings for the population
	weights = []
	for i in population:
		weight = (i.fitness / fitness_sum)
		weights.append(weight)

	#select the remainder of the pool weighted by fitness
	weighted_pool = numpy.random.choice(population,(len(population) - eliteSize), weights)

	for i in weighted_pool:
		selected.append(i)

	return selected

#testing code
testPop = generatePop(50)
matingPool = selection(testPop,10)
for i in matingPool:
	print(i.fitness)

