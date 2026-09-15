"""
Helper functions for data loading and analysis.
"""
import pandas as pd #Import Pandas for data manipulation
import matplotlib.pyplot as plt #Import Matplotlib for plotting graphs
import seaborn as sns #Import Seaborn for statistical visualisations

# Load the dataset from a CSV file
def load_data(filepath="data/youtube.csv"):
    return pd.read_csv(filepath, low_memory=False)

#Generate a report of missing values
def missing_report(df):
    m = df.isnull().sum() #Count missing values in each column
    #Create a table with missing counts and percentages
    out = pd.DataFrame({"missing": m, "pct": (100*m/len(df)).round(2)})
    #Return only columns with missing values, sorted highest to lowest
    return out[out["missing"] > 0].sort_values("missing", ascending=False)

#Return the most frequent values in a column
def top_counts(series, n=10, sep=None):
    s = series.dropna() #Remove missing values
    #Split multi-value cells if a separator is provided
    if sep:
        s = s.str.split(sep).explode().str.strip()
    return s.value_counts().head(n) #Return the top N most common values

#How fast each trending video accumulates views between snapshots
def add_view_velocity(df, time_col="timestamp", video_col="ytvideoid", views_col="views"):
    out = df.copy() #Work on a copy so the original DataFrame is not changed
    out[time_col] = pd.to_datetime(out[time_col], errors="coerce") #Convert timestamp to datetime; invalid values become NaT
    out = out.sort_values([video_col, time_col]) #Sort by video then time so consecutive rows are in order

    grouped = out.groupby(video_col, sort=False) #Group by video to calculate changes within each video
    out["hours_since_prev"] = grouped[time_col].diff().dt.total_seconds() / 3600 #Hours since the previous snapshot for that video
    out["views_delta"] = grouped[views_col].diff() #Change in views since the previous snapshot for that video
    out["views_per_hour"] = out["views_delta"] / out["hours_since_prev"] #View velocity: views gained per hour

    return out #Return DataFrame with three new velocity columns