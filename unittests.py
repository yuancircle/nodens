#!nodens-python
import unittest
import constraint
import networkx as nx
import cPickle

class TestSequenceFunctions(unittest.TestCase):
		
	def setUp(self):
		self.undirected = nx.read_edgelist("unit test data/adp.edgelist",create_using=nx.Graph())		

	def test_undirected_constraints_whole(self):
		f = open("unit test data/adp_constraints_whole.pickle","r")
		expected = cPickle.load(f)
		f.close()
		
		constraints = constraint.calcConstraints(self.undirected,True,False,True)
		
		for node in constraints:
			for entry in constraints[node]:
				self.assertAlmostEqual(constraints[node][entry],expected[node][entry])
				
	def test_undirected_constraints_ego(self):
		f = open("unit test data/adp_constraints_ego.pickle","r")
		expected = cPickle.load(f)
		f.close()

		constraints = constraint.calcConstraints(self.undirected,True,False,False)

		for node in constraints:
			for entry in constraints[node]:
				self.assertAlmostEqual(constraints[node][entry],expected[node][entry])

if __name__ == '__main__':
	unittest.main()
