import numpy as np
import pandas as pd

"""Set-up some data and centres"""
np.random.seed(1)
x = 2
data1 = np.random.normal(size=(5, 2)) + [ x, x]
data2 = np.random.normal(size=(5, 2)) + [-x,-x]
data  = np.concatenate((data1, data2))
np.random.shuffle(data)
data_df = pd.DataFrame(data=data, columns=['feat1', 'feat2'])
centres_df = data_df.iloc[:2]

def calc_distances_test(data_df, centres_df):
    distances = calc_distances(data_df, centres_df)
    assert distances[0][0] == 0
    assert distances[1][1] == 0

def nearest_cluster_test(data_df, centres_df):
    nearest_cluster(data_df, centres_df)
    assert data_df['labels'].iloc[0] == 0
    assert data_df['labels'].iloc[1] == 1

def cluster_mean_test(data_df):
    centres_df = cluster_mean(data_df)
    assert centres_df.shape == (2, 2)
