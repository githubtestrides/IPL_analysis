import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

import helper

df=pd.read_csv('IPL Matches 2008-2020 (1).csv')
st.sidebar.title("IPL ANALYSIS")

image = Image.open('ipl.jpg')

st.sidebar.image('ipl.jpg')


user_menu=st.sidebar.radio(
    'select an option',
    ('Overall Analysis','max_Player of Match','max_Time winner Team','max_time first umpire','max_time second umpire','Toss_Analysis')
)

if user_menu=='Overall Analysis':

    st.title('Overall Analysis')


    temp_df = helper.clean_df(df)
    temp_df = df
    st.dataframe(temp_df)

if user_menu=='max_Player of Match':
    st.title('maxmimum no of player of matches')
    player = df['player_of_match'].value_counts().reset_index()
    player.rename(columns={'index': 'player', 'player_of_match': 'counts'}, inplace=True)
    st.dataframe(player)
    ax = px.bar(df, x=list(df['player_of_match'].value_counts().keys())[0:10],
                y=list(df['player_of_match'].value_counts())[0:10])
    st.plotly_chart(ax)

if user_menu=='max_Time winner Team':
    st.title('max_time winner Team')
    winner = df['winner'].value_counts().reset_index()
    winner.rename(columns={'index': 'Teams', 'winner': 'Counts'}, inplace=True)
    st.dataframe(winner)



    fig = px.bar(df, x=list(df['winner'].value_counts().keys())[0:10], y=list(df['winner'].value_counts()[0:10]),
                 color=list(df['winner'].value_counts()[0:10]),
                 labels={'pop': 'population of Canada'}, height=400)
    st.plotly_chart(fig)

if user_menu=='max_time first umpire':
    st.title('max_time first umpire')
    umpire = df['umpire1'].value_counts().reset_index()
    umpire.rename(columns={'index': 'umpires', 'umpire1': 'counts'}, inplace=True)
    st.dataframe(umpire)
    fig = px.bar(df,  x=list(df['umpire1'].value_counts().keys())[0:10],y=list(df['umpire1'].value_counts())[0:10],
                 text_auto='.2s',
                 title="max_time first umpire")
    st.plotly_chart(fig)

if user_menu=='max_time second umpire':
    st.title('max_time second umpire')
    umpire2 = df['umpire2'].value_counts().reset_index()
    umpire2.rename(columns={'index': 'umpires', 'umpire2': 'counts'}, inplace=True)
    st.dataframe(umpire2)

    fig = px.bar(df, x=list(df['umpire2'].value_counts().keys())[0:10], y=list(df['umpire2'].value_counts())[0:10],
                 text_auto='.2s',
                 title="max_time second umpire")
    st.plotly_chart(fig)

if user_menu=='Toss_Analysis':
    st.title('Toss Winners')
    toss = df['toss_winner'].value_counts().reset_index()
    toss.rename(columns={'index': 'Teams', 'toss_winner': 'counts'}, inplace=True)
    st.dataframe(toss)

if user_menu=='Toss_Analysis':

    fig = px.bar(df, y=list(df['toss_winner'].value_counts()), x=list(df['toss_winner'].value_counts().keys()),
                 text_auto='.2s',
                 title="Toss Winners")
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig)








