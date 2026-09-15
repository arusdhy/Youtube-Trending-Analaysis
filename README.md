# YouTube Engagement Trend Analysis

## What this project is / what it gives you

A beginner-level EDA and visualization project exploring engagement on trending YouTube videos: 200,000 daily stat snapshots of ~11,000 trending videos, covering views, likes, dislikes, and comments over time.

This project gives you a clear picture of how engagement behaves on trending content. It is not a predictive model — it is an exploratory analysis focused on insight, visualizations, and reproducible notebooks.

I also added a **view-velocity** section, which looks at how quickly videos accumulate views between snapshots, not just their total counts. This makes the project more time-aware and less like a standard summary-statistics EDA.

## Dataset
- Source: Trending YouTube time-series, subsampled to 200,000 snapshots.
- Columns: `videostatsid`, `ytvideoid`, `views`, `comments`, `likes`, `dislikes`, `timestamp`.
- Dataset note: the checklist’s `datasnaek` YouTube CSV is no longer hosted, so this openly available time-series version is used instead. It carries engagement metrics over time rather than title/category metadata, so the analysis focuses on engagement dynamics.
  
## What answers it gives / key findings
Scale: 200,000 snapshots across ~11,160 trending videos, with a mean of ~2.3M views and ~114k likes per snapshot.

Engagement scales together: views correlate 0.84 with likes and 0.68 with comments. A trending video that gets views generally gets proportional likes and comments.

Audiences are overwhelmingly positive: the median like ratio is 0.976, dislikes are rare on trending content.

Heavy right skew: all engagement metrics are heavily skewed. A few mega-viral videos dominate, which is why log scales are used in the distributions.

View velocity extension: between consecutive snapshots, the median view growth is about 7323 views/hour, while the 90th percentile is about 49971 views/hour. A small set of videos grow much faster, reinforcing the bursty nature of trending content.

## Technologies Used
- Python
- Jupyter Notebook
- pandas-data loading, cleaning, grouping, time-based features
- NumPy-numeric operations and log transforms
- Matplotlib-histograms, scatter plots, bar charts
- Seaborn-correlation heatmap and statistical visualization
- Git / GitHub-version control and project hosting

## What else could be added to improve the project / get more key insights
- Build a simple view-growth forecasting or trend-detection model using the timestamp snapshots.
- Add video metadata such as title, category, channel, and publish time to compare engagement by category, channel size, and upload age.

- 
