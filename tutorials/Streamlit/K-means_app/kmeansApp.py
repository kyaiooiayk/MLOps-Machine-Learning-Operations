"""
Creates a Kmeans model and plot the results in a web browser.
Gives the option to the user to change the number of cluster via 
a sidebar

References:
Article: https://www.kdnuggets.com/2021/09/create-stunning-web-apps-data-science-projects.html
Code: https://github.com/ThuwarakeshM/Streamlit-Intro
"""


# Imports
#========
from scipy.sparse import data
import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()


# Helper functions
#=================
# Load data from external source
@st.cache
def load_data():
    df = pd.read_csv(
        "./voters_demo_sample.csv"
    )
    return df


df = load_data()


def run_kmeans(df, n_clusters=2):
    kmeans = KMeans(n_clusters, random_state=0).fit(df[["Age", "Income"]])

    fig, ax = plt.subplots(figsize=(16, 9))

    ax.grid(True)
    ax.set_facecolor("#FFF")
    ax.spines["bottom"].set_visible(True)
    ax.spines["left"].set_visible(True)
    #ax.spines[["left", "bottom"]].set_color("#4a4a4a")
    ax.tick_params(labelcolor="k")
    ax.yaxis.label.set(color="k", fontsize=20)
    ax.xaxis.label.set(color="k", fontsize=20)

    # Create scatterplot
    ax = sns.scatterplot(
        ax=ax,
        x=df.Age,
        y=df.Income,
        hue=kmeans.labels_,
        palette=sns.color_palette("colorblind", n_colors=n_clusters),
        legend=None,
    )

    # Annotate cluster centroids
    for ix, [age, income] in enumerate(kmeans.cluster_centers_):
        ax.scatter(age, income, s=200, c="#a8323e")
        ax.annotate(
            f"Cluster #{ix+1}",
            (age, income),
            fontsize=25,
            color="#a8323e",
            xytext=(age + 5, income + 3),
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#a8323e", lw=2),
            ha="center",
            va="center",
        )

    return fig


# SIDEBAR
#========
sidebar = st.sidebar
df_display = sidebar.checkbox("Display Raw Data", value=True)

n_clusters = sidebar.slider(
    "Select Number of Clusters",
    min_value=2,
    max_value=10,
)

sidebar.write(
    """
    This is just an example on how to add text and link
    - [LinkedIn](https://linkedin.com)
    """
)


# Main
#=====
# Create a title for your app
st.title("Interactive K-Means Clustering")

# Show cluster scatter plot
st.write(run_kmeans(df, n_clusters=n_clusters))

if df_display:
    st.write(df)
# -----------------------------------------------------------