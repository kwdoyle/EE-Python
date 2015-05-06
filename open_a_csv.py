import pandas as pd
import numpy as np


# using an example csv of blood gluecose levels from biometry
data = pd.read_csv("/Users/kevin/School/Spring '15/Biometry/Week 4/Problem Set/diabetes.csv")


# note: matrices are not stored as "data frames" in rodeo
# or potentially just numpy matrices aren't.
matrix = np.matrix([[1,2,3],[3,4,5],[5,6,7]])


# import a csv file stored on my server so this script will work anywhere
clouds = pd.read_csv("http://mylifeisdoyle.com/ups/clouds.csv")
# this also just proved that pd.read_csv() can use URLS just like R's read.csv()