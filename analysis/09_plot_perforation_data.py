import pandas as pd
import numpy as np

## from https://stackoverflow.com/questions/49926147/how-to-modify-edge-color-of-violinplot-using-seaborn
import seaborn.categorical
seaborn.categorical._Old_Violin = seaborn.categorical._ViolinPlotter

class _My_ViolinPlotter(seaborn.categorical._Old_Violin):

    def __init__(self, *args, **kwargs):
        super(_My_ViolinPlotter, self).__init__(*args, **kwargs)
        self.gray='k'

seaborn.categorical._ViolinPlotter = _My_ViolinPlotter
import seaborn as sns
##

import os
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as font_manager
import scienceplots
from matplotlib_scalebar.scalebar import ScaleBar

plt.style.use('nature')

font_size = 6
matplotlib.rcParams["xtick.minor.bottom"]=False
matplotlib.rcParams["xtick.top"]=False
matplotlib.rcParams["ytick.minor.left"]=False
matplotlib.rcParams["ytick.right"]=False
matplotlib.rcParams["font.size"] = font_size
matplotlib.rcParams["axes.spines.right"] = True
matplotlib.rcParams["axes.spines.top"] = True
matplotlib.rcParams["xtick.minor.visible"] = False
matplotlib.rcParams["ytick.minor.visible"] = False
matplotlib.rcParams["xtick.direction"] = "out"
matplotlib.rcParams["ytick.direction"] = "out"
matplotlib.rcParams["legend.fontsize"] = font_size
matplotlib.rcParams["svg.fonttype"] = "none"
matplotlib.rcParams["xtick.labelsize"] = font_size
matplotlib.rcParams["ytick.labelsize"] = font_size
matplotlib.rcParams["axes.titlesize"] = font_size
matplotlib.rcParams["axes.labelsize"] = font_size
matplotlib.rcParams["grid.alpha"] = 0
matplotlib.rcParams["savefig.transparent"] = True
matplotlib.rcParams["savefig.dpi"] = 300
matplotlib.rcParams["savefig.format"] = "svg"

path = "/usr/share/fonts/truetype/msttcorefonts/Arial.ttf"
font_manager.fontManager.addfont(path)
prop = font_manager.FontProperties(fname=path)
matplotlib.rcParams["font.family"] = prop.get_name()

def set_size(w,h, ax=None):
    """ w, h: width, height in inches """
    if not ax: ax=plt.gca()
    l = ax.figure.subplotpars.left
    r = ax.figure.subplotpars.right
    t = ax.figure.subplotpars.top
    b = ax.figure.subplotpars.bottom
    figw = float(w)/(r-l)
    figh = float(h)/(t-b)
    ax.figure.set_size_inches(figw, figh)
    
### Make a folder to save plots
plot_version = 1
try:
    os.mkdir("plots_{}".format(str(plot_version).zfill(2)))
except:
    pass

### import data
sl = pd.read_csv("dataframes/perforation_analysis.csv")
fl = pd.read_csv("dataframes/cell_envelope_breakdown_analysis.csv")

k = 35
d = pd.read_csv("lysis_data_time_adjusted/lysis_{}.csv".format(str(k).zfill(2)))

### Graph widths in mm
time_series_width = 125
vio_width = 16



### Plot perforation time series - for figure 5
inch = 25.4
w = time_series_width/inch
h = 29.7/inch
sl_start = sl["start_time"][sl["cell"] == k].tolist()[0]
fl_start = fl["rise_time"][fl["cell"] == k].tolist()[0]
fl_peak = fl["peak_time"][fl["cell"] == k].tolist()[0]
fl_end = fl["fall_time"][fl["cell"] == k].tolist()[0]

t = d["time"].tolist()
con = d["c"].tolist() # contrast of cell
hor = np.mean(con[2000:t.index(sl_start)]) # horizontal, i.e. baseline contrast

fig, ax = plt.subplots(dpi=300)

#ax.plot(d["time"]-sl_start, d["l"], color="#420a68", label="Left of cell")
ax.plot(d["time"]-sl_start, d["c"], color="#3090AB", label="Cell")
ax.plot(d["time"]-sl_start, d["r"], color="#807f7e", label="Right of cell")
ax.plot(d["time"]-sl_start, d["st"], color="k", label="Control region")
ax.vlines(sl_start-sl_start, 305, 995, linestyle=":", color="k", label="Perforation")
ax.vlines(fl_start-sl_start, 305, 995, linestyle="dashdot", color="k", label="Lysis start")
ax.hlines(hor, -1.95, 7.95, linestyle="--", color="k")
ax.set_xlabel("Offset time, $t - t_4$ (s)")
ax.set_ylabel("Mean intensity (AU pixel$^{-1}$)")
ax.legend(frameon=False, loc=2)
ax.set_xlim([-1.95,7.95])
ax.set_ylim([305,995])

fig.tight_layout()
set_size(w,h)
plt.savefig("plots_{}/perforation_time_series_v{}.svg".format(str(plot_version).zfill(2), str(plot_version).zfill(2)))
plt.show()
plt.close()



### Plot perforation violin - for figure 5
slow_times = sl["perforation_duration"].tolist()
fast_times = [x for x in np.subtract(np.array(fl["fall_time"]), np.array(fl["rise_time"]))]
perforation_str = ["Perforation" for x in slow_times]
lysis_str = ["Lysis" for x in fast_times]
times = slow_times + fast_times
groups = perforation_str + lysis_str 

df_groups = pd.DataFrame()
df_groups["step"] = groups
df_groups["times"] = times

df_perf = df_groups[df_groups["step"] == "Perforation"]
df_lysis = df_groups[df_groups["step"] == "Lysis"]


matplotlib.rcParams["xtick.bottom"]=False
inch = 25.4
w = vio_width/inch
h = 29.7/inch

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(w/0.7,h), dpi=300) # the figsize argument spaces out swarmplot dots

sns.violinplot(data=df_perf, y="times", x="step", ax=ax, color="#3090AB", inner="quartile")
sns.swarmplot(data=df_perf, y="times", x="step", ax=ax, s=2, color="white")
ax.set_ylabel("t5 - t4 (s)")
ax.set(xlabel=None)
ax.set(xticklabels=[])
ax.set_ylim([0,26])
fig.tight_layout()
set_size(w,h)
plt.savefig("plots_{}/perforation_vio_v{}.svg".format(str(plot_version).zfill(2), str(plot_version).zfill(2)))
plt.show()
plt.close()
matplotlib.rcParams["xtick.bottom"]=True



### Graph width in mm
time_series_width = 90

### Plot perforation time series - for supplementary material
inch = 25.4
w = time_series_width/inch
h = 2*29.7/inch
sl_start = sl["start_time"][sl["cell"] == k].tolist()[0]

xlims = [-10,10]
ylims = [220,1080]
fig, ax = plt.subplots(dpi=300)

k = 35
d = pd.read_csv("lysis_data_time_adjusted/lysis_{}.csv".format(str(k).zfill(2)))
sl_start = sl["start_time"][sl["cell"] == k].tolist()[0]
ax.plot(d["time"]-sl_start, d["c"], color="#3090AB", label="Cell from fig. 5", zorder=200)

clean = [1,2,3,4,6,7,9,10,12,13,15,16,17,18,19,23,24,25,26,27,28,29,30,31,34,35,36,38,39,40,41,42,43,44,45,47] # the inclusion list for events, clean for both perforation and lysis
for k in clean:
    if k == 1:
        d = pd.read_csv("lysis_data_time_adjusted/lysis_{}.csv".format(str(k).zfill(2)))
        sl_start = sl["start_time"][sl["cell"] == k].tolist()[0]
        ax.plot(d["time"]-sl_start, d["c"], color="#807f7e", linewidth=0.1, label="Other cells", zorder=0)
    if k not in [1, 35]:
        d = pd.read_csv("lysis_data_time_adjusted/lysis_{}.csv".format(str(k).zfill(2)))
        sl_start = sl["start_time"][sl["cell"] == k].tolist()[0]
        ax.plot(d["time"]-sl_start, d["c"], color="#807f7e", linewidth=0.1, zorder=0)
        
ax.vlines(sl_start-sl_start, ylims[0], ylims[1], linestyle=":", color="k", label="Perforation", zorder=210)
ax.set_xlabel("Offset time, $t - t_4$ (s)")
ax.set_ylabel("Mean intensity (AU pixel$^{-1}$)")
ax.legend(frameon=False, loc=2)
ax.set_xlim(xlims)
ax.set_ylim(ylims)

fig.tight_layout()
set_size(w,h)
plt.savefig("plots_{}/additional_perforation_time_series_v{}.svg".format(str(plot_version).zfill(2), str(plot_version).zfill(2)))
plt.show()
plt.close()