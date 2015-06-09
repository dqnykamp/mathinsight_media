from scipy import *
from matplotlib.pyplot import *
matplotlib.rcParams.update({'font.size': 20})
A= array([[0,1,0,0,0,0,0,0,0,0],[1,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,1,0,0,0,0,1,0,0,0],[0,1,1,0,0,0,1,1,1,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,0,1,0,0,1,1],[0,0,0,0,0,1,0,1,0,0],[0,0,0,0,0,0,0,1,0,0]])
ks=sum(A,0)
hist(ks,bins=arange(1,7)-0.5,normed=True)
xlim(-0.5,5.5)
xlabel("degree")
ylabel("fraction of nodes")
savefig("small_undirected_network_degree_distribution.png", transparent=True, dpi=60)
