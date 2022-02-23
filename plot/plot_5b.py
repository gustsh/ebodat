# -*- coding: utf-8 -*-n
"""
Created on Sat Jul  3 22:54:40 2021

@author: gustav
"""

import numpy as np
import matplotlib.pyplot as plt
import mpltex

data = np.loadtxt('data/dat_5b.txt')

fig = plt.figure(dpi = 300)
width ="60%"
height="5%"
labelsize = 12
bordersize = 1.5
borderpad = 1

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
ax = fig.add_subplot(111)
linestyles = mpltex.linestyle_generator(colors = ['black'])
size = 16
ax.set_yscale('log')

for i in range(1,17):
    ax.step(data[:,0],data[:,i], **next(linestyles), alpha = 1, markevery=3)

ax.set_xlabel("time (weeks)",fontsize=size)
ax.set_ylabel( r'\boldmath{$R(t)$}',fontsize= size)

ax.legend(loc='upper left', ncol=6,fontsize = 6, fancybox=True, framealpha=0.0)
fig.tight_layout(pad=2.0)

ax.grid(True, 'major', 'y', ls='--', lw=.5, c='grey', alpha=.5)
ax.tick_params(axis='both', which='both', labelsize=size, direction = 'in',
               bottom=True, top=True, labelbottom=True,
               left=True, right=True, labelleft=True)

for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)
plt.ylim(0,1000)
plt.tight_layout(pad = 3)
plt.yscale('log')
plt.show()
