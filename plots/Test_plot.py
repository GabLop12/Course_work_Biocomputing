import unittest

import matplotlib

from github.my_project1.plots.plots import plot


def isintance(fig, Figure):
    pass


class TestPlot(unittest.TestCase):
    def test_plot_runs(self):
        assert plot() is None
