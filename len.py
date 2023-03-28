import numpy as np
#load the data from the file
a = np.load("all_images.npz")
#Select the first array
m = a['arr_0']
#Create a list and loop over from the 3D array
images = [m[i, :, :] for i in range(m.shape[0])]
#Print lenght of images
print(len(images))