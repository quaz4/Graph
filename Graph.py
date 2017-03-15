#!/usr/bin/python
#Written by William Stewart 
#Last modified 15/03/2017

#TODO Check params in all functions, no tests at the moment

class Graph():
	"""Data structure representing an undirected graph and its traversal"""

	def __init__(self, fileName):
		"""Given a file name, reads in graph information and initialises data"""
		
		self.graph = {}
		self.start = None
		self.stack = None

		file = open(fileName, "r")

		lines = file.readlines()

		file.close()

		#Loop through all lines in file and make graph
		for i in lines:
			print i

			nodeInfo = i.split()

			#Check if first node exists, make if doesn't exist
			if not self.graph.has_key(nodeInfo[0]):
				print "No key"
				self.graph[nodeInfo[0]] = self.Node(nodeInfo[0])

			#Check if second node exists, make if doesn't exist
			if not self.graph.has_key(nodeInfo[1]):
				print "No key"
				self.graph[nodeInfo[1]] = self.Node(nodeInfo[1])

			#Add edges
			edge = self.graph[nodeInfo[0]].addConnection(nodeInfo[1], nodeInfo[2])
			self.graph[nodeInfo[1]].addConnection(nodeInfo[0], nodeInfo[2])

	def init(self, inStart):
		self.start = inStart
		self.stack = [Graph.start]

	def move(self, nodeName):
		self.stack.append(self.graph[nodeName])

	def back(self):
		self.stack.pop()

	def neighbors(self, nodeName):
		return self.graph[nodeName].getConnections()

	class Node():
		"""Data structure representing a node in an undirected graph"""

		def __init__(self, inName):
			self.name = inName
			self.connections = {}

		def addConnection(self, node, cost):
			self.connections[node] = cost

		def removeConnection(self, nodeName):
			del self.connections[nodeName]

		def getConnections(self):
			return self.connections.keys()

		def getCost(self, nodeName):
			return self.connections[nodeName]