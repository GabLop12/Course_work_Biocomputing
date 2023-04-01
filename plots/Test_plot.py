import unittest

import matplotlib
# import the function to be tested from the project
from github.my_project1.plots.plots import plot

# define an empty function
def isintance(fig, Figure):
    pass

# define a unit test class that inherits from `unittest.TestCase`
class TestPlot(unittest.TestCase):
    # define a test method that checks if the function runs without error
    def test_plot_runs(self):
        assert plot() is None
