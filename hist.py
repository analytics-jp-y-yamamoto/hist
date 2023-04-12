import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# ページのタイトル設定
st.set_page_config(
    page_title="histogram",
)

# csv読み込み
df0 = pd.read_csv('test.csv', index_col=0)

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
        unsafe_allow_html=True,
    )

    shop_list=st.session_state.df0.columns.values
    Day_list=st.session_state.df0.index.values
    shop_list_selector=st.sidebar.selectbox( "ショップ選択",shop_list)
    Day_list_selector=st.sidebar.selectbox( "日時選択",Day_list)

    hist_array=[]
    top5=[]
    day5=[]


    for i in range(10):
        hist_array.append(st.session_state.df0[shop_list[i]][Day_list_selector])

    top=st.session_state.df0.sort_values(shop_list_selector,ascending=False)[:5][shop_list_selector]

    shop_list_top5=st.session_state.df0.iloc[0]
    shop_list_top5=shop_list_top5[:5]

    fig1, ax1 = plt.subplots()
    fig2, ax2 = plt.subplots()

    ax1.hist(hist_array,bins=4)
    ax1.set_title("全店売上金額度数表")
    ax1.set_xlabel(Day_list_selector)
    #ax1.set_ylabel("年齢")


    ax2.bar(top.index.values,top)
    ax2.set_title(shop_list_selector+"店上位5位売り上げ")

    st.pyplot(fig1)
    st.pyplot(fig2)

    #st.text(top.index.values)
    #st.text(st.session_state.df0)
    #st.text(st.session_state.df0.at[Day_list_selector,shop_list_selector])

# ページ判定
if st.session_state.page_id == -1:
    main_page()

![スクリーンショット 2023-04-12 15 11 51](https://user-images.githubusercontent.com/129849323/231367510-7c6ffeca-672a-4563-80d9-dd3f5d249c5e.png)
