# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 12:45:57 2021

@author: gustav
"""
import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('data/dat_5a.txt')

x,y, yerr = data[0], data[1], data[2]

fig = plt.figure(dpi = 300)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

ax = fig.add_subplot(111)

ax.errorbar(x, y, yerr=yerr,ecolor = 'black', elinewidth = 2, capsize  = 2.5, 
            fmt='o', alpha = 1, color = 'black',)

ax.tick_params( labelsize=16, left=True, labelleft =True,  labelright =False, 
               labelbottom = True , axis='both',which='both',direction = 'in',) 
ax.set_ylabel(  r'\boldmath{$ (\sigma / \mu)$}' ,fontsize = 16)
ax.set_xlabel( ''r'\boldmath{$(\alpha / \beta)$',fontsize = 16)

for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2.0)

ax.set_xticks(np.arange(0,1.05, 0.25))
ax.set_xticklabels([0,1,2,3,4])

ax.text(0.04, 0.95, r'$\textbf{(a)}$', transform=ax.transAxes, color = 'black',
      fontsize=16, fontweight='bold', va='top')

plt.tight_layout(pad = 4)

plt.show()


