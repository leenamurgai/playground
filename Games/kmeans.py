import numpy as np
import pandas as pd

def find_cluster_centres(data_df, k, max_iter = 100):
    """
    k-means algo:
    1. choose the first k data points to be the cluster centres
    2. assign all data points to the closest cluster
    3. calculate the new cluster centres as the mean of the data points in each cluster
    4. repeat steps 2 and 3
    """
    n_data = data_df.shape[0]
    n_feat = data_df.shape[1]

    centres = data_df.iloc[:k]
    labels = nearest_cluster(centres)
    for i in range(max_iter):
        centres = self.cluster_mean()
        data_df['labels'] = self.nearest_cluster(centres)
        label_change = np.abs(data_df['labels'] - labels).sum()
        if label_change == 0:
            break
    return data_df

def calc_distances(data_df, centres_df):
    k = centres_df.shape[0]
    n_data = data_df.shape[0]

    def distance(centre):
        return np.sqrt(np.sum((data_df-centre)**2, axis=1))
    #distances = np.zeros((n_data, k))
    #for i in range(k):
    #    distances[:,i] = np.sqrt(np.sum((data_df-centres_df.iloc[i])**2, axis=1))
    distances_df = centres_df.apply(distance, axis=1)
    return distances_df.T

def nearest_cluster(data_df, centres_df):
    distances_df = calc_distances(data_df, centres_df)
    #print('test', distances.shape)
    #data_df['labels'] = np.argmin(distances, axis=1)
    data_df['labels'] = distances_df.idxmin(axis=1)

def cluster_mean(data_df):
    return data_df.groupby('labels').mean()

"""Set-up some data"""
np.random.seed(1)
x = 2
data1 = np.random.normal(size=(100, 2)) + [ x, x]
data2 = np.random.normal(size=(100, 2)) + [-x,-x]
data  = np.concatenate((data1, data2))
np.random.shuffle(data)
data_df = pd.DataFrame(data=data, columns=['feat1', 'feat2'])
"""pick centres"""
centres_df = data_df.iloc[:2]
"""check some stuff"""
#print(centres_df)
#print(calc_distances(data_df, centres_df)[:2, :])
nearest_cluster(data_df, centres_df)
#print(data_df.iloc[:2])
print(cluster_mean(data_df))
