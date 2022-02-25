# -*- coding: utf-8 -*-n

import numpy as np
import matplotlib.pyplot as plt
import mpltex

data1 = np.loadtxt('data/dat_5a.txt')
data2 = np.loadtxt('data/dat_5b.txt')

x,y, yerr = data1[0], data1[1], data1[2]

fig = plt.figure(figsize=(6,6),dpi = 150)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

ax1 = fig.add_subplot(211)

ax1.errorbar(x, y, yerr=yerr,ecolor = 'black', elinewidth = 2, capsize  = 2.5, 
            fmt='o', alpha = 1, color = 'black',)

ax1.tick_params( labelsize=16, left=True, labelleft =True,  labelright =False, 
               labelbottom = True , axis='both',which='both',direction = 'in',) 
ax1.set_ylabel(  r'\boldmath{$ (\sigma / \mu)$}' ,fontsize = 16)
ax1.set_xlabel( ''r'\boldmath{$(\alpha / \beta)$',fontsize = 16)

for axis in ['top','bottom','left','right']:
    ax1.spines[axis].set_linewidth(2.0)

ax1.set_xticks(np.arange(0,1.05, 0.25))
ax1.set_xticklabels([0,1,2,3,4])

ax1.text(0.04, 0.95, r'$\textbf{(a)}$', transform=ax1.transAxes, color = 'black',
      fontsize=16, fontweight='bold', va='top')


ax1.errorbar(x, y, yerr=yerr,ecolor = 'black', elinewidth = 2, capsize  = 2.5, 
            fmt='o', alpha = 1, color = 'black',)

ax2 = fig.add_subplot(212)

linestyles = mpltex.linestyle_generator(colors = ['black'])

for i in range(1,17):
    ax2.step(data2[:,0],data2[:,i], **next(linestyles), alpha = 1, markevery=3)

ax2.set_xlabel("time (weeks)",fontsize=16)
ax2.set_ylabel( r'\boldmath{$R(t)$}',fontsize= 16)
ax2.set_yscale('log')
ax2.legend(loc='upper left', ncol=6,fontsize = 6, fancybox=True, framealpha=0.0)

ax2.grid(True, 'major', 'y', ls='--', lw=.5, c='grey', alpha=.5)
ax2.tick_params(axis='both', which='both', labelsize=16, direction = 'in',
               bottom=True, top=True, labelbottom=True,
               left=True, right=True, labelleft=True)

for axis in ['top','bottom','left','right']:
    ax2.spines[axis].set_linewidth(2)

ax2.text(0.04, 0.95, r'$\textbf{(b)}$', transform=ax2.transAxes, color = 'black',
      fontsize=16, fontweight='bold', va='top')

plt.tight_layout(pad = 4)

plt.subplots_adjust(hspace=0.40)

plt.show()

