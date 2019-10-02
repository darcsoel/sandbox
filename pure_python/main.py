import random
import scipy as sp
import numpy as np
# import mysql.connector
from tkinter import *

data = sp.genfromtxt("web_traffic.tsv", delimiter="\t")
print(data[:10])

root = Tk()
root.title('test')
root.geometry('100x100')

root.mainloop()
