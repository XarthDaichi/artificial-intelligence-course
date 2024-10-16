import numpy as np
import matplotlib.pyplot as plt
#
plt.rc('font', size=14)
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('legend', fontsize=14)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)

def save_fig(fig_name, tight_layout=True, fig_extension="png", resolution=300):
    filename = f"img/{fig_name}.{fig_extension}"
    if tight_layout:
        plt.tight_layout()
    plt.savefig(filename, format=fig_extension, dpi=resolution)
    