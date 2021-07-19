import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt
plt.style.use('seaborn')
plt.rcParams["axes.grid"] = False

import pandas as pd
import numpy as np

print("running...", np.random.rand())

def doviz(vals,labs,fname,data_credit,dynomight_yloc,cols=None):
    plt.figure(1,figsize=[8,8])
    # best cmaps
    cmap = plt.get_cmap("coolwarm").reversed(); clim = [-1,1]
    #cmap = plt.get_cmap("RdBu"); clim = [-1,1]
    #cmap = plt.get_cmap("Spectral"); clim = [-1,1]
    #cmap = plt.get_cmap("bwr").reversed(); clim = [-1,1]
    #cmap = plt.get_cmap("seismic").reversed(); clim = [-1,1]
    # good cmaps
    #cmap = plt.get_cmap("BrBG"); clim = [-1,1]
    #cmap = plt.get_cmap("PuOr"); clim = [-1,1]
    #cmap = plt.get_cmap("RdGy"); clim = [-1,1]
    #cmap = plt.get_cmap("RdYlBu"); clim = [-1,1]
    #cmap = plt.get_cmap("RdYlGn"); clim = [-1,1]
    # ok cmaps
    #cmap = plt.get_cmap("gist_earth").reversed(); clim = [-1,1]
    #cmap = plt.get_cmap("gist_stern"); clim = [-.2,1]
    #cmap = plt.get_cmap("cubehelix").reversed(); clim = [-1,1]
    #cmap = plt.get_cmap("ocean"); clim=[-1,1]
    #cmap = plt.get_cmap("twilight_shifted").reversed(); clim=[-1,1]
    # bad cmaps
    # cmap = plt.get_cmap("terrain"); clim = [0,1]    
    #cmap = plt.get_cmap("tab10"); clim = [-.2,1]
    plt.imshow(vals, cmap=cmap, origin='upper', interpolation='nearest',aspect='equal')
    plt.clim(clim)
    plt.yticks(np.arange(0, len(labs)), labs)
    plt.xticks(np.arange(0, len(labs)), labs)
    xlab_position=(0,1.05)
    plt.gca().set_xticklabels(labs,rotation=90,ha="center",va="bottom",position=xlab_position)
    #plt.clim([-.7,.7])
    #plt.clim([-.2,1])
    cb = plt.colorbar(shrink=.7)
    cb.ax.set_title("correlation",fontsize=10)

    plt.figtext(0.0,.088+0.07,data_credit,color='gray',alpha=0.7,fontsize=5,fontname='monospace')
    plt.figtext(.78,dynomight_yloc,'dynomight.net',color='gray',alpha=0.5,fontsize=6,fontname='monospace')
    #plt.savefig(fname+'.png')
    #plt.savefig(fname+'.pdf')
    if cols:
        for t,c in zip(plt.gca().xaxis.get_ticklabels(),cols):
            t.set_color(c)
        for t,c in zip(plt.gca().yaxis.get_ticklabels(),cols):
            t.set_color(c)
    plt.savefig(fname+'.png',bbox_inches='tight')
    plt.savefig(fname+'.pdf',bbox_inches='tight')
    plt.savefig(fname+'.svg',bbox_inches='tight')
    plt.clf()

def fill_lower(vals):
    vals = np.array(vals)
    for i in range(vals.shape[0]):
        for j in range(i+1):
            if i==j:
                vals[i,j]=1
            else:
                vals[i,j]=vals[j,i]
    return np.array(vals,dtype=float)
def fill_upper(vals):
    return fill_lower(np.array(vals).T)

def swap(m,i,j):
    tmp = m[i]
    m[i] = m[j]
    m[j] = tmp
    return m

def swap2d(M,i,j):
    tmp    = M[:,i]+0.0
    M[:,i] = M[:,j]
    M[:,j] = tmp
    tmp    = M[i, :]+0.0
    M[i,:] = M[j,:]
    M[j,:] = tmp
    return M

mats = {}
matlabs = []

# ibrahim
A = pd.read_csv("ibrahim2011.csv").values
labs = A[:,0]
vals = fill_lower(A[:,1:])
dynomight_yloc=.19
data_credit = 'Data from "Exploring the General Motor Ability Construct", Ibrahim et al., 2011'
doviz(vals,labs,'ibrahim2011',data_credit,dynomight_yloc)
mats["ibrahim"] = vals

# marsh 1994
labs = ["Strong", "Balance", "Shuttle", "Flexible", "Endure"]
vals = fill_upper([[0,0,0,0,0],
                 [.096, 0, 0, 0, 0],
                 [.152, .024, 0, 0, 0],
                 [.376, .049, .294, 0, 0],
                 [.221, .102, .437, .394, 0]])

dynomight_yloc=.19
data_credit = 'Data from "A Multidimensional Physical Self-concept and Its Relations to Multiple Components of Physical Fitness", Marsh et al., 1994'
doviz(vals,labs,'marsh1994',data_credit,dynomight_yloc)
mats["marsh"] = vals

A = pd.read_csv("baumgartner1972.csv").values
labs = A[:,0]
vals = fill_lower(np.array(A[:,1:])/100)
for i in [9,11,12]: # flip stuff that measures distances
    vals[:,i] = -vals[:,i]
    vals[i,:] = -vals[i,:]
# flip location of dash
dynomight_yloc=.19
vals = swap2d(vals,9,12)
labs = swap(labs,9,12)
vals = swap2d(vals,11,12)
labs = swap(labs,11,12)
data_credit = 'Data from "Factor Analysis of Physical Fitness Tests", Baumgartner and Zuidema, 1972'
#cols = cols = ['black']*4 + ['C2']*4 + ['C3']*2 + ['C5']*3
cols = cols = ['black']*4 + ['C1']*4 + ['C2']*2 + ['C5']*3
#cols = None
doviz(vals,labs,'baumgartner1972',data_credit,dynomight_yloc,cols=cols)
mats["baumgartner"] = vals

A = pd.read_csv("alderton1997.csv").values
labs = A[:,0]
vals = np.array(A[:,1:],dtype=float)
for i in range(vals.shape[0]):
    for j in range(vals.shape[1]):
        if vals[i,j] != vals[j,i]:
            print(i, j, vals[i,j], vals[j,i])
for i in [16,17,18]: # flip stuff that measures errors
    vals[:,i] = -vals[:,i]
    vals[i,:] = -vals[i,:]
dynomight_yloc=.19
data_credit = 'Data from "The ECAT Battery", Alderton et al., 1997'
doviz(vals,labs,'alderton1997',data_credit,dynomight_yloc)
mats["alderton"] = vals

stuff = [["Letter sets"],["Figure classification",.38],["Calendar test",.62,.43],["Vocabulary",.44,.26,.54],["Analogies",.52,.33,.60,.71],["Sentence completion",.57,.35,.64,.63,.58],["Math aptitude",.35,.24,.40,.31,.33,.33],["Math operations",.35,.34,.49,.33,.40,.40,.35],["Submult",.30,.15,.33,.16,.21,.24,.32,.35],["Cube comparison",.21,.27,.25,.15,.16,.18,.27,.24,.15],["Hidden patterns",.49,.42,.52,.40,.45,.42,.30,.37,.22,.22],["Surface development",.51,.45,.57,.39,.49,.39,.35,.43,.22,.41,.56],["Word endings",.31,.19,.30,.34,.35,.33,.15,.23,.22,.18,.24,.27],["Word beginnings",.41,.24,.39,.44,.46,.40,.21,.31,.26,.16,.33,.34,.52],["Opposites",.36,.28,.43,.40,.40,.45,.25,.29,.24,.24,.28,.32,.35,.46],["Faces",.25,.19,.24,.23,.21,.27,.11,.13,.10,.15,.18,.18,.09,.13,.15],["Pictures",.37,.25,.34,.33,.31,.43,.17,.15,.12,.11,.30,.27,.25,.18,.22,.36],["Changes",.52,.38,.63,.58,.57,.62,.25,.34,.21,.10,.44,.42,.25,.34,.36,.37,.43],["Blends",.48,.34,.56,.58,.55,.58,.24,.30,.16,.13,.39,.37,.26,.34,.36,.31,.45,.74],["Management",.45,.31,.52,.41,.40,.52,.16,.21,.16,.05,.34,.29,.16,.26,.27,.36,.39,.66,.62],["Relationships",.38,.27,.47,.39,.40,.47,.18,.22,.15,.06,.33,.28,.15,.25,.24,.32,.34,.61,.59,.70]]
labs = [a[0] for a in stuff]
vals = np.zeros([len(labs), len(labs)])
for i, ai in enumerate(stuff):
    for j, aij in enumerate(ai[1:]):
        vals[i,j] = aij
vals = fill_upper(vals)
# keep only cognitive tests
vals = vals[:15,:15]
labs = labs[:15]
cols = cols = ['black']*3 + ['C1']*3 + ['C2']*3 + ['C3']*3 + ['C4']*3 + ['C5']*6
dynomight_yloc=.19
data_credit = 'Data from "Emotional Intelligence Is a Second-Stratum Factor of Intelligence", MacCann et al., 2014'
doviz(vals,labs,'maccann2014',data_credit,dynomight_yloc,cols=cols)
mats["maccann"] = vals

stuff = [["Vocabulary"],["Similarities",.67],["Information",.72,.59],["Comprehension",.70,.58,.59],["Picture arrangement",.51,.53,.50,.42],["Block design",.45,.46,.45,.39,.43],["Arithmetic",.48,.43,.55,.45,.41,.44],["Picture completion",.49,.52,.52,.46,.48,.45,.30],["Digit span",.46,.40,.36,.36,.31,.32,.47,.23],["Object assembly",.32,.40,.32,.29,.36,.58,.33,.41,.14],["Digit symbol",.32,.33,.26,.30,.28,.36,.28,.26,.27,.25]]
labs = [a[0] for a in stuff]
vals = np.zeros([len(labs), len(labs)])
for i, ai in enumerate(stuff):
    for j, aij in enumerate(ai[1:]):
        vals[i,j] = aij
vals = fill_upper(vals)
dynomight_yloc=.19
data_credit = 'Data from "Cognitive and Neurobiological Mechanisms of the Law of General Intelligence", Chabris, 2007'
doviz(vals,labs,'chabris2007a',data_credit,dynomight_yloc)
mats["chabris (a)"] = vals


stuff = [["Raven’s Matrices"],["Working Memory",.39,.46],["Verbal Fluency",.36,.48,.42],["Response Time",.41,.28,.41,.39],["Mental Rotation",.41,.29,.15,.21,.34],["Coordinate Spatial Encoding",.32,.30,.07,-.02,.04,.25],["Categorical Spatial Encoding",.21,.12,-.02,.13,.16,.21,.20]]
labs = [a[0] for a in stuff]
vals = np.zeros([len(labs), len(labs)])
for i, ai in enumerate(stuff):
    for j, aij in enumerate(ai[1:]):
        vals[i,j] = aij
vals = fill_upper(vals)
dynomight_yloc=.19
data_credit = 'Data from "Cognitive and Neurobiological Mechanisms of the Law of General Intelligence", Chabris, 2007'
doviz(vals,labs,'chabris2007b',data_credit,dynomight_yloc)
mats["chabris (b)"] = vals

# I think this data is from a model, not observed
# stuff =  [["Verbal Comprehension"],["Perceptual Reasoning",.73],["Processing Speed",.48,.67],["Auditory Working Memory",.69,.76,.68],["Visual Working Memory",.71,.88,.72,.88],["Auditory Memory",.71,.60,.52,.68,.82],["Visual Memory",.54,.81,.54,.64,.96,.81]]
# labs = [a[0] for a in stuff]
# vals = np.zeros([len(labs), len(labs)])
# for i, ai in enumerate(stuff):
#     for j, aij in enumerate(ai[1:]):
#         vals[i,j] = aij
# vals = fill_upper(vals)
# dynomight_yloc=.19
# data_credit = 'Confirmatory Factor Analysis of the WAIS-IV/WMS-IV", Holdnack et al., 2011'
# doviz(vals,labs,'holdnack2011',data_credit,dynomight_yloc)
# mats["holdnack"] = vals

A = pd.read_csv("vanderlinden2010.csv").values
labs = A[:,0]
vals = np.array(A[:,1:],dtype=float)
for i in range(vals.shape[0]):
    for j in range(vals.shape[1]):
        if vals[i,j] != vals[j,i]:
            print(i, j, vals[i,j], vals[j,i])
dynomight_yloc=.19
data_credit = 'Data from "The General Factor of Personality: A meta-analysis of Big Five intercorrelations and a criterion-related validity study", van der Linden et al., 2010'
doviz(vals,labs,'vanderlinden2010',data_credit,dynomight_yloc)
mats["vanderlinden"] = vals

import palettable
import itertools
#colors = itertools.cycle(palettable.cartocolors.qualitative.Prism_9.mpl_colors)
colors = itertools.cycle(palettable.cartocolors.qualitative.Safe_9.mpl_colors)

plt.rcParams["axes.grid"] = True
plt.figure(figsize=(3*1.1,6*1.1))
axis1=plt.subplot(3,1,1)
alls = ['alderton','chabris (a)','maccann','chabris (b)','ibrahim','baumgartner','marsh','vanderlinden'] # 'holdnack'
ints = ['alderton','chabris (a)','chabris (b)',"holdnack",'maccann']
pers = ["vanderlinden"]
for matlab in alls:
    mat = mats[matlab]
    e = np.abs(np.flip(np.linalg.eigvalsh(mat)))
    if matlab in ints:
        line = '-'
        plt.plot(100*np.arange(1,len(e)+1)/len(e), 100*np.cumsum(e)/np.sum(e), line, linewidth=0.6, markersize=2, label=matlab, alpha = 0.8, color=next(colors))
plt.ylabel("% variance explained")
plt.yticks([0,25,50,75,100])
plt.legend(frameon=False,loc="lower right", title="cognitive")
#
axis2=plt.subplot(3,1,2,sharex=axis1)
for matlab in alls:
    mat = mats[matlab]
    e = np.abs(np.flip(np.linalg.eigvalsh(mat)))
    if (not matlab in ints) and (not matlab in pers):
        line = '-'
        plt.plot(100*np.arange(1,len(e)+1)/len(e), 100*np.cumsum(e)/np.sum(e), line, linewidth=0.6, markersize=2, label=matlab, alpha = 0.8, color=next(colors))
plt.ylabel("% variance explained")
plt.xlabel("% principal components")
plt.legend(frameon=False,loc="lower right", title="physical")
plt.xticks([0,25,50,75,100])
plt.yticks([0,25,50,75,100])
plt.setp(axis1.get_xticklabels(), visible=False)
plt.savefig("var2.pdf",bbox_inches='tight')
plt.savefig("var2.png",bbox_inches='tight')
plt.clf()

plt.rcParams["axes.grid"] = True
plt.figure(figsize=(4,6))
axis1=plt.subplot(3,1,1)
#alls = ['holdnack','alderton','chabris (a)','chabris (b)','maccann','ibrahim','baumgartner','marsh','vanderlinden']
#ints = ['alderton','chabris (a)','chabris (b)',"holdnack",'maccann']
pers = ["vanderlinden"]
for matlab in alls:
    mat = mats[matlab]
    e = np.abs(np.flip(np.linalg.eigvalsh(mat)))
    if matlab in ints:
        line = '-'
        plt.plot(100*np.arange(1,len(e)+1)/len(e), 100*np.cumsum(e)/np.sum(e), line, linewidth=0.6, markersize=2, label=matlab, alpha = 0.8, color=next(colors))
        #plt.plot(100*np.arange(1,len(e)+1)/len(e), 100*(e/np.sum(e)), line, linewidth=0.6, markersize=2, label=matlab, alpha = 0.8, color=next(colors))
plt.ylabel("% variance explained")
plt.yticks([0,50,100])
plt.legend(frameon=False,loc="lower right", title="cognitive")
#
axis2=plt.subplot(3,1,2,sharex=axis1)
for matlab in alls:
    mat = mats[matlab]
    e = np.abs(np.flip(np.linalg.eigvalsh(mat)))
    if (not matlab in ints) and (not matlab in pers):
        line = '-'
        plt.plot(100*np.arange(1,len(e)+1)/len(e), 100*np.cumsum(e)/np.sum(e), line, linewidth=0.6, markersize=2, label=matlab, alpha = 0.8, color=next(colors))
        #plt.plot(100*np.arange(1,len(e)+1)/len(e), 100*(e/np.sum(e)), line, linewidth=0.6, markersize=2, label=matlab, alpha = 0.8, color=next(colors))
plt.ylabel("% variance explained")
plt.legend(frameon=False,loc="lower right", title="physical")
plt.yticks([0,25,50,75,100])
#
axis3=plt.subplot(3,1,3,sharex=axis1)
for matlab in alls:
    mat = mats[matlab]
    e = np.abs(np.flip(np.linalg.eigvalsh(mat)))
    if matlab in pers:
        line = '-'
        plt.plot(100*np.arange(1,len(e)+1)/len(e), 100*np.cumsum(e)/np.sum(e), line, linewidth=0.6, markersize=2, label=matlab, alpha = 0.8, color=next(colors))
        #plt.plot(100*np.arange(1,len(e)+1)/len(e), 100*(e/np.sum(e)), line, linewidth=0.6, markersize=2, label=matlab, alpha = 0.8, color=next(colors))
plt.ylabel("% variance explained")
plt.xlabel("% principal components")
plt.legend(frameon=False,loc="lower right", title="personality")
plt.xticks([0,25,50,75,100])
plt.yticks([0,25,50,75,100])
plt.setp(axis1.get_xticklabels(), visible=False)
plt.setp(axis2.get_xticklabels(), visible=False)
plt.savefig("var3.pdf",bbox_inches='tight')
plt.savefig("var3.png",bbox_inches='tight')
plt.clf()