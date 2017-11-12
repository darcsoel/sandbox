import random
import scipy as sp
import numpy as np
# import mysql.connector

data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")
print(data[:10])
