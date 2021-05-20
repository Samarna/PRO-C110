import pandas as pd 
import plotly.figure_factory as ff 
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("medium_data.csv")
data = df["temp"].tolist()

mean = statistics.mean(data)
print("Mean of population is ",mean)
std = statistics.stdev(data)
print("Standard Deviation of population is ",std)

def sample_mean(number):
    dataset = []
    for i in range(0,number):
        random_index = random.randint(0,len(data)-1)
        dataset.append(data[random_index])
    mean = statistics.mean(dataset)
    return mean

def setup():
    means_list = []
    for i in range(0,1000):
        means = sample_mean(400)
        means_list.append(means)
    fig = ff.create_distplot([means_list],["Temperatures"],show_hist = False)
    mean = statistics.mean(means_list)
    print("Mean of samples is ",mean)
    std = statistics.stdev(means_list)
    print("Standard Deviation of samples is ",std)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    fig.show()

setup()