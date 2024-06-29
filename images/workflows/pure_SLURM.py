#!/bin/env python3 

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

languages = ['bash', 'Perl', 'Python']
counts = [4400, 274, 55]
bar_labels = ['red', 'blue', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:orange']

bars = ax.bar(languages, counts, label=bar_labels, color=bar_colors)
plt.grid(False)
#plt.axis('off')
ax.bar_label(bars, fmt='%d')
ax.set_xticks(np.arange(len(languages)), labels=languages)
ax.yaxis.set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
#plt.show()
plt.savefig('SLURM_workflow_solution.png', bbox_inches='tight')
