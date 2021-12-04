import csv
from os import name
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

file = pd.read_csv('Data.csv')
data = file['claps'].tolist()

def RandomMean(counter):
    dataSet=[]
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data))
        value= data[randomIndex]
        dataSet.append(value)

    populatioMean = statistics.mean(dataSet)
    return populatioMean
    
def showFigure(list):
    df=list
    figure= ff.create_distplot([df],['Claps'],show_hist=False)
    figure.show()

list=[]
def setUp():
  
  for i in range(0,100):
    meanOfRandom=RandomMean(30)
    list.append(meanOfRandom) 
    showFigure(list)
mean1 = statistics.mean(list)
stdev = statistics.stdev(list)
print(' the mean  of sample disribution'+str(mean1))
print(' standard Deviation of sample disribution'+str(stdev))

std1Start,std1End=mean1-stdev,mean1+stdev
std2Start,std2End=mean1-(2*stdev),mean1+(2*stdev)
std3Start,std3End=mean1-(3*stdev),mean1+(3*stdev)


figure= ff.create_distplot([data],["Writing Scores"], show_hist=False)
figure.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.17],mode="lines",name="Mean Of Writing Scores of All Students"))
figure.add_trace(go.Scatter(x=[std1Start,std1Start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 START"))
figure.add_trace(go.Scatter(x=[std1End,std1End],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 END"))
figure.add_trace(go.Scatter(x=[std2Start,std2Start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 START"))
figure.add_trace(go.Scatter(x=[std2End,std2End],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 END"))
figure.add_trace(go.Scatter(x=[std3Start,std3Start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 START"))
figure.add_trace(go.Scatter(x=[std3End,std3End],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 END"))
figure.show()

setUp()
