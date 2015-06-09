# Usage: python plot_degree_distribution_undir.py [filename] [min] [max]

import sys
import os
from scipy import *
from matplotlib.pyplot import *
matplotlib.rcParams.update({'font.size': 20, 'axes.titlesize': 'medium'})

if(len(sys.argv)>1):
    filename=sys.argv[1]
else:
    filename='A.txt'
if(len(sys.argv)>2):
    try:
        min_degree_displayed = int(sys.argv[2])
    except:
        min_degree_displayed = -1
else:
    min_degree_displayed = -1
if(len(sys.argv)>3):
    try:
        max_degree_displayed = int(sys.argv[3])
    except:
        max_degree_displayed = -1
else:
    max_degree_displayed = -1


filename_base=os.path.splitext(filename)[0]
output_filename=filename_base + '_degree_distribution.png'


print "loading " + filename
try:
    A=loadtxt(filename)
except:
    print "Couldn't load " + filename
    sys.exit(2)

ks=sum(A,0)
maxdeg=max(ks)
mindeg=min(ks)

if maxdeg-mindeg< 50:
    # for small numbers of bins, shift so bins are centered around number
    [counts,bins,patches]=hist(ks,bins=arange(1,maxdeg+2)-0.5)
    shifted=True
else:
    [counts,bins,patches]=hist(ks,bins=min(100,maxdeg-mindeg+1))
    shifted=False

figure()
bar(bins[:-1],counts/float(sum(counts)),width=bins[1]-bins[0])

adjust_range=False
if min_degree_displayed >=0:
    adjust_range=True
    if max_degree_displayed <0:
        max_degree_displayed=maxdeg

    if shifted:
        min_degree_displayed -= 0.5
        max_degree_displayed -= 0.5

        
if adjust_range:
    xlim(min_degree_displayed,max_degree_displayed+1)
xlabel("degree")
ylabel("fraction of nodes")
savefig(output_filename,dpi=60,bbox_inches='tight')
print "Saved figure as " + output_filename
