import matplotlib.pyplot as plt
import numpy as np


def plot():
    # load the data from the file
    a = np.load("all_images.npz")
    # Select the first array
    m = a['arr_0']
    # Create a list and loop over from the 3D array
    images = [m[i, :, :] for i in range(m.shape[0])]
    N = 4
    # Create a figure with N subplots arranged in a row.
    fig, axes = plt.subplots(1, N, sharex=True, sharey=True)
    # Generate a random permutation of the indices of the images list.
    Ns = np.random.permutation(np.arange(len(images)))
    # Loop over the axes
    for ax, i in zip(axes, Ns):
        ax.imshow(images[i])
        ax.set_title(f"Image {i}")
    # Subplots are properly spaced
    fig.tight_layout()
    return plt.show()




