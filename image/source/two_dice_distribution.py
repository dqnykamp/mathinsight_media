from scipy import *
from matplotlib.pyplot import *
matplotlib.rcParams.update({'font.size': 20})
x=linspace(2,12,11)
p=array([1,2,3,4,5,6,5,4,3,2,1])/36.
bar(x-0.4,p)
xlim(1.4,12.6)
xlabel("x")
ylabel("P(x)")
savefig("two_dice_distribution.png", transparent=True, dpi=60)
