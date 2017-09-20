from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import lstm, time

#Step 1 load data
X_train, y_train, X_test, y_test = lstm.load_data('sp500.csv', 50, True)