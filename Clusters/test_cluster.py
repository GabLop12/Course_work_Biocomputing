import unittest

from github.my_project1.Clusters.clusters import clustering


class TestClustering(unittest.TestCase):

    def test_clusters(self):
        # Test that the function runs without errors
        try:
            clustering()
        except Exception as e:
            self.fail(f"clustering() raised an unexpected exception: {e}")
