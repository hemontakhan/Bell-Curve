import plotly.figure_factory as ff
import pandas as pd
import csv

fetcher = pd.read_csv('data.csv')
graph = ff.create_distplot([fetcher["Weight(Pounds)"].tolist()],["Weight"],show_hist=False)
graph.show()