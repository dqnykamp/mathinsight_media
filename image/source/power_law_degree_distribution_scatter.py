from scipy import *
from matplotlib.pyplot import *
matplotlib.rcParams.update({'font.size': 20})

Nnodes=10000
power=-2;
maxdegree=1000;
mindegree=1;
ks = ((maxdegree**(power+1)-mindegree**(power+1) )*random.random(Nnodes)+mindegree**(power+1))**(1/(power + 1))

[counts,bins,patches]=hist(ks,bins=100)

figure()
subplot(2,1,1)
bar(bins[:-1],counts/float(sum(counts)),width=bins[1]-bins[0])
ylabel("fraction of nodes")

subplot(2,1,2)
bar(bins[:-1],counts/float(sum(counts)),width=bins[1]-bins[0],log=True)
#hist(ks,bins=arange(min(ks),max(ks)),normed=True,log=True)
xlabel("degree")
ylabel("fraction of nodes")

savefig("power_law_degree_distribution.png", transparent=True, dpi=60)

maxdegfound=int(ceil(max(bins)))
[counts,bins,patches]=hist(ks,bins=maxdegfound)


countsnozero=counts*1.
countsnozero[counts==0]=-Inf

figure()
scatter(bins[:-1],countsnozero/float(sum(counts)),s=60)
yscale('log')
xscale('log')
ylim(0.00008,1.1)
xlim(0.8,1100)
xlabel('degree')
ylabel("fraction of nodes")
subplots_adjust(bottom=0.15)

savefig("power_law_degree_distribution_scatter.png", transparent=True, dpi=60)
