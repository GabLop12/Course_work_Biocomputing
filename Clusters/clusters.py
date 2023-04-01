import numpy as np
from tensorflow import keras
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

a = 'all_images.npz'


def clustering(a='all_images.npz'):
    # Load the npz file
    data = np.load('all_images.npz')
    X = data['arr_0']
    # Preprocess the images
    X = X.astype('float32') / 255.0
    X = np.expand_dims(X, axis=-1)  # add another dimension

    # Define the encoder model
    inputs = keras.layers.Input(shape=X[0].shape)
    x = keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same')(inputs)
    x = keras.layers.MaxPooling2D((2, 2))(x)
    x = keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
    x = keras.layers.MaxPooling2D((2, 2))(x)
    x = keras.layers.Flatten()(x)
    encoder_output = keras.layers.Dense(64, activation='relu')(x)

    encoder = keras.Model(inputs=inputs, outputs=encoder_output)

    # Get the encoded images
    encoded_imgs = encoder.predict(X)

    # Cluster the images using KMeans
    kmeans = KMeans(n_clusters=8, random_state=42)
    kmeans.fit(encoded_imgs)

    # Visualize the clusters
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111)
    # Adding colors
    colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'brown']
    for i in range(encoded_imgs.shape[0]):
        ax.scatter(encoded_imgs[i, 0], encoded_imgs[i, 1], c=colors[kmeans.labels_[i]])
    return plt.show()

clustering()