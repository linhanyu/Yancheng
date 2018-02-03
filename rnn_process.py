import numpy as np

def window_transform_series(series, window_size):
    # containers for input/output pairs
    X = [series[i:i+window_size] for i in range(0,len(series)-window_size)]
    y = [series[i] for i in range(window_size,len(series))]

    # reshape each
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)

    return X,y
