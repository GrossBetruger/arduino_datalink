 
import numpy as np
import plotly.express as px
import pandas as pd 

data = pd.read_csv('arduino_log.txt', header=None)
print(data)

px.line(data).show()
