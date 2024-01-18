import os
import sys

import pandas

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fedall.utils import FedAll as fa

# Specify the server address in terms of IP and Port number
SERVER_ADDRESS = "localhost:6005"

# Load the data for training purposes
# The data contains both the input features and the output feature
# The features are represented as columns
# The data points are represented as rows
Data = pandas.read_csv("train_data_1.csv", header=None)
Data = Data.to_numpy()

NUM_ROUNDS = 50
# The following will start the training and will return the final model
final_model = fa.client_start(SERVER_ADDRESS, Data, NUM_ROUNDS)
