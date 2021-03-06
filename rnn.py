import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


def build_part1_RNN(window_size):
    model = Sequential()
    model.add(LSTM(window_size, input_shape=(window_size, 1)))
    model.add(LSTM(window_size)
    model.add(Dense(1))

    return model
