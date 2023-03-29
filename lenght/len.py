import numpy as np
c ="all_images.npz"
def image_counter (c):
    #load the data from the file
    a = np.load("all_images.npz")
    #Select the first array
    m = a['arr_0']
    #Create a list and loop over from the 3D array
    images = [m[i, :, :] for i in range(m.shape[0])]
    #Return lenght of images
    return len(images)



