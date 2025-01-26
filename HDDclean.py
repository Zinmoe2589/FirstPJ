import pandas as pd
import streamlit as st
import plotly.express as px
df = pd.read_csv('HDDclean.csv')
st.set_page_config(page_title='My Resale List 2019',page_icon=':bar_chart:',layout='wide')
st.sidebar.header("Please Filter Here")
town_name = st.sidebar.multiselect(
    "Select Town",
    options = df['town'].unique(),
    default = df['town'].unique()[:6])
flat_model_name = st.sidebar.multiselect(
    "Select Flat Model",
    options = df['flat_model'].unique(),
    default = df['flat_model'].unique()[:6])
storey_range_name = st.sidebar.multiselect(
    "Select Storey Range",
    options = df['storey_range'].unique(),
    default = df['storey_range'].unique()[:6])
st.title(":bar_chart: Resale Flat Model For Each Town")
st.markdown("##")
total_town = df['town'].nunique()
types_of_flat_model = df['flat_model'].nunique()
leftcol,rightcol = st.columns(2)
with leftcol:
    st.subheader('Total Town')
    st.subheader(f"{total_town} Towns")
with rightcol:
    st.subheader('Total Flat Model Type')
    st.subheader(f"{types_of_flat_model} Types")
df_select = df.query("town==@town_name and flat_model==@flat_model_name and storey_range==@storey_range_name")
aa=df_select.groupby('town')['resale_price'].mean().sort_values()
fig_resale_by_town = px.bar(
    aa,
    x=aa.index,
    y=aa.values,
    title="Resale Price By Town")
a,b,c=st.columns(3)
a.plotly_chart(fig_resale_by_town,use_container_width=True)
bb=df_select.groupby('flat_model')['resale_price'].mean().sort_values()
fig_resale_by_flat_model = px.bar(
    bb,
    x=bb.index,
    y=bb.values,
    title="Resale Price By Flat Model")
b.plotly_chart(fig_resale_by_flat_model,use_container_width=True)
cc=df_select.groupby('storey_range')['resale_price'].mean().sort_values()
fig_resale_by_storey_range = px.bar(
    cc,
    x=cc.index,
    y=cc.values,
    title="Resale Price By Storey Range")
c.plotly_chart(fig_resale_by_storey_range,use_container_width=True)
d,e=st.columns(2)
line_fig_resale_by_town = px.line(
    aa,
    x=aa.values,
    y=aa.index,
    title="Resale Price By Town")
d.plotly_chart(line_fig_resale_by_town,use_container_width=True)
pie_fig_resale_by_flat_model = px.pie(
    df_select,
    values='resale_price',
    names='flat_model',
    title="Resale Price By Flat Model")
e.plotly_chart(pie_fig_resale_by_flat_model,use_container_width=True)
f,g = st.columns(2)
scatter_fig_resale_by_storey_range = px.scatter(
    cc,
    x=cc.values,
    y=cc.index,
    title="Resale Price By Storey Range")
f.plotly_chart(scatter_fig_resale_by_storey_range,use_container_width=True)

