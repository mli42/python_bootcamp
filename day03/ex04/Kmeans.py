# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Kmeans.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/08 17:04:24 by mli               #+#    #+#              #
#    Updated: 2022/03/14 00:21:33 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re # Regex
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def fit(self, X: np.ndarray) -> None:
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            None.
        Raises:
            This function should not raise any Exception.
        """
        self.kmeans = KMeans(init='random',
                             n_clusters=self.ncentroid,
                             n_init=self.max_iter)
        self.kmeans.fit(X)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            The prediction as a numpy.ndarray, a vector of dimension m * 1.
        Raises:
            This function should not raise any Exception.
        """
        self.cluster_labels = self.kmeans.predict(X)
        self.centroids = self.kmeans.cluster_centers_
        return self.centroids

    def fig_3D(self, X: np.ndarray) -> None:
        fig = plt.figure()
        ax = Axes3D(fig)

        cluster_labels = self.cluster_labels
        cluster_centers = self.centroids

        ax.set_xlabel("Height")
        ax.set_ylabel("Weight")
        ax.set_zlabel("Bone Density")

        colorstr = ["red", "blue", "green", "purple"]
        for i in range(self.ncentroid):
            ax.scatter(X[cluster_labels == i, 0], X[cluster_labels == i, 1],
                    X[cluster_labels == i, 2], color=colorstr[i])
            ax.scatter(cluster_centers[i, 0], cluster_centers[i, 1],
                    cluster_centers[i, 2], color=colorstr[i], marker="o", s=150, label="centroids")
        plt.show()

ARGS_NAME = ['filepath', 'ncentroid', 'max_iter']

def parsing() -> list or None:
    if (len(sys.argv) != 4):
        return None
    args_regex = [
        rf"^{ARGS_NAME[0]}=(.+\.csv)$",
        rf"^{ARGS_NAME[1]}=(\d+)$",
        rf"^{ARGS_NAME[2]}=(\d+)$",
    ]
    res = []

    for i, regex in enumerate(args_regex):
        search_obj = re.search(args_regex[i], sys.argv[i + 1])
        if (search_obj is None):
            return None
        res.append(search_obj.group(1))
    return res

def print_usage():
    print(f"""USAGE:
    python {sys.argv[0]} %s=PATH %s=NB %s=NB
EXAMPLE:
    python {sys.argv[0]} %s=../resources/solar_system_census.csv %s=4 %s=30
    """ %(*ARGS_NAME, *ARGS_NAME))

def main():
    ARGV = parsing()
    if ARGV is None:
        print_usage()
        return
    data = np.genfromtxt(ARGV[0], delimiter=",", skip_header=1)
    X = data[:, 1:] # Delete index
    ncentroid = 4

    kms = KmeansClustering(ncentroid=ncentroid)
    kms.fit(X)
    kms.predict(X)
    kms.fig_3D(X)

if __name__ == "__main__":
    main()
