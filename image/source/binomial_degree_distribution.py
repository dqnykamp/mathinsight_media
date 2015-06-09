from scipy import *
from matplotlib.pyplot import *
matplotlib.rcParams.update({'font.size': 20})

Nnodes=10000
prob_connection=10.0/Nnodes;
ks = random.binomial(Nnodes,prob_connection,Nnodes)

figure()
subplot(2,1,1)
hist(ks,bins=arange(min(ks),max(ks)),normed=True)
ylabel("fraction of nodes")

subplot(2,1,2)
hist(ks,bins=arange(min(ks),max(ks)),normed=True,log=True)
xlabel("degree")
ylabel("fraction of nodes")

savefig("binomial_degree_distribution.png", transparent=True, dpi=60)
