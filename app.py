import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import plotly.io as pio
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Macroeconomic Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

pio.templates.default = "plotly_dark"

# -------------------------
# LOAD CSS
# -------------------------
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# -------------------------
# DATA FUNCTIONS
# -------------------------
@st.cache_data
def load_global_economy():
    try:
        df = pd.read_csv("global_economy.csv")
        df["Date"] = pd.to_datetime(df["Date"])
        df["Year"] = df["Date"].dt.year
        return df.sort_values("Date")
    except:
        return pd.DataFrame()


@st.cache_data
def load_world_countries():
    df_full = px.data.gapminder()
    df = df_full.query("year == 2007").copy()

    df["Pre_Conflict_GDP_Billion"] = (df["gdpPercap"] * df["pop"]) / 1e9

    rng = np.random.default_rng(42)

    df["Post_Conflict_GDP_Billion"] = (
        df["Pre_Conflict_GDP_Billion"] * rng.uniform(0.90, 1.15, len(df))
    )

    df["Exports_Billion"] = (
        df["Pre_Conflict_GDP_Billion"] * rng.uniform(0.10, 0.40, len(df))
    )

    df["Imports_Billion"] = (
        df["Pre_Conflict_GDP_Billion"] * rng.uniform(0.10, 0.40, len(df))
    )

    df = df.rename(columns={
        "country": "Country",
        "continent": "Continent"
    })

    return df.sort_values("Country"), df_full


# -------------------------
# LOAD DATA
# -------------------------
df_economy_raw = load_global_economy()
df_world, df_world_full = load_world_countries()


# -------------------------
# CUSTOM METRIC
# -------------------------
def custom_metric(title, value_raw, delta):
    try:
        val = float(value_raw)
        formatted_value = f"${val:,.2f}"
    except:
        formatted_value = str(value_raw)

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{formatted_value}</div>
        <div class="metric-delta">{delta}</div>
    </div>
    """, unsafe_allow_html=True)


# -------------------------
# SIDEBAR MENU
# -------------------------
with st.sidebar:

    st.markdown("## 🌍 Macro Dashboard")

    selected = option_menu(
        menu_title=None,
        options=[
            "Market Impact",
            "Economic Map",
            "Countries Comparison",
            "Country Analysis"
        ],
        icons=[
            "graph-up-arrow",
            "globe-americas",
            "bar-chart-line",
            "search"
        ],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "#161B22"
            },
            "icon": {"color": "#58A6FF", "font-size": "18px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "5px",
                "border-radius": "12px"
            },
            "nav-link-selected": {
                "background-color": "#238636"
            },
        },
    )


# -------------------------
# MARKET IMPACT
# -------------------------
if selected == "Market Impact":

    st.title("Global Economy & Geopolitical Conflicts")

    if df_economy_raw.empty:
        st.warning("Add global_economy.csv file")
        st.stop()

    latest = df_economy_raw.iloc[-1]

    c1, c2, c3, c4 = st.columns(4)

    def safe(v):
        try:
            return float(v)
        except:
            return 0.0

    with c1:
        custom_metric("Oil Price", round(safe(latest['Oil_Price']), 2), "Live")

    with c2:
        custom_metric("EUR/USD", round(safe(latest['EUR_USD']), 4), "FX")

    with c3:
        custom_metric("USD/CHF", round(safe(latest['USD_CHF']), 4), "Forex")

    with c4:
        custom_metric("STOXX 50", round(safe(latest['Europe_Stock']), 2), "Europe")


    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(
            x=df_economy_raw["Date"],
            y=df_economy_raw["Oil_Price"],
            name="Oil Price",
            line=dict(color="#F85149", width=3)
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(
            x=df_economy_raw["Date"],
            y=df_economy_raw["Europe_Stock"],
            name="STOXX 50",
            line=dict(color="#58A6FF", width=2, dash="dot")
        ),
        secondary_y=True
    )

    fig.update_layout(
        height=650,
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22",
        font=dict(color="white")
    )

    st.plotly_chart(fig, use_container_width=True)


# -------------------------
# ECONOMIC MAP
# -------------------------
elif selected == "Economic Map":

    st.title("Interactive World Economic Map")

    metric = st.selectbox(
        "Select Metric",
        [
            "Pre_Conflict_GDP_Billion",
            "Post_Conflict_GDP_Billion",
            "Exports_Billion",
            "Imports_Billion"
        ]
    )

    fig_map = px.choropleth(
        df_world,
        locations="iso_alpha",
        color=metric,
        hover_name="Country",
        color_continuous_scale="Viridis"
    )

    fig_map.update_layout(height=700, paper_bgcolor="#0E1117")

    st.plotly_chart(fig_map, use_container_width=True)


# -------------------------
# COUNTRIES COMPARISON
# -------------------------
elif selected == "Countries Comparison":

    st.title("World Countries Comparison")

    fig = px.scatter(
        df_world,
        x="Pre_Conflict_GDP_Billion",
        y="Post_Conflict_GDP_Billion",
        color="Continent",
        size="pop",
        hover_name="Country"
    )

    fig.update_layout(
        height=700,
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22"
    )

    st.plotly_chart(fig, use_container_width=True)


# -------------------------
# COUNTRY ANALYSIS
# -------------------------
elif selected == "Country Analysis":

    st.title("Country Deep Analysis")

    country = st.selectbox(
        "Select Country",
        df_world["Country"]
    )

    row = df_world[df_world["Country"] == country].iloc[0]

    c1, c2, c3 = st.columns(3)

    with c1:
        custom_metric("Pre GDP", row['Pre_Conflict_GDP_Billion'], "")

    with c2:
        custom_metric("Post GDP", row['Post_Conflict_GDP_Billion'], "")

    with c3:
        custom_metric(
            "Trade Balance",
            row['Exports_Billion'] - row['Imports_Billion'],
            ""
        )