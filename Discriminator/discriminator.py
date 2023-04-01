import numpy as np
from github.Course_work_Biocomputing.len import images

mean_image = sum(images) / len(images)

# discriminator code, use this to decide if an image is just noise
def is_this_a_particle(images):
    return np.corrcoef(images.ravel(), mean_image.ravel())[0, 1] > 0

# discriminator code for all_data

def all_data():
    results = []
    for image in images:
        is_particle = is_this_a_particle(image)
        results.append(is_particle)
    return results
