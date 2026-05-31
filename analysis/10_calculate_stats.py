import pandas as pd
import numpy as np
from statsmodels.stats.descriptivestats import describe

df = pd.read_csv("dataframes/cell_envelope_breakdown_analysis.csv", encoding='utf-8-sig')
df["start_to_end"] = np.subtract(np.asarray(df["fall_time"]), np.asarray(df["rise_time"]))
df["start_to_peak"] = np.subtract(np.asarray(df["peak_time"]), np.asarray(df["rise_time"]))
df["peak_to_end"] = np.subtract(np.asarray(df["fall_time"]), np.asarray(df["peak_time"]))
describe(df[["start_to_end", "start_to_peak", "peak_to_end"]]).to_csv("dataframes/cell_envelope_breakdown_stats.csv", encoding='utf-8-sig')

df = pd.read_csv("dataframes/perforation_analysis.csv", encoding='utf-8-sig')
describe(df["perforation_duration"]).to_csv("dataframes/perforation_stats.csv", encoding='utf-8-sig')