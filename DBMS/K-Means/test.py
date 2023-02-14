from sklearn.datasets import make_blobs
from numpy import genfromtxt
import numpy as np
from KMeans import KMeans
from sklearn.model_selection import train_test_split

if __name__ == "__main__":
    np.random.seed(42)

    # data = np.genfromtxt('DBMS\Datasets\BreastCancer\Breast_cancer_data.csv', delimiter=',')
    # X, y = np.array(list(zip(data[:, 3], data[:, 2]))) , data[:, -1]
    X, y = make_blobs(
        centers=3, n_samples=500, n_features=2, shuffle=True, random_state=40
    )

    clusters = len(np.unique(y))
    print(clusters)

    k = KMeans(K=clusters, max_iters=150, plot_steps=True)
    y_pred = k.predict(X)

    k.plot()