import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from copy import deepcopy

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

mpg_df_raw = load_data("internet.csv")
mpg_df = deepcopy(mpg_df_raw)

st.title("Introduction to Streamlit")
st.header("Internet Data Exploration")

if st.checkbox("Show Dataframe"):
    st.subheader("This is my dataset:")
    st.dataframe(mpg_df)

left_column, middle_column, right_column = st.columns([3, 1, 1])

numeric_cols = mpg_df.select_dtypes(include=['number']).columns
object_cols = mpg_df.select_dtypes(include=['object']).columns

if len(numeric_cols) >= 2:
    col_x = numeric_cols[0]
    col_y = numeric_cols[1]
else:
    col_x = mpg_df.columns[0]
    col_y = mpg_df.columns[0]

if len(object_cols) > 0:
    group_col = object_cols[0]
else:
    group_col = mpg_df.columns[0]

if "year" in mpg_df.columns:
    years = ["All"] + sorted(pd.unique(mpg_df["year"]))
    year = left_column.selectbox("Choose a year", years)
    if year == "All":
        reduced_df = mpg_df
    else:
        reduced_df = mpg_df[mpg_df["year"] == year]
else:
    reduced_df = mpg_df

show_means = middle_column.radio("Show Class Means", ["Yes", "No"])

plot_types = ["Matplotlib", "Plotly"]
plot_type = right_column.radio("Choose Plot type", plot_types)

means = reduced_df.groupby(group_col).mean(numeric_only=True)

if plot_type == "Matplotlib":
    m_fig, ax = plt.subplots(figsize=(10, 8))
    ax.scatter(reduced_df[col_x], reduced_df[col_y], alpha=0.7)
    ax.set_title("Data Exploration Plot")
    ax.set_xlabel(col_x)
    ax.set_ylabel(col_y)

    if show_means == "Yes" and col_x in means.columns and col_y in means.columns:
        ax.scatter(means[col_x], means[col_y], alpha=0.7, color="red", label="Class Means")
    st.pyplot(m_fig)

else:
    p_fig = px.scatter(
        reduced_df, 
        x=col_x, 
        y=col_y, 
        opacity=0.5,
        width=750, 
        height=600, 
        labels={col_x: col_x, col_y: col_y},
        title="Data Exploration Plot"                   
    )
    p_fig.update_layout(title_font_size=22)

    if show_means == "Yes" and col_x in means.columns and col_y in means.columns:
        p_fig.add_trace(go.Scatter(x=means[col_x], y=means[col_y], mode="markers", marker={"color": "red"}))
        p_fig.update_layout(showlegend=False)
    st.plotly_chart(p_fig)

url = "https://archive.ics.uci.edu/ml/datasets/auto+mpg"
st.write("Data Source", url)

st.subheader("Streamlit Map")
ds_geo = px.data.carshare()
st.dataframe(ds_geo.head())

ds_geo["lat"] = ds_geo["centroid_lat"]
ds_geo["lon"] = ds_geo["centroid_lon"]
st.map(ds_geo)
