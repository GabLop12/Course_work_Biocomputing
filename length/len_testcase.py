import unittest
import numpy as np


class TestImageCounter(unittest.TestCase):
    def test_image_counter_empty_file(self):
        # Create an empty numpy array and save it to a file
        data = np.array([])
        np.savez("empty_images.npz", data)
        # Import from the directory
        from github.my_project1.len import image_counter
        result = image_counter("empty_images.npz")
        # Assert that the result is equal to zero
        self.assertEqual(result, 0)

    def setUp(self):
        # Create a numpy array to simulate the data
        self.data = np.random.rand(100, 64, 64)
        np.savez("all_images.npz", self.data)

    def test_image_counter_with_valid_file(self):
        from github.my_project1.len import image_counter
        # Test the function with a valid file
        result = image_counter("all_images.npz")
        self.assertEqual(result, self.data.shape[0])


if __name__ == '__main__':
    unittest.main()
