# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:13:13 2021

@author: gustav
"""


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import matplotlib.colors as colors

from matplotlib import cm

a =  np.loadtxt('data/dat_4a.txt', delimiter=None)
b =  np.loadtxt('data/dat_4b.txt', delimiter=None)
c =  np.loadtxt('data/dat_4c.txt', delimiter=None)
d =  np.loadtxt('data/dat_4d.txt', delimiter=None)

fig = plt.figure(figsize=(7,7),dpi = 150)

width, height ="50%","5%"
labelsize = 12
bordersize = 2.0
borderpad = 2.0
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

numb= 11
N = numb
cmap = cm.get_cmap('binary_r',100)
interpolation = 'none'

temp = np.linspace(2,4, num=numb, endpoint=True)
x = list()
y = np.linspace(0,1, num = 21, endpoint = True)
for i in range(numb):
    x.append(0.1/temp[i])

x = np.asarray(x)
y = np.asarray(y)

labelfontsize =14
fontsize = 14

alpha = 1.0

ax1 = fig.add_subplot(221)
ax1.tick_params(axis='both',which='both',direction = 'in', labelsize=labelsize, 
               bottom=True, top=True, labelbottom=False,left=True, right=True)

im1 = ax1.imshow(a, cmap=cmap, interpolation = interpolation , origin = 'lower',  alpha = alpha, 
               norm=colors.LogNorm(vmin=0.01, vmax=1))

axins1 = inset_axes(ax1,width=width,height=height, borderpad=borderpad ,loc=2)
cb1 = fig.colorbar(im1, cax=axins1, orientation = 'horizontal', ticks=[0.01,0.1,1])

ax1.text(0.825, 0.95, r'$\textbf{(a)}$', transform=ax1.transAxes, color = 'black',
      fontsize=labelfontsize, fontweight='bold', va='top')

cb1.set_label('averaged attack rate $(\%)$', fontsize =8, labelpad=-36)
for axis in ['top','bottom','left','right']:
  ax1.spines[axis].set_linewidth(bordersize)

ax1.set_yticks([0, 5,10])
ax1.set_yticklabels([temp[0],temp[5],temp[10]])
ax1.set_xticks([0, 5,10,])
ax1.set_xticklabels([y[0]/0.1,y[5]/.1,y[10]])
ax1.set_ylabel(''r'\boldmath{$\beta / \gamma $', fontsize=fontsize )

ax2 = fig.add_subplot(222)
ax2.tick_params(axis='both',which='both',direction = 'in', labelsize=labelsize,
               bottom=True, top=True, labelleft = False, labelbottom=False,left=True, right=True)

im2 = ax2.imshow(b, cmap=cmap, interpolation = interpolation , origin = 'lower', 
               norm=colors.LogNorm(vmin=0.01, vmax=1))

axins2 = inset_axes(ax2,width=width,height=height, borderpad=borderpad ,loc=2)
cb2 = fig.colorbar(im2, cax=axins2, orientation = 'horizontal', ticks=[0.01,0.1,1])

ax2.text(0.825, 0.95, r'$\textbf{(b)}$', transform=ax2.transAxes, color = 'black',
      fontsize=labelfontsize, fontweight='bold', va='top')

cb2.set_label('averaged attack rate $(\%)$', fontsize =8, labelpad=-36)
for axis in ['top','bottom','left','right']:
  ax2.spines[axis].set_linewidth(bordersize)

ax2.set_yticks([0, 5,10])
ax2.set_yticklabels([temp[0],temp[5],temp[10]])
ax2.set_xticks([0, 5,10,])
ax2.set_xticklabels([y[0]/0.1,y[5]/.1,y[10]])
ax2.text(8, 0.25, 'supercritical \n domain', color = 'white', ha='center', fontsize = 12)
ax2.text(1.25, 3.25, 'subcritical \n domain', color = 'black', ha='center', fontsize = 12, rotation = 90)

ax3 = fig.add_subplot(223)
ax3.tick_params(axis='both',which='both',direction = 'in', labelsize=labelsize,
               bottom=True, top=True, labelbottom=True,left=True, right=True)

im3 = ax3.imshow(c, cmap=cmap, interpolation = interpolation , origin = 'lower', 
               norm=colors.LogNorm(vmin=0.01, vmax=1))

axins3 = inset_axes(ax3,width=width,height=height, borderpad=borderpad ,loc=2)
cb3 = fig.colorbar(im3, cax=axins3, orientation = 'horizontal', ticks=[0.01,0.1,1])

ax3.text(0.825, 0.95, r'$\textbf{(c)}$', transform=ax3.transAxes, color = 'black',
      fontsize=labelfontsize, fontweight='bold', va='top')

cb3.set_label('averaged attack rate $(\%)$', fontsize =8, labelpad=-36)
for axis in ['top','bottom','left','right']:
  ax3.spines[axis].set_linewidth(bordersize)

ax3.set_yticks([0, 5,10])
ax3.set_yticklabels([temp[0],temp[5],temp[10]])
ax3.set_xticks([0, 5,10,])
ax3.set_xticklabels([y[0]/0.1,y[5]/.1,y[10]/.1])
ax3.set_xlabel(''r'\boldmath{$\alpha / \beta$}', fontsize=fontsize )
ax3.set_ylabel(''r'\boldmath{$\beta / \gamma $', fontsize=fontsize )

ax4 = fig.add_subplot(224)
ax4.tick_params(axis='both',which='both',direction = 'in', labelsize=labelsize,
               bottom=True, top=True, labelleft = False, labelbottom=True,left=True, right=True)

im4 = ax4.imshow(d, cmap=cmap, interpolation = interpolation , origin = 'lower', 
               norm=colors.LogNorm(vmin=0.01, vmax=1))

axins4 = inset_axes(ax4,width=width,height=height, borderpad=borderpad ,loc=2)
cb4 = fig.colorbar(im2, cax=axins4, orientation = 'horizontal', ticks=[0.01,0.1,1])

ax4.text(0.825, 0.95, r'$\textbf{(d)}$', transform=ax4.transAxes, color = 'black',
      fontsize=labelfontsize, fontweight='bold', va='top')

cb4.set_label('averaged attack rate $(\%)$', fontsize =8, labelpad=-36)
for axis in ['top','bottom','left','right']:
  ax4.spines[axis].set_linewidth(bordersize)

ax4.set_yticks([0, 5,10])
ax4.set_yticklabels([temp[0],temp[5],temp[10]])
ax4.set_xticks([0, 5,10,])
ax4.set_xticklabels([y[0]/0.1,y[5]/.1,y[10]/.1])
ax4.set_xlabel(''r'\boldmath{$\alpha / \beta$}', fontsize=fontsize )

plt.subplots_adjust(wspace =-0.08, hspace=0.04)
plt.show()

