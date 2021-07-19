from matplotlib import pyplot as plt
plt.style.use('seaborn')
plt.rcParams["axes.grid"] = False

import pandas as pd
import numpy as np

#A = np.genfromtxt("table.csv",delimiter=',')
#from IPython import embed; embed()

A = pd.read_csv("ibrahim2011.csv").values

labs = A[:,0]
vals = np.array(A[:,1:])
for i in range(vals.shape[0]):
    for j in range(i+1):
        if i==j:
            vals[i,j]=1
        else:
            vals[i,j]=vals[j,i]
vals = np.array(vals,dtype=float)


def doviz(vals,labs,fname):
    plt.figure(1,figsize=[8,8])
    cmap = plt.get_cmap("coolwarm")
    #plt.matshow(vals, cmap=cmap.reversed(),fignum=1)
    plt.imshow(vals, cmap=cmap.reversed(), origin='upper', interpolation='nearest',aspect='equal')
    plt.yticks(np.arange(0, len(labs)), labs)
    plt.xticks(np.arange(0, len(labs)), labs)
    #plt.gca().set_xticklabels(labs,rotation=35,ha="left",position=(-0.5,1))
    xlab_position=(0,1.05)
    plt.gca().set_xticklabels(labs,rotation=90,ha="center",va="bottom",position=xlab_position)
    plt.clim([-1, 1])
    #cb = plt.colorbar()
    #cb.ax.set_title("correlation",fontsize=10)
    cb = plt.colorbar(shrink=.7)
    cb.ax.set_title("correlation",fontsize=10)
    #plt.tight_layout()
    plt.savefig(fname+'.png',bbox_inches='tight')
    plt.savefig(fname+'.pdf',bbox_inches='tight')

doviz(vals,labs,'vals')