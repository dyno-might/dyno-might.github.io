import pandas as pd
import plotnine as p9
from matplotlib import pyplot as plt
import numpy as np
import re

df = pd.read_csv('data.csv')
#print(f'{data=}')

df['fight'] = df['Do you think you could beat me in a fight?']
df['I/E'] = pd.Categorical(df['What was your score along the I/E axis?'], categories=['I','i','x','e','E'])
df['S/N'] = pd.Categorical(df['What was your score along the S/N axis?'], categories=['S','s','x','n','N'])
df['F/T'] = pd.Categorical(df['What was your score along the F/T axis?'], categories=['F','f','x','t','T'])
df['J/P'] = pd.Categorical(df['What was your score along the J/P axis?'], categories=['J','j','x','p','P'])


good = (~df['fight'].isnull()) * (~df['I/E'].isnull())
df = df[good]

print(f'{df.columns}')

plot = (p9.ggplot(df,
                 p9.aes('Do you think you could beat me in a fight?',
                        y=p9.after_stat("count"),
                        fill='I/E'
                 )
    )
    + p9.geom_histogram(binwidth=0.95)
    #+ p9.geom_bar(position='fill')
    + p9.scale_y_continuous(expand=(0,0),limits=(0,400))
    + p9.themes.theme_tufte()
    + p9.theme(text=p9.element_text(family="Montserrat"))
    #+ p9.theme(axis_line_x=p9.element_line())
    + p9.theme(axis_ticks=p9.element_blank())
    + p9.theme(axis_text_x = p9.element_text(va='top'))
    + p9.theme(plot_background=p9.element_rect(fill='white',color='white'))
    + p9.annotate('text',x=5.3,y=30,label='dynomight.net',family="monospace",color='lightgray',size=4,alpha=1.0)
    + p9.ggtitle('Do you think you could beat me in a fight?')
    + p9.labs(x="")
    + p9.scale_x_discrete(limits=['Almost surely','Probably','Unsure','Probably not','Very unlikely'])
    #+ p9.scale_fill_discrete(limits=['E','e','x','i','I'])
)

plot.save('fight.pdf')
plot.save('fight.svg')
plot.save('fight.png')

plot = (p9.ggplot(df,
                 p9.aes('Do you think you could beat me in a fight?',
                        y=p9.after_stat("count"),
                        fill='I/E'
                 )
    )
    #+ p9.geom_histogram()
    + p9.geom_bar(position='fill')
    #+ p9.scale_y_continuous(expand=(0,0),limits=(0,450))
    + p9.scale_y_continuous(expand=(0,0),limits=(0,1))
    + p9.themes.theme_tufte()
    + p9.theme(text=p9.element_text(family="Montserrat"))
    #+ p9.theme(axis_line_x=p9.element_line())
    + p9.theme(axis_ticks=p9.element_blank())
    + p9.theme(axis_text_x = p9.element_text(va='top'))
    + p9.theme(plot_background=p9.element_rect(fill='white',color='white'))
    + p9.annotate('text',x=5.3,y=30,label='dynomight.net',family="monospace",color='lightgray',size=4,alpha=1.0)
    + p9.ggtitle('Do you think you could beat me in a fight?')
    + p9.labs(x="")
    + p9.scale_x_discrete(limits=['Almost surely','Probably','Unsure','Probably not','Very unlikely'])
    #+ p9.scale_fill_discrete(limits=['E','e','x','i','I'])
)

plot.save('fight_condprob.pdf')
plot.save('fight_condprob.svg')
plot.save('fight_condprob.png')



plot = (p9.ggplot(df,
                 p9.aes('I/E',
                        y=p9.after_stat("count"),
                        fill='fight'
                 )
    )
    #+ p9.geom_histogram()
    + p9.geom_bar(position='fill')
    #+ p9.scale_y_continuous(expand=(0,0),limits=(0,450))
    + p9.scale_y_continuous(expand=(0,0),limits=(0,1))
    + p9.themes.theme_tufte()
    + p9.theme(text=p9.element_text(family="Montserrat",size=10))
    + p9.theme(plot_background=p9.element_rect(fill='white',color='white'))
    #+ p9.theme(axis_line_x=p9.element_line())
    + p9.theme(axis_ticks=p9.element_blank())
    + p9.annotate('text',x=5.3,y=30,label='dynomight.net',family="monospace",color='lightgray',size=4,alpha=1.0)
    + p9.ggtitle('Do you think you could beat me in a fight?')
    + p9.labs(x="")
    + p9.labs(fill="")
    + p9.labs(y="")
    + p9.scale_fill_discrete(limits=['Almost surely','Probably','Unsure','Probably not','Very unlikely'])
    #+ p9.scale_fill_discrete(limits=['E','e','x','i','I'])
)

plot.save('fight_mbti.pdf')
plot.save('fight_mbti.svg')
plot.save('fight_mbti.png')


import matplotlib.pyplot as plt
from matplotlib import rcParams

# Set font properties globally
rcParams['font.family'] = 'Montserrat'
rcParams['font.size'] = 12

#['Very unlikely','Probably not','Unsure','Probably','Almost surely']

axes = ['I/E','S/N','F/T','J/P']
categories = [['I','i','x','e','E'],['S','s','x','n','N'],['F','f','x','t','T'],['J','j','x','p','P']]

import statsmodels.stats.api as sms

l = None
for axis,cats in zip(axes,categories):
       score = []
       lo = []
       hi = []
       std = []
       for x in cats:
              df3 = df[df[axis]==x]

              data = np.array(1*(df3['fight']=='Very unlikely') + 2*(df3['fight']=='Probably not') + 3*(df3['fight']=='Unsure') + 4*(df3['fight']=='Probably') + 5*(df3['fight']=='Almost surely')) 

              score.append(np.mean(data))
              my_lo, my_hi = sms.DescrStatsW(data).tconfint_mean()
              lo.append(my_lo)
              hi.append(my_hi)
              std.append(my_hi-score[-1])


       plt.plot(score,label=axis)
       #plt.errorbar(range(len(score)),score,yerr=std)
       plt.fill_between(range(len(score)),y1=lo,y2=hi,alpha=0.2)
       plt.xticks(range(5),cats)
       plt.ylim([2,3.5])
       plt.yticks([2,2.5,3,3.5])
       plt.gca().spines['top'].set_visible(False)
       plt.gca().spines['bottom'].set_visible(False)
       plt.gca().spines['left'].set_visible(False)
       plt.gca().spines['right'].set_visible(False)
       plt.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False)
       plt.ylabel("Could you beat me in a fight?")

       #plt.legend()
       plt.savefig('fight_' + re.sub(r'[^a-zA-Z]', '', axis) + '.pdf',facecolor='white')
       plt.savefig('fight_' + re.sub(r'[^a-zA-Z]', '', axis) + '.svg',facecolor='white')
       plt.savefig('fight_' + re.sub(r'[^a-zA-Z]', '', axis) + '.png',facecolor='white')
       #l.remove()
       plt.clf()