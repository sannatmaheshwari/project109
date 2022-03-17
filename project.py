import random as r
import pandas as pa
import plotly.express as px
import plotly.figure_factory as p
import statistics as s
import plotly.graph_objects as go

df = pa.read_csv("StudentsPerformance.csv")
diceresult = df["reading score"].tolist()
mean = s.mean(diceresult)   
median = s.median(diceresult)
mode = s.mode(diceresult)
sd = s.stdev(diceresult)
print(mean,median,mode,sd)

sd1start,sd1end = mean-sd,mean+sd
sd2start,sd2end = mean-(sd*2),mean+(sd*2)
sd3start,sd3end = mean-(sd*3),mean+(sd*3)

figure = p.create_distplot([diceresult],["figure"],show_hist=False)
figure.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
figure.add_trace(go.Scatter(x=[sd1start,sd1start],y=[0,0.17],mode="lines",name="sd1"))
figure.add_trace(go.Scatter(x=[sd1end,sd1end],y=[0,0.17],mode="lines",name="sd1"))
figure.add_trace(go.Scatter(x=[sd2start,sd2start],y=[0,0.17],mode="lines",name="sd2"))
figure.add_trace(go.Scatter(x=[sd2end,sd2end],y=[0,0.17],mode="lines",name="sd2"))
figure.add_trace(go.Scatter(x=[sd3start,sd3start],y=[0,0.17],mode="lines",name="sd3"))
figure.add_trace(go.Scatter(x=[sd3end,sd3end],y=[0,0.17],mode="lines",name="sd3"))
figure.show()

data1 = [result for result in  diceresult if result>sd1start and result<sd1end]
data2 = [result for result in  diceresult if result>sd2start and result<sd2end]
data3 = [result for result in  diceresult if result>sd3start and result<sd3end]

p1 = len(data1)*100.0/len(diceresult)
p2 = len(data2)*100.0/len(diceresult)
p3 = len(data3)*100.0/len(diceresult)
print(p1,p2,p3)