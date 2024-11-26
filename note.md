jupyter notebook --NotebookApp.iopub_data_rate_limit=1e7  # This sets the limit to 10,000,000 bytes/sec

dealing with missing values cat_cols  investigate between setting missing value to missing or dropping them or choose most frequent

dealing with missing numerical values experiment with replacing with zero, median or mean

do more data exploration

Seaborn is a powerful data visualization library in Python, designed to make statistical graphics more attractive and easier to generate. It offers a wide variety of plot types to cater to different needs for data analysis and presentation. Here are the main types of plots you can create with Seaborn:

1. Relational Plots
These are useful for visualizing relationships between two or more variables.

Scatter plot (scatterplot) - Used to visualize the relationship between two continuous variables.
Line plot (lineplot) - Useful for plotting data over time or ordered categories.
2. Categorical Plots
These plots are ideal for showing the distribution of a dataset across different categories.

Bar plot (barplot) - Shows an estimate of the central tendency for a numeric variable with the height of each rectangle.
Count plot (countplot) - Used for displaying counts of observations in each categorical bin.
Box plot (boxplot) - Used to display the distribution of a variable across different categories using quartiles and outliers.
Violin plot (violinplot) - Combines aspects of box plots and density plots, showing the distribution of the data across categories.
Point plot (pointplot) - Estimates central tendency using a point and provides some indication of the uncertainty around that estimate.
3. Distribution Plots
These plots are great for examining univariate and bivariate distributions.

Histogram (histplot) - Shows the distribution of a dataset and can include kernel density estimation (KDE).
KDE Plot (kdeplot) - Visualizes the density of observations at different values in a continuous variable.
ECDF Plot (ecdfplot) - The empirical cumulative distribution function plot.
4. Matrix Plots
Ideal for displaying data where the rows and columns both are categorical variables.

Heatmap (heatmap) - Used to visualize matrix-like data, good for correlation matrices.
Cluster map (clustermap) - Organizes data into clusters and represents them as a heatmap.
5. Regression Plots
These are used to plot data and a linear regression model fit.

Reg plot (regplot) - Plots the scatter plot plus the linear regression line for two variables.
LM plot (lmplot) - Combines regplot and FacetGrid, allowing you to plot multiple linear relationships in a dataset.
6. Multi-Plot Grids
These allow you to draw multiple subplots of certain kinds of plots.

Pair plot (pairplot) - Plots pairwise relationships in a dataset.
Facet Grid (FacetGrid) - Used to draw plots with multiple subplots based on the features of your dataset.
Pair Grid (PairGrid) - Allows for complex customization of pair-wise plots.
7. Miscellaneous Plots
Joint plot (jointplot) - Used to display a relationship between 2 variables along with each variable’s marginal distribution.
Strip plot (stripplot) - Draws a scatterplot where one variable is categorical.
Swarm plot (swarmplot) - Similar to stripplot, but the points are adjusted so they don’t overlap.
These are the general categories of plots available in Seaborn, each suited for different data visualization needs. You can combine these plots in various ways to create complex visualizations tailored to your specific analysis requirements.

