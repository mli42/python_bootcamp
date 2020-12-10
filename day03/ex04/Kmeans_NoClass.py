# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Kmeans_NoClass.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/10 21:53:46 by mli               #+#    #+#              #
#    Updated: 2020/12/10 21:53:48 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

# Generate data
X = np.genfromtxt("../resources/solar_system_census.csv", delimiter=",", skip_header=1)
X = X[:, 1:] # Delete index

# Fit K-means with Scikit
nclusters = 4
kmeans = KMeans(init='k-means++', n_clusters=nclusters, n_init=10)
kmeans.fit(X)

# Predict the cluster for all the samples
P = kmeans.predict(X)

def kmeans_3D() -> None:
    fig = plt.figure()
    ax = Axes3D(fig)

    cluster_labels = P
    cluster_centers = kmeans.cluster_centers_

    ax.set_xlabel("Height")
    ax.set_ylabel("Weight")
    ax.set_zlabel("Bone Density")

    colorstr = ["red", "blue", "green", "purple"]
    for i in range(nclusters):
        ax.scatter(X[cluster_labels == i, 0], X[cluster_labels == i, 1],
                   X[cluster_labels == i, 2], color=colorstr[i])
        ax.scatter(cluster_centers[i, 0], cluster_centers[i, 1],
                   cluster_centers[i, 2], color=colorstr[i], marker="o", s=150, label="centroids")

    # Centroids colored in black
    #ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1],
    #           cluster_centers[:, 2], color="black", marker='o', s=120, label="centroids")
    #ax.legend()

    plt.show()

kmeans_3D()
