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