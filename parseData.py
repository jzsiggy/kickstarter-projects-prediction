import os
import cv2
import sklearn
from sklearn.model_selection import train_test_split
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


full_data = pd.read_csv("kickstarter-projects/ks-projects-201801.csv")
interest_categories = [ 'main_category' , 'goal' , 'pledged' , 'backers' , 'country' , 'usd pledged' , 'state' ]

data = full_data[interest_categories]

plt.scatter(data['goal'] , data['pledged'])
plt.show()