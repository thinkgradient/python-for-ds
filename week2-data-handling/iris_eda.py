import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

raw_data = pd.read_csv('https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv') # Read data from URL

print(raw_data.head()) # print first 5 rows of data
