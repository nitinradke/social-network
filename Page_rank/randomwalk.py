import numpy as np
import matplotlib.pyplot as plt
import random
import networkx as nx
def walk(n,p):
    start=random.randint(0,n-1)
    G=nx.erdos_renyi_graph(n,p)
    count=0
    s=set([start])
    v=start
    while len(s)<G.order():
        nb=nx.neighbors(G,v)
        v=random.choice(nb)
        s.add(v)
        count+=1
    return count    
l=[]
for i in range(20,1000):
    s=[]
    for j in range(10):
        c=walk(i,0.7)
        s.append(c)
        print(str(i)+"---->"+str(np.average(s)))    
    l.append(np.average(s))
plt.plot(l)    
plt.show()
