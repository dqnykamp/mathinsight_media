from scipy import *
from matplotlib.pyplot import *
matplotlib.rcParams.update({'font.size': 20})

A=array([[0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0],[1,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,1,1,0,0],[0,0,1,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0 ]])


kins=sum(A,1)
kouts=sum(A,0)
ktots=kins+kouts

nnodes=len(kins)

maxin=max(kins)
maxout=max(kouts)
maxtot=max(ktots)

pdeg=zeros([maxin+1,maxout+1])

for i in range(nnodes):
    din=kins[i]
    dout=kouts[i]
    pdeg[dout][din]+=1

pdeg=pdeg/nnodes

figure()
pcolor(arange(maxin+2)-0.5,arange(maxout+2)-0.5,pdeg)
xticks(range(maxin+1))
yticks(range(maxout+1))
xlabel('in-degree')
ylabel('out-degree')
cb=colorbar()
cb.set_label('fraction of nodes')

savefig("small_directed_network_degree_distribution.png", transparent=True, dpi=60,bbox_inches='tight')

figure()
subplot(3,1,1)
hist(kins,bins=arange(0,maxin+2)-0.5,normed=True)
xlim(-0.5,maxin+0.5)
ylim(0,0.4)
xticks(range(maxin+1))
yticks(arange(0,0.5,0.1))
xlabel("in-degree")


subplot(3,1,2)
hist(kouts,bins=arange(0,maxout+2)-0.5,normed=True)
xlim(-0.5,maxout+0.5)
ylim(0,0.4)
xticks(range(maxout+1))
xlabel("out-degree")
yticks(arange(0,0.5,0.1))
ylabel("fraction of nodes")

subplot(3,1,3)
hist(ktots,bins=arange(0,maxtot+2)-0.5,normed=True)
xlim(-0.5,maxtot+0.5)
xticks(range(maxtot+1))
yticks(arange(0,0.4,0.1))
xlabel("total degree")


subplots_adjust(hspace=0.7,right=0.7)



savefig("small_directed_network_marginal_degree_distributions.png", transparent=True, dpi=70,bbox_inches='tight')
