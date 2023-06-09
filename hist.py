import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib

# ページのタイトル設定
st.set_page_config(
    page_title = "histogram",
)

# csv読み込み
df0 = pd.read_csv('hist.csv', index_col=0)

# セッション情報の初期化
if "page_id" not in st.session_state:
    st.session_state.page_id = -1
    st.session_state.df0 = df0

# 各種メニューの非表示設定
hide_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_style, unsafe_allow_html=True)

# 最初のページ
def main_page():
    st.markdown(
        "<h1 style='text-align: center;'>ヒストグラム表示</h1>",
        unsafe_allow_html = True,
    )

    column_list = st.session_state.df0.columns.values
    data_list = st.session_state.df0.index.values
    data_list_selector = st.sidebar.selectbox( "データセット選択", data_list)
    bin = st.sidebar.slider('binの数を決めてください', 5, 100, 25)

    hist_array = []
    for i in range(st.session_state.df0.shape[1]):
        hist_array.append(st.session_state.df0[column_list[i]][data_list_selector])

    Y, X, _ = plt.hist(hist_array, bins = bin, range = (-1, 1))
    y_max = int(max(Y)) + 1

    fig1, ax1 = plt.subplots()

    ax1.hist(hist_array, bins = bin, ec = 'navy', range = (-1, 1))
    ax1.set_title("標準正規分布"+str(st.session_state.df0.shape[1])+"個データ")
    ax1.set_xlabel(data_list_selector)
    ax1.set_ylabel("度数")
    ax1.set_yticks(np.arange(0,y_max,int(y_max/10)))

    st.pyplot(fig1)

# ページ判定
if st.session_state.page_id == -1:
    main_page()

    #タイタニックデータセットの分析
    #コードの修正
    #なんでこういうデザインにしたのか？
