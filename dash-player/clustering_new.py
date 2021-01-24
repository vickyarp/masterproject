import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster import hierarchy
import scipy.cluster.hierarchy as sch
import plotly.figure_factory as ff
def get_dendogram_angle():
    df = pd.read_csv('table.csv',index_col=0)
    A = df.to_numpy()
    new = 1-A
    y = new[np.triu_indices(73,1)]
    labels = list(df.index)

    fig = ff.create_dendrogram(new, orientation='left', linkagefun=lambda x: sch.linkage(x, "average"),labels=labels, color_threshold=0.3, colorscale= ['skyblue', 'tan', 'teal', 'red', 'tomato', 'yellow','turquoise', 'violet', 'wheat', 'white', 'whitesmoke','ellow', 'yellowgreen'],hovertext=labels)
    fig.update_layout(width=1000, height=800,title="Dance Poses Clustering ")
    return fig


def get_dendogram_velocity():
    df = pd.read_csv('table_velocity_first_attempt.csv',index_col=0)
    df = df.dropna(axis='columns')
    A = df.to_numpy()
    new = 1-A
    y = new[np.triu_indices(68,1)]
    labels = list(df.index)

    fig = ff.create_dendrogram(new, orientation='left', linkagefun=lambda x: sch.linkage(x, "average"),labels=labels, color_threshold=1.2, colorscale= ['skyblue', 'tan', 'teal', 'red', 'tomato', 'yellow','turquoise', 'violet', 'wheat', 'white', 'whitesmoke','ellow', 'yellowgreen'],hovertext=labels)
    fig.update_layout(width=1000, height=800,title="Dance Poses Clustering")
    return fig
